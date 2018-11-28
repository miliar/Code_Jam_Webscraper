#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <limits>
#include <bitset>
#include <utility>
#include <iomanip>
#include <set>
#include <fstream>
#include <numeric>
#include <stdexcept>
#include <cassert>

#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define INF_LL 9223372036854775807LL
#define INF 2000000000
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

int n;
LL x;
string in;
bool DP[10005][2][4][25][3];
int mul[4][4];
map<char, int> m;
int MAGIC;

bool solve(int ind, bool sign, int num, int level,int target)
{
  if(level == min(23LL, x)) return false;
  if(ind == n)
  {
    if(target == 2 && num == 3 && !sign)
      if((x - level - 1) % MAGIC == 0)
        return true;
    bool res = false;
    if(target == num - 1 && target != 2 && !sign)
      res=solve(0, 0, 0, level + 1, target + 1);
    res = res | solve(0, sign, num, level + 1, target);
    return res;
  }
  if(DP[ind][sign][num][level][target]) return false;
  DP[ind][sign][num][level][target] = true;
  if(target == num - 1 && target != 2 && !sign)
    if(solve(ind, 0, 0, level, target + 1))
      return true;
  int res = mul[num][m[in[ind]]];
  if(res < 0)
    sign = !sign;
  res = abs(res);
  if(res == 4) res = 0;
  return solve(ind + 1, sign, res, level, target);
}

int main()
{
  ios_base::sync_with_stdio(0);
  freopen("C-small-attempt1.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  int t, tt = 1;
  cin >> t;
  mul[0][0] = 0;
  mul[0][1] = 1;
  mul[0][2] = 2;
  mul[0][3] = 3;

  mul[1][0] = 1;
  mul[1][1] = -4;
  mul[1][2] = 3;
  mul[1][3] = -2;

  mul[2][0] = 2;
  mul[2][1] = -3;
  mul[2][2] = -4;
  mul[2][3] = 1;

  mul[3][0] = 3;
  mul[3][1] = 2;
  mul[3][2] = -1;
  mul[3][3] = -4;

  m['i'] = 1;
  m['j'] = 2;
  m['k'] = 3;
  while(t--)
  {
    cin >> n >> x >> in;
    bool sign = 0;
    int num = 0;
    for(int i=0;i<n;i++)
    {
      num = mul[num][m[in[i]]];
      if(num < 0)
        sign = !sign;
      num = abs(num);
      if(num == 4) num = 0;
    }
    if(num == 0)
    {
      if(sign) MAGIC = 2;
      else MAGIC = 1;
    }
    else MAGIC = 4;
    setzero(DP);
    bool sol = solve(0, 0, 0, 0, 0);
    cout << "Case #" << tt++ << ": " ;
    if(sol) cout << "YES\n";
    else cout << "NO\n";
  }
  return 0;
}
