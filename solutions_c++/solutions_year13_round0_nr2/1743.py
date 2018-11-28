#include<cstdio>
int n,m,a[105][105],T,row[105],col[105],ac;
int mx(int u,int v){
    if (u>v) return u;
    return v;    
}
int main(){
    scanf("%d",&T);
    for (int o=1; o<=T; o++){
        scanf("%d%d",&n,&m);
        for (int i=1; i<=n; i++) row[i]=0;
        for (int i=1; i<=m; i++) col[i]=0;
        for (int i=1; i<=n; i++){
            for (int j=1; j<=m; j++){
                scanf("%d",&a[i][j]);  
                row[i]=mx(row[i],a[i][j]);
                col[j]=mx(col[j],a[i][j]);  
            }    
        }
        ac=1;
        for (int i=1; i<=n; i++){
            for (int j=1; j<=m; j++)
                if (a[i][j]<row[i]&&a[i][j]<col[j]) ac=0;   
        }
        printf("Case #%d: ",o);
        if (ac) printf("YES\n");
        else printf("NO\n");
    }
    return 0;    
}
