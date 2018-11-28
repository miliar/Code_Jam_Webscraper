#include<stdio.h>
#include<string.h>
int s[102][102],L1[102],L2[102];
int main(){
    freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
    int t,n,m,i,j,k,big,check;
    while(scanf("%d",&t)!=EOF){
        for(k=1;k<=t;k++){
            printf("Case #%d: ",k);
            check=0;
            scanf("%d%d",&n,&m);
            for(i=0;i<n;i++){
                big=0;
                for(j=0;j<m;j++){
                    scanf("%d",&s[i][j]);
                    if(s[i][j]>big) big=s[i][j];
                }
                L1[i]=big;
            }
            for(i=0;i<m;i++){
                big=0;
                for(j=0;j<n;j++){
                    if(s[j][i]>big) big=s[j][i];
                }
                L2[i]=big;
            }
            for(i=0;i<n;i++){
                for(j=0;j<m;j++){
                    if(s[i][j]!=L1[i] && s[i][j]!=L2[j]){
                        check=1;
                        goto go;
                    }
                }
            }
            go:
            if(check)
            puts("NO");
            else
            puts("YES");
        }
    }
}
