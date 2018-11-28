#include <stdio.h>
#include <string.h>

#define min(x,y) ((x)<(y)?(x):(y))

#define N 1000
#define MAX 1000000

int T,n;
char s[N+1];
int d[2][N][N];

int main() {
  int TT;
  int i,j,k,l,m,x;
  scanf("%d",&T);
  for(TT=1;TT<=T;TT++){
    scanf("%s",s);
    n=strlen(s);
    for(i=0;i<n;i++){
      if(s[i]=='+') {
        d[0][i][i]=0;
        d[1][i][i]=1;
      }else{
        d[0][i][i]=1;
        d[1][i][i]=0;
      }
    }
    for(k=1;k<n;k++){
      for(i=0,j=k;j<n;i++,j++){
        for(m=0;m<2;m++){
          d[m][i][j]=MAX;
          for(l=i+1;l<=j;l++){
            x=d[m][i][l-1]+d[m][l][j];
            if(d[m][l][j])x+=2;
            d[m][i][j]=min(d[m][i][j],x);
          }
        }
        d[0][i][j]=min(d[0][i][j],d[1][i][j]+1);
        d[1][i][j]=min(d[1][i][j],d[0][i][j]+1);
      }
    }
    printf("Case #%d: %d\n",TT,d[0][0][n-1]);
  }
}
