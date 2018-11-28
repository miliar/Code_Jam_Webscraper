#include <bits/stdc++.h>
using namespace std;

int n_test;
int n;
vector<string> s[222];

vector<string> readline() {
    string line;
    getline(cin, line);

    vector<string> s;
    stringstream ss;
    ss << line;
    for (string x; ss >> x;)
        s.push_back(x);
    return s;
}

int bit(int n, int k) {
    return (n >> k) & 1;
}

int main() {

    // freopen("C.in", "r", stdin);
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C.out", "w", stdout);

    cin >> n_test; 
    for (int test = 1; test <= n_test; test++) {
        cin >> n;
        string dummy;
        getline(cin, dummy);

        map<string, int> l[2];
        l[0].clear();
        l[1].clear();
        auto eng = readline();
        auto fre = readline();

        for (string x: eng)
            l[0][x]++;
        for (string x: fre)
            l[1][x]++;

        n -= 2;
        for (int i = 0; i < n; i++)
            s[i] = readline();

        int ans = 1e9, cur = 0;
        for (int i = 0; i < n; i++) 
            for (string x: s[i])
                l[0][x]++;

        for (map<string, int>::iterator it = l[0].begin(); it != l[0].end(); it++)
            if (l[1][it->first] > 0)
                cur++;

        ans = min(ans, cur);
        for (int i = 1; i < (1 << n); i++) {
            int pstate = ((i - 1) >> 1) ^ (i - 1);
            int cstate = (i >> 1) ^ i;
            for (int k = 0; k < n; k++)
                if (bit(pstate, k) != bit(cstate, k)) {
                    int ii = bit(pstate, k);
                    int jj = bit(cstate, k);
                    for (string x: s[k]) {
                        l[ii][x]--;
                        if (l[ii][x] == 0 && l[jj][x] > 0)
                            cur--;
                    }
                    for (string x: s[k]) {
                        if (l[jj][x] == 0 && l[ii][x] > 0)
                            cur++;
                        l[jj][x]++;
                    }
                }
            ans = min(ans, cur);
        }

        cout << "Case #" << test << ": " << ans << "\n";
    }

    return 0;
}