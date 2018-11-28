#include <stdio.h>
int grid[100][100];
int main(){
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int t,i,j,k,cc,m,n;
    for(cc=1,scanf("%d",&t);cc<=t;++cc){
        scanf("%d%d",&m,&n);
        for(i=0;i<m;++i) for(j=0;j<n;++j) scanf("%d",&grid[i][j]);
        for(i=0;i<m;++i){
            for(j=0;j<n;++j){
                bool row=true,col=true;
                for(k=0;k<n;++k) if(grid[i][k]>grid[i][j]) {row=false;break;}
                for(k=0;k<m;++k) if(grid[k][j]>grid[i][j]) {col=false;break;}
                if(!row&&!col) goto hell;
            }
        }
        hell:
        printf("Case #%d: ",cc);
        if(i==m) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}

