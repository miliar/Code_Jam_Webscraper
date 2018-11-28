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

char s[25];
long double P[(1<<20)+100], D[(1<<20)+100];

int main()
{     
  int tst, cnt, len, mask, i, j, p;
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  scanf("%d ", &tst);
  for (cnt=1; cnt<=tst; cnt++)
  {
    cerr<<cnt<<endl;
    gets(s), len=strlen(s);
    memset(D,0,sizeof(D)), mask=0, memset(P,0,sizeof(P));
    for (i=0; i<len; i++)
      if (s[i]=='X')
        mask+=(1<<i);
    P[mask]=1.0;
    while (mask<(1<<len)-1)
    {
      for (i=0; i<len; i++)
      {
        j=i, p=len;
        while (mask&(1<<j))
          j++, j%=len, p--;
        P[mask+(1<<j)]+=P[mask]/len, D[mask+(1<<j)]+=(P[mask]*p+D[mask])/len;
      }
      mask++;
    }
    printf("Case #%d: %.12lf\n", cnt, (double)D[(1<<len)-1]);
  }
  return 0;
}

