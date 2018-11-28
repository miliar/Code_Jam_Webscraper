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

const long long INF64 = (long long) 1e18;

ll N;
ll sum[1000100], arr[1000100];

ll eva(int L, int R){
  if(L > R) return -INF64;
  ll sumL = 0, sumM, sumR, sumMax;
  if(L) sumL += sum[L-1];
  sumM = sum[R] - sumL;
  sumR = sum[N-1] - sumL - sumM;
  sumMax = max(sumL, max(sumM, sumR));
  //printf("L %d R %d: sumL(%lld, %lld, %lld) sum %lld ans %lld\n", L, R, sumL, sumM, sumR, sumMax, sum[N-1] - sumMax);
  return sum[N-1] - sumMax;
}

int main()
{
freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
  ll p, q, r, s;
  int T;
  int L, R;
  ll ans;
  cin >> T;
  for(int z=1;z<=T;z++){
    ans = 0;
    cin >> N >> p >> q >> r >> s;
    for(ll i=0; i<N; i++){
      arr[i] = (i*p+q)%r + s;
      //printf("%lld ", arr[i]);
      sum[i] = arr[i];
      if(i) sum[i] += sum[i-1];
    }
    //puts("");
    L = 0;
    for(R = 0;R < N;R++){
      while(eva(L, R) < eva(L+1, R)) L++;
      ans = max(ans, eva(L, R));
    }
    printf("Case #%d: %.10lf\n", z, double(ans)/double(sum[N-1]));
  }
  return 0;
}
