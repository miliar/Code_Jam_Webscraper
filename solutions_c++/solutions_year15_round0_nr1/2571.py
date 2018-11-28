 #include <bits/stdc++.h>
 using namespace std;
 
 int main(int argc, char** argv) {
     int tests, smax;
     string slist;
     cin >> tests;
     for (int test = 1; test <= tests; test++) {
         cin >> smax >> slist;
         int maxi = 0, cur = 0;
         for (int i = 0; i <= smax; i++) {
             if (i-cur > 0)
                 maxi = maxi < (i-cur) ? (i-cur) : maxi;
             cur += slist[i]-'0';
         }
         cout << "Case #" << test << ": " << maxi << endl;
     }
     return 0;
 }