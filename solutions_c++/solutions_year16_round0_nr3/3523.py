#include <iostream>
#include <vector>
#include <map>

using namespace std;
typedef long long ll;

vector<ll> ans[40];
map<ll,ll>mp;
const int N = 1000000;            // 范围
ll pr[N], p[N >> 3], lp;            // lp素数表大小，p[]素数表，pr[n]表示n的最小质因子
void gp() {
    for (int i = 2; i < N; i++) {
        if (!pr[i])p[lp++] = pr[i] = i;
        for (int j = 0; j < lp && i * p[j] < N; j++) {
            pr[i * p[j]] = p[j];
            if (i % p[j] == 0)break;
        }
    }
}

bool check(ll num) {
    for (int i = 2; i <= 10; i++) {
        ll x = 0;
        ll tx = num;
        ll t = 1;
        while (tx) {
            x = x + t * (tx % 10);
            tx /= 10;
            t *= i;
        }
        bool ff = false;
        for (int j = 0; p[j] * p[j] < x && j < lp; j++) {
            if (x % p[j] == 0) {
                mp[x] = p[j];
                ff = true;
                break;
            }
        }
        if (ff == false) return false;
    }
    return true;
}

void dfs(ll num, int now, int tot) {
    if (now == tot - 1) {
        num = num * 10 + 1;
        if (check(num)) {
            ans[tot].push_back(num);
            // cout<<tot<<" "<<num<<endl;
        }
        return;
    }
    if (ans[tot].size() >= 500) return;
    dfs(num * 10, now + 1, tot);
    dfs(num * 10 + 1, now + 1, tot);
}

void solve(int x) {
    dfs(1, 1, x);
    //cout << x << " " << ans[x].size() << endl;
}

void init(int n) {
    for (int i = 2; i <= n; i++) {
        solve(i);
    }
}



void solve2(int n, int all) {
    for (int k = 0; k < all; k++) {
        ll num = ans[n][k];
        cout << num;
        for (int i = 2; i <= 10; i++) {
            ll x = 0;
            ll tx = num;
            ll t = 1;
            while (tx) {
                x = x + t * (tx % 10);
                tx /= 10;
                t *= i;
            }
            cout<<" "<<mp[x];
        }
        cout<<endl;

    }
}

int main() {
    gp();
    init(16);
    freopen("/Users/vino/Desktop/C-small-attempt0.in", "r", stdin);
    freopen("/Users/vino/Desktop/C-small-attempt0.out", "w", stdout);
    int T;
    cin >> T;
    int cas = 1;
    while (T--) {
        int n, j;
        cin>>n>>j;
        printf("Case #%d:\n", cas++);
        solve2(n, j);
    }
    return 0;
}