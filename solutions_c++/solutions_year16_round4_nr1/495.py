#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

int n, r, p, s;
string ch[3] = {"R", "P", "S"};
string ans;

string dfs(int c, int x){
    string ret;
    if (c == n){
        ret = "" + ch[x];
        return ret;
    }
    string p = dfs(c + 1, x);
    string q = dfs(c + 1, (x + 3 - 1) % 3);
    if ((p + q) < (q + p)) return p + q;
                    else   return q + p;
}

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; ++ cas){
        scanf("%d%d%d%d", &n, &r, &p, &s);
        ans = "";
        for (int i = 0; i < 3; ++ i){
            int tr = 0, tp = 0, ts = 0;
            string tmp = dfs(0, i);
            for (int j = 0; j < (int)tmp.size(); ++ j){
                if (tmp[j] == 'P') tp ++;
                if (tmp[j] == 'R') tr ++;
                if (tmp[j] == 'S') ts ++;
            }
            if (tp != p || tr != r || ts != s) continue;
            if (ans == "" || tmp < ans) ans = tmp;
        }
        if (ans == "")
            printf("Case #%d: IMPOSSIBLE\n", cas);
        else{
            printf("Case #%d: ", cas);
            cout << ans << endl;
        }
    }
    fclose(stdin);
    fclose(stdout);

    return 0;
}
