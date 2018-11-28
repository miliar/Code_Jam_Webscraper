 #include <bits/stdc++.h>
 using namespace std;
 
 int main(int argc, char** argv) {
     int tests;
     cin >> tests;
     for (int test = 1; test <= tests; test++) {
         int a, x, y;
         cin >> a >> x >> y;
         if (a < 7 && (a == 1 || max(x,y) >= a && min(x,y) >= a-1) && x*y % a == 0)
            cout << "Case #" << test << ": GABRIEL" << endl;
         else
            cout << "Case #" << test << ": RICHARD" << endl;
     }
     return 0;
 }