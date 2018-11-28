#pragma comment (linker, "/STACK:128000000")
#include <iostream>
#include <cstdio>
#include <fstream>
#include <functional>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <bitset>
#include <ctime>
#include <sstream>
#include <stack>
#include <cassert>
#include <list>
#include <deque>

using namespace std;

#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()

typedef long long li;
typedef long long i64;
typedef pair <int, int> pi;
typedef vector <int> vi;
typedef double ld;
typedef vector<int> vi;
typedef pair <int, int> pi;

void solve();

//int timer = 0;
#define FILENAME ""

int main() {
    string s = FILENAME;
#ifdef YA
    //assert(!s.empty());
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //cerr<<FILENAME<<endl;
    //assert (s != "change me please");
    clock_t start = clock();
#else
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    //freopen(FILENAME ".in", "r", stdin);
    //freopen(FILENAME ".out", "w", stdout);
    cin.tie(0);
#endif
    cout.sync_with_stdio(0);
    cout.precision(10);
    cout << fixed;
    int t = 1;

    cin >> t;
    for (int i = 1; i <= t; ++i) {
        //++timer;
        cout << "Case #" << i << ": ";
        solve();
    }
#ifdef YA
    cerr << "\n\n\n" << (clock() - start) / 1.0 / CLOCKS_PER_SEC << "\n\n\n";
#endif
    return 0;
}

int n;
vector <vector <int> > newst;

bool gogo(int pos, const vector<int>& perm, vector <int>& arr) {
    if (pos == perm.size()) {
        for (int f: arr) {
            if (!f) {
                return false;
            }
        }
        return true;
    }

    bool found = false;
    for (int i = 0; i < n; ++i) {
        if (!arr[i] && newst[perm[pos]][i]) {
            found = true;
            arr[i] = 1;
            bool result = gogo(pos + 1, perm, arr);
            arr[i] = 0;
            if (!result) {
                return false;
            }
        }
    }
    if (!found) {
        bool result = gogo(pos + 1, perm, arr);
        if (!result) {
            return false;
        }
    }

    return true;
}

bool check(const vector <int>& perm) {
    vector <int> curarr(n, 0);
    return gogo(0, perm, curarr);
}

bool start_pere() {
    vector <int> perm;
    for (int i = 0; i < n; ++i) {
        perm.push_back(i);
    }
    while (true) {
        if (!check(perm)) {
            return false;
        }
        if (not next_permutation(perm.begin(), perm.end())) {
            break;
        }
    }
    return true;
}

void solve() {
    cin >> n;
    vector <vector <int>> start(n, vector <int> (n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            char c;

            cin >> c;
            if (c == '1') {
                start[i][j] = 1;
            }
        }
    }

    int ans = 1000;
    for (int mask = 0; mask < (1 << (n * n)); ++mask) {
        newst = start;
        int cost = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if ((1 << (n * i + j)) & mask) {
                    ++cost;
                    newst[i][j] = 1;
                }
            }
        }
        if (start_pere()) {
            ans = min(ans, cost);
        }
    }

    cout << ans << endl;
}