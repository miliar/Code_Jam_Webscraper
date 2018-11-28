#include<iostream>
#include<algorithm>
#include<cstdio>
#include<iomanip>
#include<cmath>

using namespace std;

int main()
{
   int T;
   cin >> T;
   for(int h = 1; h <= T; ++h){
      double C, F, X;
      cin >> C >> F >> X;
      int r = ceil(X/C -1 -2/F);
      r = max(r, 0);
      double ans = 0, R = 2;
      for(int i = 0; i < r; ++i){
         ans += C / R;
         R += F;
      }
      ans += X / R;
      cout << "Case #" << h << ": ";
      cout << fixed << setprecision(7) << ans << endl;
   }
   
   
   return 0;
}

