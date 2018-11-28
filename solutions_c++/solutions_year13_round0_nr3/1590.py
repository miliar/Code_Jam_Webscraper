#include <iostream>
#include <iomanip>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <bitset>
using namespace std;
#define INF 0x7fffffff
#define LL long long
#define LD long double
#define PII pair<int,int>
#define x first
#define y second
#define pb push_back
#define sz(a) int(a.size())
#define all(a) a.begin(),a.end()
#define For(i,a,b) for(int i=a;i<=b;i++)
#define dbg(x) cerr<<__LINE__<<": "<<#x<<" = "<<(x)<<endl

inline int palind(LL x) {
  static char st[30];
  sprintf(st+1,"%lld",x);
  int l=strlen(st+1);
  For(i,1,l) if (st[i]!=st[l-i+1]) return 0;
  return 1;
}

inline int check(LL x) {
  LL sx=sqrt(x);
  if (sx*sx!=x) return 0;
  if (!palind(x)) return 0;
  if (!palind(sx)) return 0;
  return 1;
}

#define N 10000010
int is[N];

LL calc(LL a,LL b) {
  LL i=sqrt(a),res=0;
  for (;i*i<=b;i++)
    if (i*i>=a) res+=is[i];
  return res;
}

int main() {
  freopen("C-large-1.in","r",stdin);
  freopen("OUT2","w",stdout);

  for (LL i=0;i<N;i++) {
    is[i]=check(i*i);
  }

  int T;
  scanf("%d",&T);
  For(t,1,T) {
    printf("Case #%d: ",t);

    LL a,b;
    cin>>a>>b;
    cout<<calc(a,b)<<endl;;
  }
  return 0;
}

