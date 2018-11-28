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

const int MAXN = 30;
const int MAXNUM = 5000;

int n;
vector <int> a[MAXN];
bool used[2][MAXNUM];
int lang[MAXN];

map <string, int> num_word;
vector <string> word;

int get_num_word (string s) {
    map <string, int> :: iterator it = num_word.find(s);
    if (it == num_word.end()) {
        num_word[s] = sz(word);
        word.pb(s);
        return (sz(word) - 1);
    }

    return it->sc;
}

int main () {
    //ios_base::sync_with_stdio(0);
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

    int tc;
    cin >> tc;

    for (int ti = 0; ti < tc; ++ti) {
        num_word.clear();
        word.clear();

        cin >> n;
        string s;
        getline (cin, s);

        for (int i = 0; i < n; ++i) {
            a[i].clear();

            getline (cin, s);
            stringstream ss;
            ss << s;

            while (ss >> s) {
                a[i].pb(get_num_word(s));
            }
        }

        int total_words = sz(word);
        int ans = total_words;
        for (int mask = 0; mask < (1 << (n - 2)); ++mask) {
            for (int i = 0; i < total_words; ++i) {
                used[0][i] = used[1][i] = false;
            }

            lang[0] = 0;
            lang[1] = 1;
            for (int i = 2; i < n; ++i) {
                lang[i] = ((mask >> (i - 2)) & 1);
            }

            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < sz(a[i]); ++j) {
                    used[lang[i]][a[i][j]] = true;
                }
            }

            int cur = 0;
            for (int i = 0; i < total_words; ++i) {
                if (used[0][i] && used[1][i]) {
                    cur++;
                }
            }

            ans = min(ans, cur);
        }

        cout << "Case #" << ti + 1 << ": " << ans << "\n";
        cerr << ti << endl;
    }

	return 0;
}
