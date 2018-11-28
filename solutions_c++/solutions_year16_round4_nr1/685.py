#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
using namespace std;

typedef long long LL;
#define CLR(a,b) memset(a,b,sizeof(a))
const int N = (1<<10)+5;
int n;
string dp[13][N][N][3];
typedef pair<pair<int,int>, int> pp;

int enermy(int i) {
    if (i == 2) {
        return 0;
    }
    return i + 1;
}
int slaver(int i) {
    if (i == 0) {
        return 2;
    }
    return i -1;
}
void up(int n, int s, int p, int e, string ss) {
    if (dp[n][s][p][e].size()) {
        dp[n][s][p][e] = min(dp[n][s][p][e], ss);
    } else {
        dp[n][s][p][e] = ss;
    }
}
string ans[13][N][N];
void solve()
{
    dp[0][1][0][0] = "P";
    dp[0][0][1][1] = "S";
    dp[0][0][0][2] = "R";
    vector<pp> goods;
    goods.push_back(make_pair(make_pair(1, 0), 0));
    goods.push_back(make_pair(make_pair(0, 1), 1));
    goods.push_back(make_pair(make_pair(0, 0), 2));
    for (int n = 1; n <= 12; ++n) {
        vector<pp> nxt_goods;
        for (auto& good : goods) {
            int p = good.first.first, s = good.first.second, e = good.second;
            if (ans[n-1][p][s].size()) {
                ans[n-1][p][s] = min(ans[n-1][p][s], dp[n-1][p][s][e]);
            } else {
                ans[n-1][p][s] = dp[n-1][p][s][e];
            }
        }
        for (int i = 0; i < goods.size(); ++i) {
            for (int j = 0; j < goods.size(); ++j) {
                int s1 = goods[i].first.first, p1 = goods[i].first.second, e1 = goods[i].second;
                int s2 = goods[j].first.first, p2 = goods[j].first.second, e2 = goods[j].second;
                if (e1 == e2) continue;
                int e = (e1 == enermy(e2)) ? e1 : e2;
                int s = s1 + s2, p = p1 + p2;
                nxt_goods.push_back(make_pair(make_pair(s, p), e));
                up(n,s,p,e,dp[n-1][s1][p1][e1] + dp[n-1][s2][p2][e2]);
            }
        }
        goods = nxt_goods;
        sort(goods.begin(), goods.end());
        goods.erase(unique(goods.begin(), goods.end()), goods.end());
    }
}
int m, r, p, s;
int main()
{
    solve();
    freopen("/Users/lizhen/Documents/Project/Cpp/cpp/cpp/input.txt", "r", stdin);
    freopen("/Users/lizhen/Documents/Project/Cpp/cpp/cpp/output.txt", "w", stdout);
    int T, cas = 0;
    scanf("%d", &T);
    while (T--) {
        printf("Case #%d: ", ++cas);
        scanf("%d%d%d%d", &n,&r,&p,&s);
        if (!ans[n][r][p].size()) {
            puts("IMPOSSIBLE");
        } else {
            printf("%s\n", ans[n][p][s].c_str());
        }
    }
    return 0;
}