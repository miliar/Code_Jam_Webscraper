#include <iostream>
#include <iosfwd>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cassert>
#include <cctype>
#include <climits>
#include <vector>
#include <bitset>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <deque>
#include <string>
#include <list>
#include <iterator>
#include <sstream>
#include <complex>
#include <fstream>
#include <functional>
#include <numeric>
#include <utility>
#include <algorithm>
#include <assert.h>
#include <unordered_map>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef double ld;
typedef vector < long long > vll;
typedef pair <long long, long long> pll;
typedef pair <int, int> pii;
typedef vector < int > vii;
typedef complex < double > Point;

#define csl ios_base::sync_with_stdio(false); cin.tie(NULL)
#define mp make_pair
#define fst first
#define snd second
#define prev PREV
int t, n, m, u, v, q, r, ql, qr, k, l, s, w, h, c, z, d;
const int N = 1e5 + 500;
const long long mod = 1e9 + 7;
const long long INF = 1LL << 52LL;
string str, S;
int main() {
    csl;
    cin >> t;
    for (int ii = 1; ii <= t; ++ii) {
        cout << "Case #" << ii << ": ";
        cin >> str;
        S = "";
        int sol = 0;
        bool x = true;
        str.push_back('E');
        while (x) {
            x = false;
            S = "";
            for (int i = 0; i < int(str.size()); i += 2) {
                if (str[i] == str[i + 1]) {
                    sol += 10;
                    x = true;
                    //cout << i << '\n';
                    continue;
                }
                S.push_back(str[i]);
                i--;
            }
            if (S == str) break;
            str = S;
        }
        //cout << S.size() << '\n';
        sol += 5 * (S.size() / 2);
        cout << sol << '\n';
    }
    return 0;
}
