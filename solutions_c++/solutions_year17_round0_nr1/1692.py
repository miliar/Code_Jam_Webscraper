#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
using namespace std;
typedef unsigned long long ull;
#define INF 18000000000000000

int N, K;
map<string, ull> cache;

string flip(string s, int p) {
    string res = s;
    for (int i = 0; i < K; ++i)
        res[p+i] = res[p+i] == '-' ? '+' : '-';
    return res;
}

ull solve(string s) {
    ull L = s.length();
    if (L < K) return INF;
    if (L == K) {
        if (count(s.begin(), s.end(), '-') == K) return 1;
        if (count(s.begin(), s.end(), '+') == K) return 0;
        return INF;
    }
    if (cache.count(s) > 0) return cache[s];
    ull res = INF;
    for (int i = 0; i < K; ++i) {
        //cout << s << " " << res << endl;
        if (i + K <= L) {
            if (s[i] == '-') {
                string f = flip(s, i).substr(i+1);
                //cout << i << " " << s << " " << f << " " << solve(f) << endl;
                res = min(res, 1 + solve(f));
                break;
            }
            else {
                string f = s.substr(i+1);
                res = min(res, solve(f));
            }
        }
    }
    cache[s] = res;
    return res;
}

int main()
{
    cin >> N;
    for (int i = 1; i <= N; ++i) {
        cache.clear();
        string S;
        cin >> S >> K;
        ull ans = solve(S);
        cout << "Case #" << i << ": ";
        if (ans == INF) cout << "IMPOSSIBLE" << endl;
        else cout << ans << endl;
    }


    return 0;
}

