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
#define FORD(x, b, e) for(int (x)=(b); x>=(e); ––(x))
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

const int K = 4;

int main() {
    int t;
    scanf("%d", &t);
    FOR(z, 1, t) {
        set<int> possible[2];
        int ans, cou = 0;
        REP(d, 2) {
            int a, temp;
            scanf("%d", &a);
            a--;
            REP(i, K) {
                REP(j, K) {
                    scanf("%d", &temp);
                    if (i == a)
                        possible[d].insert(temp);
                }
            }
        }
        FOREACH(it, possible[0])
            if (possible[1].count(*it)) {
                ans = *it;
                cou++;
            }
        cout << "Case #" << z << ": ";
        if (cou == 0)
            cout << "Volunteer cheated!";
        else if (cou > 1)
            cout << "Bad magician!";
        else
            cout << ans;
        cout << endl;
    }
    return 0;
}
