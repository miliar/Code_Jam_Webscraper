#include <bits/stdc++.h>
using namespace std;



typedef double DB;
typedef long long LL;

const int N = 1e5 + 7;

int n, v[10], u[10], found;
char a[10][10];

void dfs(int x) {
    if (x == n || found) return;
    for (int i = 0; i < n; i++) if (!v[i]) {
        int flag = 0;
        v[i] = 1;
        for (int j = 0; j < n; j++) if (!u[j] && a[i][j] == '1') {
            flag = 1;
            u[j] = 1;
            dfs(x + 1);
            u[j] = 0;
        }
        v[i] = 0;
        if (!flag) found = 1;
    }

}

bool check() {
    found = 0;
    dfs(0);
    return !found;
}

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int CAS;
    scanf("%d", &CAS);
    for (int cas = 1; cas <= CAS; cas++) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
            scanf("%s", a[i]);
        vector<pair<int,int> > vec;
        for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
        if (a[i][j] == '0') vec.push_back(make_pair(i, j));
        int ans = 1e9 + 7;
        for (int i = 0; i < (1 << vec.size()); i++) {
            int tmp = 0;
            for (int j = 0; j < vec.size(); j++)
            if (i >> j & 1){
                a[vec[j].first][vec[j].second] = '1';
                tmp++;
            }
            if (check()) ans = min(ans, tmp);

            for (int j = 0; j < vec.size(); j++)
            if (i >> j & 1) a[vec[j].first][vec[j].second] = '0';
        }
        printf("Case #%d: %d\n", cas, ans);
    }
}
