#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <string>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <queue>
#include <assert.h>
#include <unordered_set>
#include <unordered_map>

using namespace std;

#define ll long long
#define ull unsigned long long
#define ld long double
#define mp make_pair
#define pb push_back
#define fst first
#define snd second

template<typename T>
T abs(T x) {
    return x > 0 ? x : -x;
}

template<typename T>
T sqr(T x) {
    return x * x;
}



vector<int> a[100];
char s[1000000];

vector<string> parse() {
    vector<string> res;
    int n = strlen(s);
    string c;
    for (int i = 0; i < n; i++) {
        if (s[i] == ' ') {
            if (c != "") {
                res.pb(c);
                c = "";
            }
        } else {
            c += s[i];
        }
    }

    if (c != "") {
        res.pb(c);
    }

    return res;
}

const int maxn = 1e7;
int usedE[maxn];
int usedF[maxn];
int currUsed = 1;

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int t;
    scanf("%d\n", &t);
    int tt = 0;
    while (t--) {
        tt++;
        cerr << tt << endl;
        int n;
        scanf("%d\n", &n);

        unordered_map<string, int> was;
        int v = 0;

        for (int i = 0; i < n; i++) {
            cin.getline(s, 1000000);

            auto u = parse();

            a[i].clear();
            for (auto x : u) {
                if (was.count(x)) {
                    a[i].pb(was[x]);
                } else {
                    was[x] = v++;
                    a[i].pb(was[x]);
                }
            }
        }


        int ans = 1e9;

        for (int i = 0; i < (1 << (n - 2)); i++) {

            currUsed++;
            int c = 0;
            for (auto x : a[0]) {
                if (usedE[x] != currUsed && usedF[x] == currUsed) {
                    c++;

                }

                usedE[x] = currUsed;
            }
            for (auto x : a[1]) {
                if (usedF[x] != currUsed && usedE[x] == currUsed) {
                    c++;

                }

                usedF[x] = currUsed;
            }

            for (int j = 2; j < n; j++) {
                if (i & (1 << (j - 2))) {
                    for (int x : a[j]) {
                        if (usedE[x] != currUsed && usedF[x] == currUsed) {
                            c++;

                        }

                        usedE[x] = currUsed;
                    }
                } else {
                    for (int x : a[j]) {
                        if (usedF[x] != currUsed && usedE[x] == currUsed) {
                            c++;

                        }

                        usedF[x] = currUsed;
                    }
                }
            }

            ans = min(ans, c);
        }

        cout << "Case #" << tt << ": " << ans << endl;
    }

    //cerr << mm << endl;

    return 0;
}