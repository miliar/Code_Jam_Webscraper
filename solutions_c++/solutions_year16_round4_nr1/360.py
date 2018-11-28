#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#include <memory.h>
#include <string>
#include <sstream>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;

#define MP make_pair
#define PB push_back
#define FF first
#define SS second

#define FORN(i, n) for (int i = 0; i <  (int)(n); i++)
#define FOR1(i, n) for (int i = 1; i <= (int)(n); i++)
#define FORD(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define FOREACH(i, c) for (typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)

#define MOD 1000000007
#define INF 2000000000

const int MAXC = 26;
int cnt[MAXC];

int T, r, p, s, tr, tp, ts; string line;

string start[3] = {"R", "P", "S"};

string goback(string s) {
    string res;

    FORN(i, s.size()) {
        if (s[i] == 'R') {
            res += "RS";
        }
        else if (s[i] == 'P') {
            res += "PR";
        }
        else {
            res += "SP";
        }
    }

    return res;
}

string arrange(string s) {
    if (s.size() == 1) return s;

    int slen = s.size();
    string spre = arrange(s.substr(0, slen / 2));
    string ssuf = arrange(s.substr(slen / 2));

    if (spre > ssuf) {
        return ssuf + spre;
    }
    else {
        return spre + ssuf;
    }
}

int main() {
    scanf("%d", &T); int N;

    for (int tc = 1; tc <= T; tc++) {
        printf("Case #%d: ", tc);
        scanf("%d%d%d%d", &N, &r, &p, &s);

        string res;

        FORN(i, 3) {
            line = start[i];
            while (line.size() < r + p + s) line = goback(line);

            memset(cnt, 0, sizeof cnt);
            FORN(j, line.size()) cnt[line[j]-'A']++;

            if (cnt['R'-'A'] == r && cnt['P'-'A'] == p && cnt['S'-'A'] == s) {
                line = arrange(line);

                if (res.size() == 0 || line < res) {
                    res = line;
                }
            }
        }

        if (res.size() == 0) {
            cout << "IMPOSSIBLE\n";
        }
        else {
            cout << res << "\n";
        }
    }
    
    return 0;
}
