#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

bool check(int R, int P, int S, string &s) {

    if(R < 0 || P < 0 || S < 0) {
        s = "IMPOSSIBLE";
        return false;
    }
    if(R == 0 && P == 0 && S == 0) return true;
    string ns = "";
    for(const char &c : s) {
        if(c == 'R') S--, ns.push_back('R'), ns.push_back('S');
        if(c == 'P') R--, ns.push_back('P'), ns.push_back('R');
        if(c == 'S') P--, ns.push_back('P'), ns.push_back('S');
    }

    s = ns;
    return check(R, P, S, s);
}

string opt(string s, int N) {
    //cout << s << endl;
    if(s == "IMPOSSIBLE") return "IMPOSSIBLE";
    if(N == 1) return s;
    int m = N / 2;
    string fh = s.substr(0, m), sh = s.substr(m, m);
    fh = opt(fh, m), sh = opt(sh, m);
    if(fh < sh) {
        return fh + sh;
    } else {
        return sh + fh;
    }
}

int main()
{
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        int N, R, P, S;
        cin >> N >> R >> P >> S;

        vector<string> res(6);

        string seq = "PR";
        check(R - 1, P - 1, S, seq);
        res[0] = seq;
        seq = "RP";
        check(R - 1, P - 1, S, seq);
        res[1] = seq;
        seq = "PS";
        check(R, P - 1, S - 1, seq);
        res[2] = seq;
        seq = "SP";
        check(R, P - 1, S - 1, seq);
        res[3] = seq;
        seq = "RS";
        check(R - 1, P, S - 1, seq);
        res[4] = seq;
        seq = "SR";
        check(R - 1, P, S - 1, seq);
        res[5] = seq;

        for(int i = 0; i < 6; i++) {
            res[i] = opt(res[i], pow(2, N));
        }

        sort(res.begin(), res.end());

        int j = 0;
        while(j < 5 && res[j] == "IMPOSSIBLE") j++;

        cout << "Case #" << t << ": " << res[j] << endl;
    }
    return 0;
}
