#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int t, n, m, a, ans;
int f[701];
int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &t);
    for(int ct=1; ct<=t; ct++){
        scanf("%d %d", &n, &m);
        memset(f,0,sizeof(f));
        for(int i=0; i<n; i++){
            scanf("%d", &a);
            f[a]++;
        }
        ans=0;
        for(int i=1; i<=700; i++){
            while(f[i]){
                f[i]--;
                ans++;
                for(int j=m-i; j>=i; j--){
                    if(f[j]){
                        f[j]--;
                        break;
                    }
                }
            }
        }
        printf("Case #%d: %d\n", ct, ans);
    }
    return 0;
}
