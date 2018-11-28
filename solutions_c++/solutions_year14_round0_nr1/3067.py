#include<cstdio>
#include<cstring>
#include<algorithm>
#define N 6
using namespace std;
int a[N][N],b[N][N];
int t,tt,n,m;

int main(){
  int i,j,k,s;
  freopen("1.txt","r",stdin);
  freopen("2.txt","w",stdout);
  scanf("%d",&t);
  for (tt=1;tt<=t;++tt){
    scanf("%d",&n);
    for (i=1;i<=4;++i)
      for (j=1;j<=4;++j) scanf("%d",&a[i][j]);
    scanf("%d",&m);
    for (i=1;i<=4;++i)
      for (j=1;j<=4;++j) scanf("%d",&b[i][j]);
    s=0;
    for (i=1;i<=4;++i)
      for (j=1;j<=4;++j)
        if (a[n][i]==b[m][j]){
          ++s;
          k=a[n][i];
          break;
        }
    printf("Case #%d: ",tt);
    if (s==1) printf("%d\n",k);
    else if (s>1) puts("Bad magician!");
    else puts("Volunteer cheated!");
  }
  return 0;
}