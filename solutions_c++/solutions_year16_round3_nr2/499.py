#include <stdio.h>
int ans[60][60];
long long pow[60];
int main(){
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int tc;
    scanf("%d",&tc);
    pow[0]=1;
    for(int i=1;i<55;i++){
        pow[i]=pow[i-1]*2;
    }
    for(int t=1;t<=tc;t++){
        int n;
        long long m;
        scanf("%d %lld",&n,&m);
        printf("Case #%d: ",t);
        if(m>pow[n-2]){
            printf("IMPOSSIBLE\n");
        }
        else{
            printf("POSSIBLE\n");
            for(int i=1;i<=n-1;i++){
                for(int j=1;j<=n-1;j++){
                    if(i<j){
                        ans[i][j]=1;
                    }
                    else{
                        ans[i][j]=0;
                    }
                }
            }
            for(int i=1;i<=n;i++){
                ans[i][n]=0;
                ans[n][i]=0;
            }
            for(int i=n-3;i>=0;i--){
                if(m>=pow[i]){
                    ans[i+2][n]=1;
                    m-=pow[i];
                }
                else{
                    ans[i+2][n]=0;
                }
            }
            if(m==1){
                ans[1][n]=1;
            }
            for(int i=1;i<=n;i++){
                for(int j=1;j<=n;j++){
                    printf("%d",ans[i][j]);
                }
                printf("\n");
            }
        }
    }
}
