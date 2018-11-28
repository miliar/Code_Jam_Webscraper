#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <sstream>
#include <iterator>
#include <functional>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cmath>
#include <cassert>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<ld, ld> pnt;

#define fi first
#define se second
#define mp make_pair
#define pb push_back

const int INF = 1000 * 1000 * 1000 + 9;
const ll MOD = 1000 * 1000 * 1000 + 7;
const ld EPS = 1e-9;


int main() {
#ifdef HOME
    freopen("/Users/sigma/Documents/Projects/blabla/blabla/input.txt", "r", stdin);
    freopen("/Users/sigma/Documents/output.txt", "w", stdout);
#endif
    int tn;
    cin >> tn;
    for (int ti = 0; ti < tn; ++ti) {
        int n;
        string s;
        cin >> s;
        n = s.size();
        while (n > 0 && s[n - 1] == '+') --n;
        int c = 0;
        for (int i = 1; i < n; ++i) c += s[i - 1] != s[i];
        cout << "Case #" << (ti + 1) << ": " << (n ? (c + 1) : 0) << '\n';
    }
    return 0;
}