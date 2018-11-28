
#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <climits>
#include <limits.h>
#include <string>
#include <stack>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <assert.h>
#include <cstring>
using namespace std;
#define rep(i, n) for (int (i) = 0, j1234 = n; (i) < j1234; (i) ++)
#define rep1(i, n) for (int (i) = 1, j1234 = n; (i) <= j1234; (i) ++)
#define For(i, a, b) for (int (i) = (a), ub1234=b; (i) <= ub1234; (i) ++)
#define db(x) {if(debug){cout << #x << " = " << (x) << endl;}}
#define dba(a, x, y) {if(debug){cout << #a << " :";For(i, (x), (y))cout<<" "<<(a)[(i)];cout<<endl;}}
#define clr(x) memset(x,0,sizeof(x));
#define mp make_pair
#define pb push_back
#define endl '\n'
#define ll long long
#define ld long double
const int INF = INT_MAX;
const ll INFL = LLONG_MAX;
const int output_precision = 15;
const ld pi = acos(-1);
const bool debug = true;
// const ll MOD = ;

int A[10010];
// 1 -> 1
// i -> 2
// j -> 3
// k -> 4
int calcres[5][5] = {
  {0, 0, 0, 0, 0},
  {0, 1, 2, 3, 4},
  {0, 2,-1, 4,-3},
  {0, 3,-4,-1, 2},
  {0, 4, 3,-2,-1}};
   

int mul(int a, int b)
{
  int sgn = 1;
  if (a < 0) 
  {
    sgn *= -1;
    a *= -1;
  }
  if (b < 0) 
  {
    sgn *= -1;
    b *= -1;
  }
  return sgn * calcres[a][b];
}
int solve()
{
  int L, X;
  string s;
  stringstream ss;
  cin >> L >> X >> s;
  rep(foo,X)
  ss << s;
  s = ss.str();
  s = " " + s;
  clr(A);
  int N = L * X;
  rep1(i,N)
  {
    switch(s[i])
    {
      case '1':
        A[i] = 1;
        break;
      case 'i':
        A[i] = 2;
        break;
      case 'j':
        A[i] = 3;
        break;
      case 'k':
        A[i] = 4;
        break;
    }
  }
//  if (N<20)
//  dba(A,1,N);
  int cur = A[1];
  int seen2 = 0;
  int seen4 = 0;
  for (int i = 1; i <= N; i++)
  {
    if (!seen2 && cur==2)
      seen2=1;
    if (seen2 && !seen4 && cur==4)
      seen4=1;
    if (i + 1 <= N) cur = mul(cur,A[i+1]);
  }
  if (seen2 && seen4 && (cur==-1))
    return 1;
  else
    return 0;
}
int T;
int main()
{
  ios_base::sync_with_stdio(0); cout.precision(output_precision); cout << fixed;
  cout.tie(0);
  cin >> T;
  rep1(testnumber,T)
  {
    cout << "Case #" << testnumber << ": " << (solve()?"YES":"NO") << endl;
  }

}
