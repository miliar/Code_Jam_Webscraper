#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>
#include <iomanip>

using namespace std;


// given C, F, X, return the critical point n*,
// which is when n = n*, the time cost is minimum
// assume all parameteres are positive
inline double nStar(const double C, const double F, const double X) {
    return X/C - 2.0/F;
}

// given C, F, X and the number of farms which need to be bought,
// return the minimum time cost
// assume n >= 0, other parameteres are all positive
double timeCost(const int n, const double C, const double F, const double X) {
    double cost = X/(2.0+n*F);
    double sum = 0;
    for (int i = 0; i < n; i++) sum += 1.0/(2.0+i*F);
    sum *= C;
    cost += sum;
    return cost;
}

// calculate the extra time cost with n+1 farms, compared with n farms
// assume n >= 0
inline double extraCost(const int n, const double C, const double F, const double X) {
    return X/(2.0+(n+1)*F) - (X-C)/(2.0+n*F);
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        cerr << "Need input file!" << endl;
        return 1;
    }
    ifstream input(argv[1]); // bind and open the input file
    // check whether open sucessfully
    if (!input) {
        cerr << "unable to open the input file!" << endl;
        return 1;
    }
    
    // set output format
    cout << fixed;
    cout << setprecision(7);
    
    int N; // number of cases
    input >> N;
    input.ignore(256, '\n'); // ignore the rest of the line
    
    // consider each case
    int i = 1; // index of case
    string line; // one line
    while (getline(input, line)) {
        stringstream ss(line);
        double C, F, X;
        ss >> C >> F >> X;
        int nstar = floor(nStar(C, F, X)); // calculate the critical value for n
        double tc; // time cost
        if (nstar < 0) tc = timeCost(0, C, F, X); // no farm
        else {
            tc = timeCost(nstar, C, F, X); // nstar farm
            double dtc = extraCost(nstar, C, F, X); // also needs to compare with the case of nstar+1 farms
            if (dtc < 0) tc += dtc;
        }
        cout << "Case #" << i << ": " << tc << endl;
        i++;
    }
    
    input.close(); // close file before return
    return 0;
    
}