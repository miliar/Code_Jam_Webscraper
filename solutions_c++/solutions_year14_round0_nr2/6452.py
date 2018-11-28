//#include <iostream>
#include <fstream>
#include <cmath>
#include <iomanip>
using namespace std;

ifstream cin("B-large.in");
ofstream cout("B-large.out");

int main() {
    int T;
    cin >> T;
    for (int t=0; t<T; t++) {
       cout << "Case #" << t+1 << ": ";
       double C,F,X;
       cin >> C >> F >> X;
       double maxtime = X/2.0;
       double cur= 2.0;
       double curtime = 0;
       double pasttime = 0; 
       while (true) {
            double breakeven = C/cur;
            curtime = pasttime+breakeven;
            cur += F;
            pasttime = curtime;
            curtime += X/cur;
            if (curtime >= maxtime) break;
            maxtime = min(maxtime,curtime);
       }
       cout << fixed << setprecision(7) << maxtime << endl;
    }
return 0;
}
