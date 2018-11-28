#include <iostream>

using namespace std;

int n, a[100], b[100], num[100], dp[100];
bool flag[100];

bool check(){
    int now[100] = {0};
    for(int i = n; i >= 1; --i){
        for(int j = n; j > i; --j){
            if(num[i] > num[j]) now[i] = max(now[i], now[j]);
        }
        now[i] ++;
        if(now[i] != b[i]) return false;
    }
    return true;
}
bool dfs(int p){
    if(p == n + 1){
        if(check()){
            for(int i = 1; i <= n; ++i)
                cout << " " << num[i];
            cout << endl;
            return true;
        }
        return false;
    }
    for(int i = a[p] + b[p] - 1; i <= n; ++i){
        if(flag[i]) continue;
        num[p] = i;

        int cur = 0;
        for(int j = 1; j < p; ++j)
            if(num[j] < i) cur = max(cur, dp[j]);
        dp[p] = cur + 1;
        if(dp[p] != a[p]) continue;

        flag[i] = true;
        bool ret = dfs(p + 1);
        if(ret) return true;
        flag[i] = false;
    }
    return false;
}
int main(){
    freopen("in.txt", "r", stdin);
    freopen("Cout.txt", "w", stdout);
    int t, cas = 1;
    for (scanf("%d", &t); t--;){
        printf("Case #%d:", cas++);
        cin >> n;
        memset(flag, false, sizeof(flag));
        memset(dp, 0, sizeof(dp));
        for(int i = 1; i <= n; ++i) cin >> a[i];
        for(int i = 1; i <= n; ++i) cin >> b[i];
        dfs(1);
    }
    return 0;
}
