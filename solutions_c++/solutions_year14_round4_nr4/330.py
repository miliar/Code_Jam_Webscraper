/******************************************************************************\
*                         Author:  Dumbear                                     *
*                         Email:   dumbear[#at]163.com                         *
*                         Website: http://dumbear.com                          *
\******************************************************************************/
#include <algorithm>
#include <bitset>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <typeinfo>
#include <utility>
#include <vector>

using namespace std;

#define output(x) cout << #x << ": " << (x) << endl;

typedef long long LL;
typedef vector<int> VI;
typedef vector<long long> VL;
typedef vector<double> VD;
typedef vector<string> VS;

class trie {
public:
    struct node {
        static const int max_n = 26;
        int ch[max_n], fail;
        node() {
            fill(ch, ch + max_n, -1);
        }
    };
    vector<node> nodes;
    void clear() {
        nodes.clear();
        nodes.push_back(node());
    }
    void insert(const char* word) {
        int p = 0;
        for (int i = 0; word[i] != '\0'; ++i) {
            int l = word[i] - 'A';
            if (nodes[p].ch[l] == -1) {
                p = nodes[p].ch[l] = nodes.size();
                nodes.push_back(node());
            } else
                p = nodes[p].ch[l];
        }
    }
};

int t, n, m, ans, cnt;
string s[16];
trie tr[8];

void check() {
    int res = 0;
    for (int i = 0; i < n; ++i) {
        if (tr[i].nodes.size() == 1)
            return;
        res += tr[i].nodes.size();
    }
    if (res > ans) {
        ans = res;
        cnt = 1;
    } else if (res == ans)
        ++cnt;
}

void dfs(int d) {
    if (d == m) {
        check();
        return;
    }
    // printf("-- %d\n", d);
    for (int i = 0; i < n; ++i) {
        trie tmp = tr[i];
        tr[i].insert(s[d].c_str());
        dfs(d + 1);
        tr[i] = tmp;
    }
}

void solve() {
    scanf("%d%d", &m, &n);
    for (int i = 0; i < m; ++i)
        cin >> s[i];
    for (int i = 0; i < n; ++i)
        tr[i].clear();
    ans = 0;
    dfs(0);
    printf("Case #%d: %d %d\n", ++t, ans, cnt);
}

int main() {
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
        solve();
    return 0;
}
