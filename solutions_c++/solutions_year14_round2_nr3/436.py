#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <stack>
using namespace std;

#define MAX 64

int n, m;
char zip[MAX][8];
vector<int> g[MAX];
int a[MAX];
char s[MAX*8], ans[MAX*8];

bool cmp(int i, int j) {
    return strcmp(zip[i], zip[j]) < 0;
}

int check(int *a) {
    stack<int> st;
    st.push(a[0]);
    for (int i = 1; i < n; ++i) {
        int flag = 0;
        while (!flag && !st.empty()) {
            int last = st.top();
            for (int j = 0; j < g[last].size(); ++j) {
                if (g[last][j] == a[i]) {
                    st.push(a[i]);
                    flag = 1;
                    break;
                }
            }
            if (!flag)
                st.pop();
        }
        if (!flag)
            return 0;
    }
    return 1;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        scanf("%d %d", &n, &m);
        int first = 1;
        for (int i = 1; i <= n; ++i) {
            g[i].clear();
            scanf("%s", zip[i]);
            if (strcmp(zip[i], zip[first]) < 0)
                first = i;
        }
        for (int i = 0; i < m; ++i) {
            int u, v;
            scanf("%d %d", &u, &v);
            g[u].push_back(v);
            g[v].push_back(u);
        }
        for (int i = 1; i <= n; ++i)
            sort(g[i].begin(), g[i].end(), cmp);
        for (int i = 0; i < n; ++i)
            a[i] = i+1;
        memset(ans, '9', sizeof(ans));
        do {
            if (check(a)) {
                s[0] = 0;
                for (int i = 0; i < n; ++i)
                    strcat(s, zip[a[i]]);
                if (strcmp(s, ans) < 0)
                    strcpy(ans, s);
            }
        } while (next_permutation(a, a+n));
        printf("Case #%d: %s\n", t, ans);
    }
}
