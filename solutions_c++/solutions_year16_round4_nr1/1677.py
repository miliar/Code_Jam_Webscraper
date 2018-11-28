#include <cstdio>
#include <utility>
#include <string>

using namespace std;

char rcd[12+1][4096+1][4096+1];
pair<int,int> trace[4096+1][4096+1];

char comp(char ca, char cb) {
    if (ca == 'F' or cb == 'F' or ca == cb) {
        return 'F';
    } else if ((ca == 'P' and cb == 'S') or (ca == 'S' and cb == 'P')) {
        return 'S';
    } else if ((ca == 'S' and cb == 'R') or (ca == 'R' and cb == 'S')) {
        return 'R';
    } else {
        return 'P';
    }
}

char dp(int t, int s, int r) {
    if (t == 0) {
        if (s == 1) return 'S';
        else if (r == 1) return 'R';
        else return 'P';
    }
    if (rcd[t][s][r] != 0) {
        return rcd[t][s][r];
    }

    int n = (1 << t);
    int p = n - s - r;
    for (int ns = 0; ns <= s; ns++) {
        if (n/2-ns-r > p) continue;
        for (int nr = 0; nr <= r; nr++) {
            if (n/2-ns-nr > p) continue;
            int np = n/2-ns-nr;
            if (ns+nr+1 < np) continue;
            if (ns+np+1 < nr) continue;
            if (nr+np+1 < ns) continue;
            
            char ca = dp(t-1, ns, nr);
            char cb = dp(t-1, s-ns, r-nr);
            char cc = comp(ca, cb);
            if (cc != 'F') {
                trace[s][r] = make_pair(ns, nr);
                return rcd[t][s][r] = cc;
            }
        }
    }
    return rcd[t][s][r] = 'F';
}

void dfs(int t, int s, int r, string& ret) {
    if (t == 0) {
        if (s == 1) ret.push_back('S');
        else if (r == 1) ret.push_back('R');
        else ret.push_back('P');
        return;
    } else {
        auto pp = trace[s][r];
        int ns = pp.first;
        int nr = pp.second;

        dfs(t-1, ns, nr, ret);
        dfs(t-1, s-ns, r-nr, ret); 
    }
}

int main() {
    int T;
    scanf("%d", &T);

    for (int times = 0; times < T; times++) {
        int n, r, p, s;
        scanf("%d%d%d%d", &n, &r, &p, &s);

        memset(rcd, 0, sizeof(rcd));

        printf("Case #%d: ", times+1);
        char ret = dp(n, s, r);
        if (ret == 'F') {
            puts("IMPOSSIBLE");
        } else {
            string ret;
            dfs(n, s, r, ret);
            printf("%s\n", ret.c_str());
        }
    }
}
