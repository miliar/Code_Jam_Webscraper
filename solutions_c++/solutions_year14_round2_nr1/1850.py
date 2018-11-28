#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <cassert>
#include <ctime>
#include <queue>
#include <map>
#include <set>
#include <climits>
using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
typedef pair<int, int> PII;

#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(auto it=(c).begin();it!=(c).end();++it)
#define FILLCHAR(a, x) memset(a, x, sizeof(a))
#define SZ(x) ((int) (x).size())
#define ALL(x) (x).begin(), (x).end()

string minimize(string s)
{
    string ret = "";
    REP(i,SZ(s)) {
        if (i == 0 || s[i] != s[i - 1]) {
            ret += s[i];
        }
    }
    return ret;
}

int getCount(string s, int index, char c) {
    int cur = -1;
    int curc = 0;
    s += "X";
    REP(i, SZ(s)) {
        if (i == 0 || s[i] != s[i - 1]) {
            if (cur == index) {
                if (c == s[i - 1]) {
                    return curc;
                } else {
                    throw "Error";
                }
            }
            cur++;
            curc = 1;
        } else {
            curc++;
        }
    }
}

int run() {
    int n;
    cin >> n;
    VS col(n);
    REP(i,n) cin >> col[i];
    string mins = "";
    REP(i,n) {
        string current = minimize(col[i]);
        if (mins == "") {
            mins = current;
        } else if (mins != current) {
            return -1;
        }
    }

    int ret = 0;
    REP(i,SZ(mins)) {
        VI lens;
        int sum = 0;
        REP(j,n) {
            int cnt = getCount(col[j], i, mins[i]);
            lens.push_back(cnt);
            sum += cnt;
        }

        int average = sum / n;
        int best1 = 0, best2 = 0;
        REP(j,n) {
            best1 += abs(lens[j] - average);
            best2 += abs(lens[j] - average - 1);
        }

        ret += min(best1, best2);
    }

    return ret;
}
int main() {
    int T;
    cin >> T;
    REP(i,T) {
        int res = run();
        if (res == -1) {
            cout << "Case #" << i + 1 << ": Fegla Won" << endl;
        } else {
            cout << "Case #" << i + 1 << ": " << res << endl;
        }
    }
}

