#include <iostream>
#include <map>
#include <string>

using namespace std;

char letters[3] = {'P', 'R', 'S'};
map<char, string> mapping = {
    {'P', "PR"},
    {'R', "RS"},
    {'S', "PS"},
};

map<pair<int, char>, string> cache;

const string& getbest(int n, char c) {
    const pair<int, char> key{n, c};
    string& ret = cache[key];
    if (ret.size()) return ret;

    if (n == 0) {
        ret.push_back(c);
    } else {
        string a = getbest(n-1, mapping[c][0]);
        string b = getbest(n-1, mapping[c][1]);

        ret = min(a+b, b+a);
    }

    return ret;
}

void solve(int e) {
    int n; cin >> n;
    int R, P, S; cin >> R >> P >> S;

    cout << "Case #" << e << ": ";

    string mn = "Z";
    for (int start=0; start<3; ++start) {
        const string& s = getbest(n, letters[start]);

        int RR = 0, PP = 0, SS = 0;

        for (const char c : s) {
            if (c == 'P') {
                ++PP;
            } else if (c == 'R') {
                ++RR;
            } else if (c == 'S') {
                ++SS;
            }
        }

        if (R == RR && P == PP && S == SS) {
            mn = min(mn, s);
        }
    }

    if (mn != "Z")
        cout << mn << endl;
    else
        cout << "IMPOSSIBLE" << endl;
}

int main() {
    int t; cin >> t;
    for (int e=1; e<=t; ++e)
        solve(e);
}
