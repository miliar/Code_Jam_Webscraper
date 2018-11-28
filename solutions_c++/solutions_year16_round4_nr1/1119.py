#include "stdafx.h"

int N, cnt[3];
const int C = 3;
char let[] = "PRS";

void count(int n, int r, int* c)
{
    if (n == 0) { c[r]++; }
    else {
        int rr = (r + 1) % C;
        count(n - 1, r, c);
        count(n - 1, rr, c);
    }
}

string make(int n, int r)
{

    if (n == 0) { return string(&let[r], 1); }
    int rr = (r + 1) % C;
    string s = make(n - 1, r);
    string ss = make(n - 1, rr);
    DBG(1, V(n) << V(s) << V(ss));
    return s < ss ? s + ss : ss + s;
}


int main() {
    int T;
    cin >> T;

    FOR(tt, T)
    {
        cout << "Case #" << (tt + 1) << ": ";
        cin >> N;
        cin >> cnt[1] >> cnt[0] >> cnt[2];
        DBG(1, V(N) << V(cnt));
        string ans;
        FOR(r, C)
        {
            string sol;
            int c[C] = { 0, 0, 0 };
            count(N, r, c);
            DBG(1, V(N) << V(r) << V(c));
            FOR(rr, C) if (cnt[rr] != c[rr]) goto nxt;
            sol = make(N, r);
            if (!ans.size() || sol < ans) ans = sol;
        nxt:;
        }
        if (!ans.size()) ans = "IMPOSSIBLE";
        cout << ans << endl;
    }
    return 0;
}
