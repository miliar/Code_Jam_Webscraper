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

int main() {
    int T;
    cin >> T;
    REP(t,T) {
        int A, B, K;
        cin >> A >> B >> K;
        int ret = 0;
        REP(i,A) REP(j,B) {
            if ((i & j) < K) {
                ret++;
            }
        }

        cout << "Case #" << t + 1 << ": " << ret << endl;
    }
}
