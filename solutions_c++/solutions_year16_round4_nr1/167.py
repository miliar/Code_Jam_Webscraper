#include <bits/stdc++.h>
using namespace std;



typedef double DB;
typedef long long LL;

const int N = 1e5 + 7;

int r, p, s;
vector<int> vec;

string dfs(int cur, int winner, int n) {
    if (cur == n) {
        if (winner == 0) {r++; return "R";}
        else if (winner == 1) {p++; return "P";}
        else if (winner == 2) {s++; return "S";}
    }

    string a = dfs(cur + 1, winner, n), b;
    if (winner == 0) b = dfs(cur + 1, 2, n);
    if (winner == 1) b = dfs(cur + 1, 0, n);
    if (winner == 2) b = dfs(cur + 1, 1, n);
    return min(a + b, b + a);
}

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int CAS, n, R, P, S;
    scanf("%d", &CAS);
    for (int cas = 1; cas <= CAS; cas++) {
        scanf("%d%d%d%d", &n, &R, &P, &S);
        int found = 0;
        string ans;
        for (int winner = 0; winner < 3; winner++) {
            r = p = s = 0;
            ans = dfs(0, winner, n);
            if (r == R && p == P && s == S) {
                found = 1;
                break;
            }
        }
        printf("Case #%d: ", cas);
        if (found) {
            cout << ans << endl;
        } else puts("IMPOSSIBLE");
    }
}
