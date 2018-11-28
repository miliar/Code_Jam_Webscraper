#include<cstdio>
int nm[100][100];
int yes[100][100];
int main() {
  int n;scanf("%d", &n);
  for(int cas=1;cas<=n;cas++) {
    int n, m; scanf("%d %d",&n,&m);
    for(int i=0;i<n;i++)
      for(int j=0;j<m;j++)
      { nm[i][j]=0; yes[i][j]=0;}
    for(int i=0;i<n;i++)
      for(int j=0;j<m;j++)
        scanf("%d", &nm[i][j]);

    for(int i=0;i<n;i++) {
      int peak=-1;
      for(int j=0;j<m;j++)
        if(nm[i][j]>=peak)
          peak=nm[i][j];
      for(int j=0;j<m;j++)
        if(nm[i][j]==peak)
          yes[i][j]=1;
    }
    for(int i=0;i<m;i++) {
      int peak=-1;
      for(int j=0;j<n;j++)
        if(nm[j][i]>=peak)
          peak=nm[j][i];
      for(int j=0;j<n;j++)
        if(nm[j][i]==peak)
          yes[j][i]=1;
    }
    bool found=true;
    for(int i=0;i<n;i++) {
      for(int j=0;j<m;j++)
        if(yes[i][j]==0) {
          printf("Case #%d: NO\n", cas);
          found=false; break;
        }
      if(!found)break;
    }
    if(found)
      printf("Case #%d: YES\n", cas);
  }
  return 0;
}
