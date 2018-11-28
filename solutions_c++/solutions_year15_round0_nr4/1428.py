#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<ctime>
#include<cmath>

#include<algorithm>
#include<bitset>
#include<complex>
#include<deque>
#include<iostream>
#include<map>
#include<numeric>
#include<queue>
#include<stack>
#include<string>
#include<set>
#include<vector>
using namespace std;

#define pb push_back
#define mp make_pair
#define x first
#define y second
#define sz(a) (int((a).size()))
#define all(a) (a).begin(), (a).end()

#define For(it,c) for(typeof(c) it = ((c).begin()); it != ((c).end()) ; ++it)

#define forn(i,n) for (int i=0; i<int(n); ++i)
#define fornd(i,n) for (int i=int(n)-1; i>=0; --i)
#define forab(i,a,b) for (int i=int(a); i<int(b); ++i)

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

typedef complex<int> cI;
typedef complex<double> cD;

typedef pair<int,int> pI;
typedef pair<ll, ll> pL;

const int INF = (int) 1e9;
const long long INF64 = (long long) 1e18;
const long double eps = 1e-9;
const long double pi = 3.14159265358979323846;


int main()
{
  int T;
  int X, R, C;
  bool flag;
  cin >> T;
  for(int z=1;z<=T;z++){
    cin >> X >> R >> C;
    flag = true;
    if(C < R) swap(C, R);
    if(R*C % X) flag = false;
    if(X==4 && (R==1 || R==2 || C < 4 )) flag = false;
    if(X==3 && (R==1 || C < 3)) flag = false;
    printf("Case #%d: %s\n", z, flag?"GABRIEL":"RICHARD");
  }
  return 0;
}
