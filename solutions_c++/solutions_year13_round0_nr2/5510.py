#include <stdio.h>

int main(){
  freopen("B-large.in","rt",stdin);
  freopen("B-large.out","wt",stdout);
  int n,m,i,j,k;
  int nTest;
  int field[110][110];
  bool noAns;
  scanf("%d",&nTest);
  for(int t = 1;t<=nTest;t++){
    noAns = false;
    scanf("%d %d",&n,&m);
    for(int i = 0;i<n;i++)
      for(int j=0;j<m;j++)
        scanf("%d",&field[i][j]);
    for(i=0;i<n;i++){
      for(j=0;j<m;j++){
        for(k =0;k<n;k++)
          if(field[k][j]>field[i][j])
            break;
        if(k<n){
          noAns = true;
        }else
          continue;
        for(k =0;k<m;k++)
          if(field[i][k]>field[i][j])
            break;
        if(k<m){
          if(noAns)
            break;
          noAns = true;
        }else
          noAns = false;
      }
      if(noAns)
        break;
    }
    if(noAns)
      printf("Case #%d: NO\n",t);
    else
      printf("Case #%d: YES\n",t);
  }

}
