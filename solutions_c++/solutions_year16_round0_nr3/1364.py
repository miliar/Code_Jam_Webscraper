#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int n, k;
int ans[100];
void dfs(int len){
    if (k == 0) return;
    if (len >= n){
       // puts("here");
        ans[n] = 1;
        int cnt = 0;
        for (int i = 2; i <= n; i += 2) if (ans[i] == 1) cnt ++;

        if (n & 1) cnt --;
        cnt--;
        //printf("%d\n", cnt);
        for (int i = 3; i < n; i += 2){
            if (cnt > 0){
                ans[i] = 1;
                cnt --;
            }
        }
        k--;
        for (int i = n; i >= 1; -- i) printf("%d", ans[i]);
        for (int i = 2; i <= 10; ++ i) printf(" %d", i + 1);
        puts("");
        for (int i = 3; i < n; i += 2){
            ans[i] = 0;
        }
        return;
    }
    for (int i = 0; i < 2; ++ i){
        ans[len] = i;
        dfs(len + 2);
    }
}

int main(){
    //freopen("in.txt", "r", stdin);
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t; scanf("%d", &t);
    while (t--){
        static int ca = 0;
        printf("Case #%d:\n", ++ ca);
        scanf("%d %d", &n, &k);
        ans[1] = 1;
        dfs(2);
    }
}
