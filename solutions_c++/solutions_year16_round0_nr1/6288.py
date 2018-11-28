#include<stdio.h>
typedef long long ll;
bool vis[15];
void mark(ll x, int &k){
    while(x){
        if(!vis[x%10]) vis[x%10] = 1, k -= 1;
        x /= 10;
    }
}
int main(){
    int T, ca = 1;
    scanf("%d", &T);
    while(T--){
        ll n;
        int k = 10, flag = 0;
        for(int i = 0; i <= 10; ++i) vis[i] = 0;
        scanf("%lld", &n);
        mark(n, k);
        for(int i = 1; i <= 1e6; ++i){
            mark(i*n, k);
            if(!k) { flag = i; break; }
        }
        if(flag) printf("Case #%d: %lld\n", ca++, n*flag);
        else printf("Case #%d: INSOMNIA\n", ca++);
    }
}
