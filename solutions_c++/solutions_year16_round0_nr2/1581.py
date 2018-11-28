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

vector<int> cnt(10);

void calc(ll x) {
    while (x) {
        cnt[x % 10]++;
        x /= 10;
    }
}

bool good() {
    for (int i = 0; i < 10; i++)
        if (!cnt[i]) return 0;
    return 1;
}

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
        string s;
        cin >> s;
        s += '+';
        int ans = 0;
        for (int i = 1; i < s.size(); i++) {
            if (s[i] != s[i - 1]) {
                ans++;
            }
        }
        printf("Case #%d: %d\n",TT,  ans);
    }
    
    
    RT;
    return 0;
}