#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int v[20000],p[50][50];
int main(void){
    int t;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++){
        int e,r,n;
        scanf("%d%d%d",&e,&r,&n);
        for(int i=0;i<n;i++)
            scanf("%d",&v[i]);
        memset(p,0,sizeof(p));
        for(int i=0;i<n;i++){
            for(int j=0;j<=e;j++){
                for(int k=0;k<=j;k++){
                    int z = min(e, j-k+r);
                    if(p[i+1][z] < p[i][j]+k*v[i])
                        p[i+1][z] = p[i][j]+k*v[i];
                }
            }
        }
        int ans=0;
        for(int i=0;i<=e;i++)
            ans = max(ans, p[n][i]);
        
        printf("Case #%d: %d\n", tt, ans);
    }
    return 0;
}

