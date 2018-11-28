#include <iostream>
#include <iomanip>  
#include <stdio.h>
#include <map>
#include <string>
#include <vector>
#include <queue>   
#include <algorithm>
#include <math.h>
#include <set>
#include <stdlib.h>
#include <stack> 
using namespace std;

#define fr(i,n)    for(int i=0;i<n;i++)
#define fru(i,a,b) for(int i=a;i<=b;i++)
#define frd(i,a,b) for(int i=a;i>=b;i--)

typedef long long   ll;
typedef long double ld;
	
const int INF = 2e9 + 10;
const int MOD = 1e9 + 7;
const int N   = 1e6 + 10;

struct POINT {
   int x;
   int y;
   //POINT(){}
   //POINT(int x, int y): x(x), y(y){}
   //bool operator < (const POINT &e) const { return x < e.x || x == e.x && y < e.y; }
} p[N];

int n, k, m, t;

int main() {
   //ios_base::sync_with_stdio(0);
   //cout.tie(0); cin.tie(0);
   
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);

   cin >> t;
   
   fru(T, 1, t)
   {
      int k;
      string s;
      
      cin >> s >> k;
      
      int res = 0;
      fr(i, (int)s.length() - k + 1)
      {
         if(s[i] == '+')
            continue;
         
         res++;
         fru(j, i, i + k - 1)
         {
            if(s[j] == '+')
               s[j] = '-';
            else
               s[j] = '+';
         }
      }
      
      int cnt = 0;
      fr(i, (int)s.length()) if(s[i] == '+')
         cnt++;
         
      if(cnt == (int)s.length())
         cout << "Case #" << T << ": " << res << "\n";
      else      
         cout << "Case #" << T << ": " << "IMPOSSIBLE" << endl; 
   }
   
   return 0;
}