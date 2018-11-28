#include <map>
#include <cmath>
#include <cstdio>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <fstream>
#include <iostream>
#include <algorithm>
#define PB push_back
#define MP make_pair
#define BG begin()
#define ED end()
#define SZ(x) ((int)((x).size()))
#define FF first
#define SS second
#define foreach(i,x) for (__typeof((x).begin()) i=(x).begin();i!=(x).end();i++)
#define FOR(i,l,r) for (int i=(l);i<=(r);i++)
#define ROF(i,r,l) for (int i=(r);i>=(l);i--)
using namespace std;

struct P3 {
  int x,y,z;
  P3(int a=0,int b=0,int c=0) : x(a),y(b),z(c) {}
  bool operator <(const P3 &p) const {return z<p.z;}
};

vector<P3> a;
int f[1005],g[1005];
int task;

//#define LOCAL_TEST

int main() {
#ifdef LOCAL_TEST
  freopen("d.in","r",stdin);
  freopen("d.out","w",stdout);
#endif
  scanf("%d ",&task);
  FOR(tt,1,task) {
    printf("Case #%d: ",tt);
    a.clear();
    int n,m,k;
    bool find=1;
    scanf("%d%d",&n,&m);
    FOR(i,0,m-1) g[i]=1;
    FOR(i,0,n-1) f[i]=1;
    FOR(i,0,n-1) FOR(j,0,m-1) {
      scanf("%d",&k);
      a.PB(P3(i,j,k));
    }
    sort(a.begin(),a.end());
    for (int h=100,r=a.size()-1;h>0;h--) {
      int l=r;
      while (l>=0 && a[l].z==h) {
        int x=a[l].x,y=a[l--].y;
        if (f[x]==0 && g[y]==0) find=0;
      }
      FOR(i,l+1,r) {
        int x=a[i].x,y=a[i].y;
        f[x]=g[y]=0;
      }
      r=l;
    }
    printf(find?"YES\n":"NO\n");
  }
}
