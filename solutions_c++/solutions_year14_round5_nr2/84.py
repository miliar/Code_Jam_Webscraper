#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cmath>
#include <assert.h>
using namespace std;
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef long double ld;
const int INF = 1000000000;
const int prime = 9241;
const ld pi = acos(-1.);


int dp[105][205][105][2];
int h[105], g[105];
void solve(int test)
{
   int p,q,n;
   cin >> p >> q >> n;
   for (int i = 0; i < n; i++)
      cin >> h[i] >> g[i];
   for (int i = 0; i <= n; i++)
      for (int j = 0; j <= 203; j++)
         for (int k = 0; k <= n; k++)
           for (int u = 0; u < 2; u++)
            dp[i][j][k][u] = -(int)1e9;
   dp[0][h[0]][0][0] = 0;
   int answer = 0;
   for (int i = 0; i < n; i++)
   {
       for (int j = h[i]; j >= 0; j--)
          for (int k = 0; k <= n; k++)
          {
              if (dp[i][j][k][0] >= 0)
              {
                 for (int h0 = 0; h0 <= 1; h0++)
                 {
                    int rest = h0 ^ 1;
                    // h раз ударили, rest отложил
                    int afterhit = j - h0 * p;
                    if (afterhit <= 0)
                    {
                       int nl = k + rest;  
                       int forkill = 0;
                       int salary = 0;
                       for (int killed = 0; killed+i+1 <= n; killed ++)
                       {
                          for (int hits = 0; hits <= (nl-forkill) && p * hits <= h[i+killed+1]; hits++)
                          {
                              int tok = nl - forkill - hits;
                              int toi = i+killed+1;
                              int toj = h[i+killed+1] - p * hits;
                              dp[toi][toj][tok][1] = max(dp[toi][toj][tok][1], dp[i][j][k][0] + g[i] + salary);
                              answer = max(answer, dp[toi][toj][tok][1]); 
                          }
                          forkill += h[killed+i+1] / p + (h[killed+i+1] % p == 0?0:1);
                          salary += g[i+killed+1];  
                       }
                    }
                    else
                    {
                       dp[i][afterhit][k+rest][1] = max(dp[i][afterhit][k+rest][1], dp[i][j][k][0]);
                    }
                 }
              }
              if (dp[i][j][k][1] >= 0)
              {
                  int afterhit = j - q;
                  if (afterhit <= 0)
                  {
                     int nl = k;  
                     int forkill = 0;
                     int salary = 0;
                     for (int killed = 0; killed+i+1 <= n; killed ++)
                     {
                        for (int hits = 0; hits <= (nl-forkill) && p * hits <= h[i+killed+1]; hits++)
                        {
                            int tok = nl - forkill - hits;
                            int toi = i+killed+1;
                            int toj = h[i+killed+1] - p * hits;
                            dp[toi][toj][tok][0] = max(dp[toi][toj][tok][0], dp[i][j][k][1] + salary);
                            answer = max(answer, dp[toi][toj][tok][0]); 
                        }
                        forkill += h[killed+i+1] / p + (h[killed+i+1] % p == 0?0:1);
                        salary += g[i+killed+1];  
                     }
                  }
                  else
                  {
                     dp[i][afterhit][k][0] = max(dp[i][afterhit][k][0], dp[i][j][k][1]);
                  }
               
              }              
          }
   }
   cout << "Case #" << test << ": " << answer << endl;
}


int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
       solve(i);
       cerr << "test " << i << endl;
    } 
}