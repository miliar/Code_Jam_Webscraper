#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <stack>
#include <bitset>
#define INF 0x3f3f3f3f
#define eps 1e-8
#define FI first
#define SE second
using namespace std;
typedef long long LL;
char s[25][20005];
map <string, int> mp;
vector <int> G[30];
int n, label;
int v[5005];

int solve(int st) {
    st <<= 2;
    st |= 2;
    memset(v, 0, sizeof(v));
    for(int i = 0; i < n; ++i) {
        int x = (st >> i) & 1;
        for(int j = 0; j < (int)G[i].size(); ++j) {
            if(x) v[G[i][j]] |= 2;
            else v[G[i][j]] |= 1;
        }
    }
    int res = 0;
    for(int i = 0; i < label; ++i) res += v[i] == 3;
    return res;
}

int add(string t) {
    map <string, int>::iterator it = mp.find(t);
    if(it == mp.end()) {
        mp[t] = label;
        return label++;
    }
    return it->SE;
}

int main() {
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int ca = 1; ca <= T; ++ca) {
        scanf("%d", &n);
        gets(s[0]);
        for(int i = 0; i < n; ++i) gets(s[i]);
        for(int i = 0; i < n; ++i) G[i].clear();
        mp.clear();
        label = 0;
        for(int i = 0; i < n; ++i) {
            int len = strlen(s[i]);
            string t = "";
            for(int j = 0; j <= len; ++j) {
                if(s[i][j] == ' ' || j == len) {
                    int id = add(t);
                    G[i].push_back(id);
                    t.clear();
                }
                else t += s[i][j];
            }
        }
        int ans = INF;
        int m = n - 2;
        for(int i = 0; i < (1 << m); ++i) {
            ans = min(ans, solve(i));
        }
        printf("Case #%d: %d\n", ca, ans);
    }
    return 0;
}
