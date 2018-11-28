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

const long double eps = 1e-8;


int main()
{
  int T;
  double C, F, X;
  double ans, ansNxt;
  double totalT, speed;
  cin >> T;
  for(int z=1;z<=T; z++){
    cin >> C >> F >> X;
    ans = X / 2;
    totalT = 0;
    speed = 2;
    while(totalT < ans){
      if(totalT + C / speed > ans - eps)break;
      totalT += C / speed;
      speed += F;
      ansNxt = totalT + X / speed;
      if(ansNxt > ans - eps)break;
      ans = ansNxt;
    }
    printf("Case #%d: %.10lf\n", z, ans);
  }
  return 0;
}
