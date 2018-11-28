
#include<iostream>
#include<cstdio>
#include<string.h>
#include<string>
#include<math.h>
#include<algorithm>
using namespace std;
#define maxn 1000009

int a[109];
int f[109][109];

void init(){
    memset(a,0,sizeof(a));
    memset(f,-1,sizeof(f));
}

int main(){
    int T;
    scanf("%d",&T);
    int x,n;
    for(int cas=1;cas<=T;cas++){
        init();
        scanf("%d %d",&x,&n);
        for(int i=1;i<=n;i++) scanf("%d",&a[i]);
        sort(a+1,a+n+1);
        f[0][0] = x;
        for(int i=1;i<=n;i++){
            if(f[0][i-1]<1000009)
                f[0][i] = f[0][i-1]*2-1;
            else f[0][i] = f[0][i-1];
        }
        for(int i=1;i<=n;i++){
            for(int j=0;j<n;j++){
                if(j){
                    if(f[i][j-1]<1000009)
                        f[i][j] = max(f[i][j],f[i][j-1]*2-1);
                    else f[i][j] = f[i][j-1];
                }
                if(f[i-1][j]>a[i]){
                    if(f[i-1][j]<1000009)
                        f[i][j] = max(f[i][j],f[i-1][j]+a[i]);
                    else f[i][j] = f[i-1][j];
                }
                else f[i][j+1] = max(f[i][j+1],f[i-1][j]);
            }
        }
        int ans = -1;
        for(int i=0;i<=n;i++){
            if(f[n][i]!=-1){
                ans = i;
                break;
            }
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
