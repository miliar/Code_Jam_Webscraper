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

int minAns[1010], eat[1010];
int K[1010];

int main()
{
  for(int i=1;i<=1000;i++){
    minAns[i] = i;
    eat[i] = i;
    K[i] = 0;
    for(int k=1;k<=i;k++){
      if( (i+k)/(k+1) + k < minAns[i]){
        minAns[i] = (i+k)/(k+1) + k;
        K[i] = k;
        eat[i] = (i+k)/(k+1);
      }
    }
  }
  int T, D, p;
  int ansCnt, ans;
  cin >> T;
  for(int z=1;z<=T;z++){
    priority_queue<pair<int, pair<int,int> > > heap;
    ans = 0;
    ansCnt = 0;
    cin >> D;
    for(int i=0;i<D;i++){
      cin >> p;
      ans = max(ans, p);
      heap.push(mp(p, mp(0,p)));
    }
    while(heap.top().y.x != K[heap.top().y.y]){
      int nowK, nowDelta;
      pair<int, pair<int,int> > now = heap.top(); heap.pop();
      ansCnt++;
      nowK = now.y.x + 1;
      nowDelta = (now.y.y + nowK)/(nowK + 1);
      heap.push(mp(nowDelta, mp(nowK, now.y.y)));
      ans = min(ans, ansCnt + heap.top().x);
    }
    printf("Case #%d: %d\n", z, ans);
  }
  return 0;
}
