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

int solve(string s) {
    int ret = 0;

    int up = 0;
    for (int i = 0; i < s.size(); i++) {
        int cnt = s[i] - '0';
        if (cnt) {
            if (up < i) {
                int add = i - up;
                ret += add;
                up += add;
            }

            up += cnt;
        }
    }

    return ret;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int sMax;
        string s;
        cin >> sMax >> s;
        cout << "Case #" << i + 1 << ": " << solve(s) << endl;
    }
}
