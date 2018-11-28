#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <unordered_map>

using namespace std;

unordered_map<string, int> h1, h2;
int n, ans, tol;
string s1[20], s2[20];

void dfs(int c, int cnt, int tmp){
    if (c == n){
        if (cnt != tol) return;
        //cout << tmp << endl;
        if (n - tmp > ans) ans = n - tmp;
        return;
    }
    dfs(c + 1, cnt, tmp);
    int x1 = h1[s1[c]], x2 = h2[s2[c]];
    h1[s1[c]] = 0;
    h2[s2[c]] = 0;
    dfs(c + 1, cnt + x1 + x2, tmp + 1);
    h1[s1[c]] = x1;
    h2[s2[c]] = x2;
}

int main(){
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; ++ cas){
        h1.clear();
        h2.clear();
        ans = 0;
        tol = 0;
        cin >> n;
        for (int i = 0; i < n; ++ i){
            cin >> s1[i] >> s2[i];
            if (h1.count(s1[i]) == 0) tol ++;
            if (h2.count(s2[i]) == 0) tol ++;
            h1[s1[i]] = 1;
            h2[s2[i]] = 1;
        }
        //cout << tol << endl;
        dfs(0, 0, 0);
        printf("Case #%d: %d\n", cas, ans);
    }
    fclose(stdin);
    fclose(stdout);

    return 0;
}
