#pragma comment(linker, "/STACK:6400000000000")

#define _USE_MATH_DEFINES

#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <stack>
#include <cstring>
#include <iomanip>
#include <ctime>
#include <stack>
#include <bitset>
using namespace std;

typedef long long ll;
typedef long double ld;

const ld EPS = 1e-9;
const int INF = (int)(2e9 + 0.5);
const int MAXN = 300;

int t, ans, now, smax;
string s;

int main() {
    freopen("INPUT.TXT", "r", stdin);
    freopen("OUTPUT.TXT", "w", stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> t;
    for(int q = 1; q <= t; ++q) {
        cin >> smax >> s;
        ans = now = 0;
        for(int i = 0; i < (int)s.size(); ++i) {
            int c = s[i] - '0';
            if(now < i) {
                ans += i - now;
                now = i;
            }
            now += c;
        }
        cout << "Case #" << q << ": " << ans << "\n";
    }
}
