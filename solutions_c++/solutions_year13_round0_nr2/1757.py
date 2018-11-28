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

#define N 128
int map[N][N];
int maxr[N],maxc[N];

int main() {
  freopen("B-large.in","r",stdin);
  freopen("OUT2","w",stdout);

  int T;
  scanf("%d",&T);
  For(t,1,T) {
    printf("Case #%d: ",t);
    int n,m;
    scanf("%d%d",&n,&m);
    For(i,1,n)
      For(j,1,m)
        scanf("%d",&map[i][j]);

    fill(maxr,maxr+N,-INF);
    fill(maxc,maxc+N,-INF);

    For(i,1,n)
      For(j,1,m) {
        maxr[i]=max(maxr[i],map[i][j]);
        maxc[j]=max(maxc[j],map[i][j]);
      }

    For(i,1,100)
      For(r,1,n)
        For(c,1,m)
          if (map[r][c]==i)
            if (min(maxr[r],maxc[c])>i)
              goto NO;

    puts("YES"); continue;
    NO: puts("NO");
  }
  return 0;
}

