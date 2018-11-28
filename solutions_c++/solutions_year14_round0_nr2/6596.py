#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cassert>
#include <string.h>
#include <sstream>
#include <fstream>
#include  <iomanip>


using namespace std;

#define ll unsigned long long

template<class T> string toString(T n){ostringstream ost;ost<<n;ost.flush();return ost.str();}//NOTES:toString(

const ll MOD = 1000000007;

const double ep = 1e-10;


int main() {

    int tt;

    ifstream cin("B-large.in");
    ofstream cout("ans.txt");
   // cout << ep << endl;

    cin >> tt;

    int cc = 1;

    while (tt--) {

        double c, f, x;

        cin >> c >> f >> x;

        double t = 0.0, v = 2, s = 0;

        while (s < x) {

            if (x - s < c) {
                t += (x - s) / v;
                break;
            }

            double y = c / v;
            t += y;
            s += c;

            if ((x / (v + f)) < ((x - s) / v))
            {
                s = 0;
                v += f;
            }
           // cout << t << endl;
        }
        cout << "Case #" << cc++ << ": " <<  setprecision(15) << t << endl;
    }

    return 0;
}
