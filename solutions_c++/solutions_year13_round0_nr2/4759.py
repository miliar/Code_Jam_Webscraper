//#define FILE_IO

#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>

using namespace std;

typedef long long ll;
#ifdef unix
#define LLD "%lld"
#else
#define LLD "%I64d"
#endif 

const int maxn=110;
int a[maxn][maxn],r[maxn],c[maxn];

int main(){
#ifdef FILE_IO
  freopen("t.in","r",stdin);
  freopen("t.out","w",stdout);
#endif
  int T,Test=0;
  int n,m,i,j;
  for(scanf("%d",&T);T--;){
    scanf("%d%d",&n,&m);
    memset(r,0,sizeof(r));
    memset(c,0,sizeof(c));
    for(i=0;i<n;++i)
      for(j=0;j<m;++j){
        scanf("%d",&a[i][j]);
        r[i]=max(r[i],a[i][j]);
        c[j]=max(c[j],a[i][j]);
      }
    printf("Case #%d: ",++Test);
    for(i=0;i<n;++i)
      for(j=0;j<m;++j)
        if(a[i][j]<r[i]&&a[i][j]<c[j])
          goto Fail;
    puts("YES");
    continue;
    Fail:
    puts("NO");
  }
  return 0;
}
