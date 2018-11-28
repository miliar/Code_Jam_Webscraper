#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int d[10000], z[10000];
vector<int> edge[10000];
int q[10000];
int a[10000];
int b[10000];
int n;
int ans[10000];
int add(int a, int b) {
    d[b]++;
    edge[a].push_back(b);
    return 0;
}

int work() {
    int k = 0, tmp = 0;
    for (int i = 1; i <= n; ++i)
    if (d[i] == 0) z[++k] = i;
    for (int i = 1; i <= n; ++i) {
        for (int j = i; j <= k; ++j)
            if (z[j] < z[i]) swap(z[j], z[i]);
        ans[z[i]] = i;
        for (int j = 0; j < edge[z[i]].size(); ++j) {
            tmp = edge[z[i]][j];
            --d[tmp];
            if (d[tmp] == 0) z[++k] = tmp;
        }
    }
    return 0;
}

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int tt;
    scanf("%d", &tt);
    for (int t = 1; t <= tt; ++t) {
        scanf("%d", &n);
        for (int i = 1; i <= n; ++i){
            ans[i] = 0;
            edge[i].clear();
        }
        for (int i = 1; i <= n; ++i) scanf("%d", &a[i]);
        for (int i = 1; i <= n; ++i) scanf("%d", &b[i]);
        for (int i = 1; i <= n; ++i) q[i] = 0;
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= a[i] - 1; ++j)
            if (q[j] != 0) add(q[j], i);
            for (int j = a[i]; j <= n; ++j)
            if (q[j] != 0) add(i, q[j]);
            q[a[i]] = i;
        }
        for (int i = 1; i <= n; ++i) q[i] = 0;
        for (int i = n; i > 0; --i) {
            for (int j = 1; j <= b[i] - 1; ++j)
            if (q[j]) add(q[j], i);
            for (int j = b[i]; j <= b[i]; ++j)
            if (q[j]) add(i, q[j]);
            q[b[i]] = i;
        }
        work();
        for (int i = 1; i <= n; ++i) {
            int m = 1;
            for (int j = 1; j <= i - 1; ++j)
            if (ans[i] > ans[j]) m = max(m, a[j] + 1);
            if (a[i] != m) {
                cout << "wrong in "  << i << endl;
            } 
        }
        for (int i = n; i > 0; --i) {
            int m = 1;
            for (int j = n; j > i; --j)
            if (ans[j] < ans[i]) m = max(m, b[j] + 1);
            if (b[i] != m) {
                cout << "wrong in " << i << endl;
            }
        }
        printf("Case #%d:", t);
        for (int i = 1; i <= n; ++i) printf(" %d", ans[i]);
        printf("\n");
    }
    return 0;
}
