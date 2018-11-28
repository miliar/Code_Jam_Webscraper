#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <ctime>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <list>
#include <set>
#include <map>
#include <sstream>
#include <iostream>

#define pb push_back
#define mp make_pair
#define TASKNAME ""

#ifdef LOCAL
#define eprintf(...) fprintf(stderr,__VA_ARGS__)
#else
#define eprintf(...)
#endif

#define TIMESTAMP(x) eprintf("[" #x "] Time = %.3lfs\n",clock()*1.0/CLOCKS_PER_SEC)

#ifdef linux
#define LLD "%lld"
#else
#define LLD "%I64d"
#endif

#define sz(x) ((int)(x).size())
#define strstr strstr_wregthrtu

using namespace std;

typedef long double ld;
typedef long long ll;
typedef vector<ll> vll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef pair<int, int> pii;

const int inf = 1e9;
const double eps = 1e-9;
const double INF = inf;
const double EPS = eps;

ll A[40];

int main()
{     
  int tst, cnt, i, j, n;
  ll b;
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  scanf("%d", &tst);
  for (cnt=1; cnt<=tst; cnt++)
  {
    cerr<<"cnt="<<cnt<<endl;
    cin>>b>>n;
    memset(A,0,sizeof(A));
    for (i=0; i<n; i++)
      cin>>A[i];
    sort(A,A+37);
    long double res=0.0;
    //cerr<<A[0]<<" "<<A[35]<<" "<<A[34]<<" "<<A[33]<<" "<<A[32]<<endl;
    for (i=1; i<37; i++)
    {
      ll s=0;
      for (j=0; j<i; j++)
        s+=A[j];
      ll mb=A[i-1];
      ll Mb=A[36];

      if (mb*i>b+s || mb>=Mb)
        continue;

      while (Mb-mb>1)
      {
        ll mid=(mb+Mb)/2;
        ll ns=0, ns2=0;
        for (j=0; j<i; j++)
          ns+=mid-A[j];
        for (j=i; j<37; j++)
          ns2+=max(0ll,mid+1-A[j]);

        (ns+ns2<=b)?(mb=mid):(Mb=mid);
      }                          
      ll ns=0, ns2=0;
      for (j=0; j<i; j++)
        ns+=mb-A[j];// cerr<<mb-A[j]<<endl;
      for (j=i; j<37; j++)
        ns2+=max(0ll,mb+1-A[j]);
      //ns-=s;
      //cerr<<i<<" "<<ns<<" "<<mb<<"    "<<s<<"   "<<ns2<<"    "<<ns*36.0/i-ns-ns2<<endl;
      res=max(res,(ld)(ns*36.0/i-ns-ns2));
    }
    printf("Case #%d: %.12lf\n", cnt, (double)res);
  }
  return 0;
}

