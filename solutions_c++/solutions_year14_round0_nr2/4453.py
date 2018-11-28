#include <iostream>
#include <string>
#include <set>
#include <sstream>
#include <iomanip>

using namespace std;

string tos(double q, int d=7) {
  stringstream A;
  A<<fixed<<setprecision(d)<<q; 
  string s; 
  A >> s; 
  return s; 
}

void solve(int ind) {
    // input
    double factoryPrice, factoryProd, target;
    cin >> factoryPrice >> factoryProd >> target;
    const double yourProd = 2.0;
    
    int nF = 0;
    double timeSoFar = 0;
    while (true) {
        // how much time it will take to get X with current production rate
        double prod = yourProd + nF * factoryProd;
        double tCur = target / prod;
        // how much time it will take to get C, buy factory and then get X
        double tC = factoryPrice / prod;
        prod += factoryProd;
        double tAfter = target / prod;
        if (tCur > tC + tAfter) {
            // buying more factories makes sense; buy 1
            timeSoFar += tC;
            ++nF;
        } else {
            break;
        }
    }
    
    double prod = yourProd + nF * factoryProd;
    double res = timeSoFar + target / prod;
    // output
    cout << "Case #" << ind << ": " << tos(res) << endl;
}

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        solve(i);
    }
}