#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <iostream>
#include <map>

using namespace std;

map<pair<int, string>, string> mp;

string dfs(int cur, string op) {
    if (cur == 0) {
        return op;
    }
    string po = "";
    if (mp.find(make_pair(cur, op)) != mp.end())
        return mp[make_pair(cur, op)];
    if (op == "R") {
        po = "S";
    } else if (op == "S") {
        po = "P";
    } else {
        po = "R";
    }
    return mp[make_pair(cur, op)] = min(dfs(cur-1, op)+dfs(cur-1,po), dfs(cur-1,po)+dfs(cur-1,op));
}
int n, R, P, S;
int find(int cur, int r, int p, int s) {
    if (cur == n)
        return r == R && p == P && s == S;
    int nR = r + p;
    int nP = p + s;
    int nS = s + r;
    return find(cur + 1, nR, nP, nS);
}

void work() {
    scanf("%d%d%d%d", &n, &R, &P, &S);
    if (find(0, 1, 0, 0)) {
        cout << dfs(n, "R") << endl;
    } else if (find(0, 0, 1, 0)) {
        cout << dfs(n, "P") << endl;
    } else if (find(0, 0, 0, 1)) {
        cout << dfs(n, "S") << endl;
    } else {
        cout << "IMPOSSIBLE" << endl;
    }
    return ;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        printf("Case #%d: ", cas);
        work();
    }
    return 0;
}
