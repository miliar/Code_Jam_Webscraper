#include<iostream>
#include <vector>
#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);
   int Test;
   cin >> Test;
   for (int t = 0; t < Test; ++t){
       double C, F, X;
       cin >> C >> F >> X;
       double Tt = 0, cc = 0;
       double res = 1e100;
       for (int cnt = 0; cnt < 100000; ++cnt) {
            res = min(res, Tt + (X - cc) / (F*cnt + 2));
            Tt += (C - cc)/(F * cnt + 2); 
       }
       cout.precision(20);
       cout << "Case #" << t + 1 << ": " << res << endl; 
   }
}