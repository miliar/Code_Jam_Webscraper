#pragma comment (linker, "/STACK:128000000")
#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>
#include <cassert>
#include <string>

#define mp make_pair
#define pb push_back
#define sz(x) ((int)(x).size())
#define forn(i, n) for(int i=0;i<(n);++i)
#define clr(ar, val) memset(ar, val, sizeof(ar))

using namespace std;

typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
typedef pair<ld, ld> point;

const int MAXN = 2e5 + 200;
const int INF = int(1e9) + 7;
const long long LINF = 1ll * INF * INF;
const int md = int(1e9) + 7;
const ld eps = 1e-9;
const ld PI = 3.1415926535897932384626433832795l;

int test, n;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
    cin >> test;
    for (int it = 1; it <= test; it++) {
        string s;
        cin >> s;
        int ans = 0, pos = 0;
        while (pos < s.length() && s[pos] == '-') {
            pos++;
        }
        if (pos > 0) {
            ans = 1;
        }
        while (pos < s.length()) {
            if (s[pos] == '+') {
                pos++;
                continue;
            }
            while (pos < s.length() && s[pos] == '-') {
                pos++;
            }
            ans += 2;
        }
        printf("Case #%d: %d\n", it, ans);
    }
    return 0;
}
