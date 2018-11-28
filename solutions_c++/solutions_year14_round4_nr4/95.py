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

const int MAXN = 10;
const int P = 1000 * 1000 * 1000 + 7;

bool used[MAXN];
int len[MAXN], color[MAXN];
string s[MAXN];
vector <string> pr[MAXN];
set <string> sets[MAXN];

int main ()
{
    ios_base::sync_with_stdio(0);
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

    int tc;
    cin >> tc;

    for (int ti = 0; ti < tc; ++ti) {
        cerr << ti << endl;

        int n, k;
        cin >> n >> k;

        for (int i = 0; i < n; ++i) {
            cin >> s[i];
            len[i] = s[i].length();
        }

        for (int i = 0; i < n; ++i) {
            string ss = "";
            pr[i].clear();
            pr[i].push_back(ss);
            for (int j = 0; j < len[i]; ++j) {
                ss.push_back(s[i][j]);
                pr[i].push_back(ss);
            }
        }

        int nmax = 0;
        int max_sum = 0;

        int deg = 1;
        for (int i = 0; i < n; ++i) {
            deg *= k;
        }

        for (int mask = 0; mask < deg; ++mask) {
            int tmask = mask;
            for (int i = 0; i < k; ++i) {
                used[i] = false;
            }

            for (int i = 0; i < n; ++i) {
                color[i] = tmask % k;
                used[color[i]] = true;
                tmask /= k;
            }

            bool key = true;
            for (int i = 0; i < k; ++i) {
                key &= used[i];
            }

            if (key) {
                for (int i = 0; i < k; ++i) {
                    sets[i].clear();
                }

                for (int i = 0; i < n; ++i) {
                    for (int j = 0; j < len[i] + 1; ++j) {
                        sets[color[i]].insert(pr[i][j]);
                    }
                }

                int cur = 0;
                for (int i = 0; i < k; ++i) {
                    cur += sets[i].size();
                }

                if (cur > max_sum) {
                    max_sum = cur;
                    nmax = 0;
                }

                if (cur == max_sum) {
                    nmax++;
                    if (nmax >= P) {
                        nmax -= P;
                    }
                }
            }
        }

        cout << "Case #" << ti + 1 << ": " << max_sum << " " << nmax << endl;
    }

	return 0;
}
