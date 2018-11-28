#include <iostream>
#include <cstring>
#include <vector>
// #include <algorithm>
#include <cassert>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <set>
#include <iomanip>

using namespace std;

vector<double> convertToIntVec(string line) {;
    vector<double> res;
    char *list =  strdup(line.c_str());
    char* next = strtok(list, " ");
    while (next) {
        res.push_back(atof(next));
        next = strtok(NULL, " ");
    }
    free(list);
    return res;
}


double cookieRecur(double C, double F, double X, double rate) {
    double t1 = X / rate;
    double t2 = C / rate;
    if (t1 < t2 + X/(rate + F)) return t1;
    return min(t1, t2 + cookieRecur(C, F, X, rate + F) );
}

double cookie(double C, double F, double X) {
    double totalTime = 0.0;
    double rate = 2.0;
    while (true) {
        double t1 = X / rate;
        double t2 = C / rate;
        if (t1 < t2 + X/(rate + F))  { // should not buy
            totalTime += t1;
            break;
        }
        totalTime += t2;
        rate += F;
    }
    return totalTime;
}

int main(int argc, char *argv[]) {
    // istream &in = cin;
    // ostream &out = cout;
    // in = &cin;
    // out = &cout;
    // ifstream inFile("tiny.in");
    // ifstream inFile("B-small-attempt0.in");
    // ofstream outFile("B-small-attempt0.out");
    // ifstream inFile("C-small-attempt0.in");
    // ifstream inFile("C-large-1.in");
    // ofstream outFile("result_large.txt");
    // ofstream outFile("C-large-1.out");
    ifstream inFile("B-large.in");
    ofstream outFile("B-large.out");
    istream &in = inFile;
    ostream &out = outFile;
    // ostream &out = cout;

    string line;
    getline(in, line);
    int T = atoi(line.c_str());
    // cout << "T: " <<  T << endl;
    for (int i = 0; i < T; ++i) {
        getline(in, line);
        auto tmp = convertToIntVec(line);
        double res = cookie(tmp[0], tmp[1], tmp[2]);
        out.setf(ios::fixed,ios::floatfield);
        out.precision(7);
        out << "Case #" << i+1 << ": " << res << endl;
    }
    return 0;
}
