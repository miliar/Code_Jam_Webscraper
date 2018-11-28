#include<stdio.h>
#include<algorithm>

int main()
{
    freopen("bl.in","r",stdin);
    freopen("bl.out","w",stdout);
    int cases,ii,i,j,k,n,m,w[102][102];
    bool yes,okr,okc;
    scanf("%d",&cases); 
    for(ii=1;ii<=cases;ii++){
        scanf("%d%d",&n,&m);
        for(i=1;i<=n;i++){
            for(j=1;j<=m;j++){
                scanf("%d",&w[i][j]);
            }
        }
        yes=true;
        for(i=1;i<=n;i++){
            for(j=1;j<=m;j++){
                okr=okc=true;
                for(k=1;k<=n;k++){
                    if(w[i][j]<w[k][j])okr=false;
                }
                for(k=1;k<=m;k++){
                    if(w[i][j]<w[i][k])okc=false;
                }
                if(!okr && !okc){
                    //fprintf(stderr,"i=%d j=%d\n",i,j);
                    yes=false;
                }
            }
        }
        
        
        if(yes)printf("Case #%d: YES\n",ii);
        else printf("Case #%d: NO\n",ii);
    }
    
    
    
}
