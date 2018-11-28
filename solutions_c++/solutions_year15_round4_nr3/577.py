#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <queue>

#define LL long long
#define mp(x, y) make_pair(x, y)
#define pb(x) push_back(x)
#define PII pair<int, int>
#define PID pair<int, double>

using namespace std;

int n, m, T, cnt, ans, sign;
char str[20000];
int type[222];
map<string, int> M;
set<int> E, F;
vector<int> token[222];
int H[10000000];

void dfs(int x) {
    if (x == n) {
        /*
        E.clear(); F.clear();
        for (int i = 0; i < n; ++i) {
            for (int w = 0; w < (int)token[i].size(); ++w) {
                if (type[i] == 0) E.insert(token[i][w]);
                else F.insert(token[i][w]);
            }
        }
        cnt = 0;
        for (auto &e : E) {
            if (F.find(e) != F.end()) ++cnt;
        }*/
        ++sign;
        for (int i = 0; i < n; ++i) {
            if (type[i] == 1) continue;
            for (int w = 0; w < (int)token[i].size(); ++w)
                H[token[i][w]] = sign;
        }
        cnt = 0;
        for (int i = 0; i < n; ++i) {
            if (type[i] == 0) continue;
            for (int w = 0; w < (int)token[i].size(); ++w)
                if (H[token[i][w]] == sign) {
                    ++cnt;
                    H[token[i][w]] = 0;
                }
        }
        if (cnt < ans) ans = cnt;
    } else {
        type[x] = 0;
        dfs(x + 1);
        type[x] = 1;
        dfs(x + 1);
    }
}

int main(){
    scanf("%d", &T);
    sign = 100;
    type[0] = 0; type[1] = 1;
    for (int Tno = 1; Tno <= T; ++Tno) {
        scanf("%d\n", &n);
        cnt = 0; ans = 1e9;
        M.clear();
        for (int i = 0; i < n; ++i) {
            fgets(str, 19999, stdin);
            int len = strlen(str);
            string w = "";
            token[i].clear();
            for (int c = 0; c <= len; ++c) {
                if (isspace(str[c])) {
                    if (w == "") continue;
                    if (M.find(w) == M.end()) M[w] = ++cnt;
                    token[i].push_back(M[w]);
                    w = "";
                } else {
                    w = w + str[c];
                }
            }
            sort(token[i].begin(), token[i].end());
        }

        fprintf(stderr, "%d\n", Tno);
        dfs(2);
        printf("Case #%d: %d\n", Tno, ans);
    }
}
