#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <cstring>
#include <string>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <stack>
#include <vector>
#include <ctime>
#include <fstream>
#include <cmath>

using namespace std;

#ifndef LOCAL
#define cerr if(0)cerr
#endif
#define pb push_back
#define mp make_pair

#define F first
#define S second
#define RT fprintf(stderr, "\nTIME = %lf\n", 1.0 * clock()/CLOCKS_PER_SEC);

typedef long long ll;
typedef long double ld;

const int INFint = 2147483547;
const ll INF = 9223372036854775807ll;
const ll MOD = 1000000007ll;

const ld EPS = 1e-9;

#define FILE "vacation"


int main() {
    ios_base::sync_with_stdio(0);
#ifdef LOCAL
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#else
    //    freopen(FILE".in", "r", stdin); freopen(FILE".out", "w", stdout);
    //    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#endif
    int T;
    cin >> T;
    for (int TT = 1; TT <= T; TT++) {
        int k, c, s;
        cin >> k >> c >> s;
        vector<int> ans;
        if (k == 1) {
            ans.pb(1);
        } else {
            if (c == 1) {
                if (k > s) {
                    printf("Case #%d: IMPOSSIBLE\n", TT);
                    continue;
                }
                for (int i = 1; i <= k; i++) ans.pb(i);
                
            } else {
                if (k - 1 > s) {
                    printf("Case #%d: IMPOSSIBLE\n", TT);
                    continue;
                }
                for (int i = 2; i <= k; i++) ans.pb(i);

            }
        }
        printf("Case #%d: ", TT);
        for (int i = 0; i < ans.size(); i++) {
            printf("%d ", ans[i]);
        }
        printf("\n");

    }
    
    
    RT;
    return 0;
}