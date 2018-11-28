#include <cstdio>
#include <utility>
#include <queue>
#include <set>
#include <list>
#include <map>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;
typedef vector<int> VI;
typedef long long LL;
#define FOR(x, b, e) for(int (x)=(b); x<=(e); ++(x))
#define FORD(x, b, e) for(int (x)=(b); x>=(e); --(x))
#define REP(x, n) for(int x=0; x<(n); ++x)
#define VAR(v,n) __typeof(n) v=(n)
#define ALL(c) c.begin(),c.end()
#define SIZE(x) (int)x.size()
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define MP make_pair
#define PII pair<int, int>

int main() {
    int t;
    cin >> t;
    FOR(z, 1, t) {
        int sm;
        cin >> sm;
        string s;
        cin >> s;
        VI shyness;
        for (auto &&c : s)
            shyness.PB(c - '0');
        int num = 0;
        int ans = 0;
        for (int i = 0; i <= sm; i++) {
            int shy = shyness[i];
            if (num < i) {
                ans += (i - num);
                num = i + shy;
            }
            else {
                num += shy;
            }
        }
        cout << "Case #" << z << ": " << ans << endl;
    }
    return 0;
}
