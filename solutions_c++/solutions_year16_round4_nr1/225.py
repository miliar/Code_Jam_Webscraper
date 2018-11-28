#include <bits/stdc++.h>

#define FO(i,a,b) for (int i = (a); i < (b); i++)
#define sz(v) int(v.size())

using namespace std;

string t[3] = {
    "R",
    "S",
    "P"
};

string gen(int n, int i) {
    if (n == 0) return t[i];
    else {
        string a = gen(n-1,i);
        string b = gen(n-1,(i+1)%3);
        return min(a+b,b+a);
    }
}

int n, r, p, s;

bool allg(string &l) {
    int mr = 0, mp = 0, ms = 0;
    FO(i,0,sz(l)) {
        if (l[i] == 'R') mr++;
        if (l[i] == 'S') ms++;
        if (l[i] == 'P') mp++;
    }
    return mr == r &&
        mp == p &&
        ms == s;
}

int main() {
    int T; scanf("%d", &T);
    FO(Z,1,T+1) {
        scanf("%d %d %d %d", &n, &r, &p, &s);
        string res = "Z";
        FO(i,0,3) {
            string ans = gen(n,i);
            if (allg(ans)) {
                res = min(ans,res);
            }
        }
        if (res == "Z") res = "IMPOSSIBLE";
        printf("Case #%d: %s\n", Z, res.c_str());
    }
}

