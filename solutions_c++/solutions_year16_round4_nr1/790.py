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

void precalc();

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

    precalc();

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

map <char, char> beats;
map <char, int> to_num;
vector <char> order;
vector <int> beatsorder;

vector <vector <string> > results;
vector <vector <vector <int> > > counts;

void count_lets(const string& s, vector <int>& a) {
    for (char c: s) {
        a[to_num[c]] += 1;
    }
}

void precalc() {
    beats['R'] = 'S';
    beats['S'] = 'P';
    beats['P'] = 'R';

    int MAX_N = 13;
    results.resize(MAX_N, vector <string> (3));
    counts.resize(MAX_N, vector <vector <int> > (3, vector <int> (3, 0)));

    order = {'R', 'S', 'P'};
    for (int i = 0; i < 3; ++i) {
        to_num[order[i]] = i;
    }
    beatsorder.resize(3);
    for (int i = 0; i < 3; ++i) {
        beatsorder[i] = to_num[beats[order[i]]];
    }

    for (int i = 0; i < 3; ++i) {
        results[0][i].push_back(order[i]);
        count_lets(results[0][i], counts[0][i]);
    }

    for (int lev = 1; lev < MAX_N; ++lev) {
        for (int i = 0; i < 3; ++i) {
            results[lev][i] = min(results[lev - 1][i] + results[lev - 1][beatsorder[i]], results[lev - 1][beatsorder[i]] + results[lev - 1][i]);
            count_lets(results[lev][i], counts[lev][i]);
        }
    }
}

void printerr() {
    cout << "IMPOSSIBLE\n";
}

void solve() {
    int n;
    cin >> n;
    map <char, int> nums;
    cin >> nums['R'] >> nums['P'] >> nums['S'];

    string bestres;
    for (int i = 0; i < 3; ++i) {
        bool f = true;
        for (int j = 0; j < 3; ++j) {
            if (counts[n][i][j] != nums[order[j]]) {
                f = false;
                break;
            }
        }
        if (f) {
            if (bestres.empty() || bestres > results[n][i]) {
                bestres = results[n][i];
            }
        }
    }

    if (bestres.empty()) {
        printerr();
    }
    else {
        cout << bestres << "\n";
    }
}