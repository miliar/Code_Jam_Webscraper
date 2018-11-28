#include<cstdio>
#include<cstring>
char s[1010];
int T, n;
int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d",&T);
    for(int t=1; t<=T; t++){
        scanf("%d %s", &n, s);
        int ans = 0, cur = 0;
        for(int i=0; i<=n; i++){
            if(cur<i){
                ans += i-cur;
                cur = i;
            }
            cur += s[i]-'0';
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
