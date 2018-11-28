#include <stdio.h>
#include <algorithm>

int h[101][101];
bool v[101][101];
bool possible;

bool ff(int i,int j,int n,int m){
     bool wayoutr=true;
     bool wayoutc=true;
     for (int r=1;r<=n;r++)
         if (h[r][j]>h[i][j]) wayoutr=false;
     for (int c=1;c<=m;c++)
         if (h[i][c]>h[i][j]) wayoutc=false;
     return (wayoutr||wayoutc);
}
     
int main(){
    int ntc=0;
    scanf("%d",&ntc);
    for (int tc=1;tc<=ntc;tc++){
        int n,m;
        scanf("%d %d",&n,&m);
        for (int i=1;i<=n;i++)
            for (int j=1;j<=m;j++)
                scanf("%d",&h[i][j]);
        possible=true;
        for (int i=1;i<=n;i++)
            for (int j=1;j<=m;j++)
                if (possible){
                   memset(v,false,sizeof(v));
                   if (!ff(i,j,n,m)) possible=false;
                }
        if (possible) printf("Case #%d: YES\n",tc);
        else printf("Case #%d: NO\n",tc);
    }
    return 0;
}
