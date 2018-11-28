#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <bitset>
#include <sstream>
#include <queue>

#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz(a) ((int) (a).size())
#define eprintf(...) fprintf(stderr, __VA_ARGS__)

using namespace std;

typedef long long int64;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const long long inf64 = ((long long)1 << 62) - 1;
const long double pi = acos(-1);

template <class T> T sqr (T x) {return x * x;}
template <class T> T abs (T x) {return x < 0 ? -x : x;}

const int MAXN = 200;

int n, m;
int a[MAXN][MAXN];
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
bool good_turn[4];

int get_num (char c) {
    if (c == '.')
        return -1;
    if (c == '>')
        return 0;
    if (c == 'v')
        return 1;
    if (c == '<')
        return 2;
    assert (c == '^');
    return 3;
}

bool in_field (int x, int y) {
    return (x >= 0) && (x < n) && (y >= 0) && (y < m);
}

int main () {
    ios_base::sync_with_stdio(0);
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

    int tc;
    cin >> tc;

    for (int ti = 0; ti < tc; ++ti) {
        cin >> n >> m;

        string s;
        for (int i = 0; i < n; ++i) {
            cin >> s;
            for (int j = 0; j < m; ++j) {
                a[i][j] = get_num(s[j]);
            }
        }

        int ans = 0;
        bool key_pos = true;
        for (int i = 0; i < n && key_pos; ++i) {
            for (int j = 0; j < m && key_pos; ++j) {
                if (a[i][j] != -1) {
                    for (int t = 0; t < 4; ++t) {
                        good_turn[t] = false;

                        int x = i, y = j;
                        x += dx[t];
                        y += dy[t];
                        while (in_field(x, y) && a[x][y] == -1) {
                            x += dx[t];
                            y += dy[t];
                        }

                        if (in_field(x, y)) {
                            good_turn[t] = true;
                        }
                    }

                    if (!good_turn[a[i][j]]) {
                        ans++;
                        if (!good_turn[0] && !good_turn[1] && !good_turn[2] && !good_turn[3]) {
                            key_pos = false;
                            break;
                        }
                    }
                }
            }
        }

        if (!key_pos) {
            cout << "Case #" << ti + 1 << ": IMPOSSIBLE\n";
        } else {
            cout << "Case #" << ti + 1 << ": " << ans << "\n";
        }

    }


	return 0;
}
