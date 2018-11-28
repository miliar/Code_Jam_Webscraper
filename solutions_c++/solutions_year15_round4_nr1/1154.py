#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <limits>
#include <utility>
#include <iomanip>
#include <set>
#include <numeric>
#include <cassert>
#include <ctime>
#include <fstream>

#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define INF_LL 9223372036854775807LL
#define INF 1000000000
#define PI acos(-1.0)
#define EPS 1e-8
#define LL long long
#define mod 1000000007
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define setzero(a) memset(a,0,sizeof(a))
#define setdp(a) memset(a,-1,sizeof(a))

using namespace std;

string s[105];
int nxt[105][105][4];
char arr[] = {'<', '>', '^', 'v'};

int main()
{
  ios_base::sync_with_stdio(0);
  freopen("A-large.in", "r", stdin);
  freopen("out.txt", "w", stdout);
  int t, tt = 1, n, m;
  cin >> t;
  while(t--)
  {
    cin >> n >> m;
    for(int i=0;i<n;i++)
      cin >> s[i];
    setdp(nxt);
    //if(res != c) cerr << "Error @ " << tt << " Expected : " << res << " Found : " << c << "\n";
    cout << "Case #" << tt++ << ": ";
    int res = 0;
    bool test = true;
    for(int i=0;i<n;i++)
    {
      int last = -1;
      for(int j=0;j<m;j++)
      {
        if(s[i][j] == '.') continue;
        nxt[i][j][0] = last;
        if(last != -1)
        {
          nxt[i][last][1] = j;
        }
        last = j;
      }
    }
    for(int j=0;j<m;j++)
    {
      int last = -1;
      for(int i=0;i<n;i++)
      {
        if(s[i][j] == '.') continue;
        nxt[i][j][2] = last;
        if(last != -1)
        {
          nxt[last][j][3] = i;
        }
        last = i;
      }
    }
    for(int i=0;i<n && test;i++)
    {
      for(int j=0;test && j<m;j++)
      {
        if(s[i][j] == '.') continue;
        bool c = false;
        for(int k=0;k<4;k++)
          c |= (nxt[i][j][k] != -1);
        if(!c)
        {
          test = false;
          break;
        }
        for(int k=0;k<4;k++)
        {
          if(s[i][j] == arr[k] && nxt[i][j][k] == -1)
            res++;
        }
      }
    }
    if(test) cout << res << "\n";
    else cout << "IMPOSSIBLE\n";
  }
  return 0;
}
