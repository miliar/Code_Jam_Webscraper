#include<stdio.h>
#include<string.h>
int a[110][110];
int n,m;
int main(){
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int ca,cc=0;
    int flag,i,j,k,s;
    scanf("%d",&ca);
    while (ca--){
        scanf("%d%d",&n,&m);
        for (i=1;i<=n;i++)
            for (j=1;j<=m;j++) scanf("%d",&a[i][j]);
        flag=1;
        for (i=1;i<=n;i++){
            for (j=1;j<=m;j++){
                s=0;
                for (k=1;k<=m;k++){
                    if (a[i][j]<a[i][k]) {s++;break;}
                }
                for (k=1;k<=n;k++){
                    if (a[i][j]<a[k][j]) {s++;break;}
                }
                if (s==2){flag=0;break;}
            }
        }
        if (flag) printf("Case #%d: YES\n",++cc);
        else printf("Case #%d: NO\n",++cc);
    }
    return 0;
}
