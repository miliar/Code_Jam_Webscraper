#include <cstdio>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <cstring>
#include <string>
#include <iostream>
#include <cassert>
#include <memory.h>
using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define foreach(it, a) for (__typeof((a).begin()) it = (a).begin(); it != (a).end(); it++)
#define pb push_back
typedef long long ll;
typedef pair<int, int> pii;
typedef long double ld;
/*
string mem[5][2100][2100][3];
bool u[5][2100][2100][3];

string get(int i, int p, int r, int s, int w) {
    assert((p + r + s) == (1 << i));
    assert(p >= 0 && r >= 0 && s >= 0);
    // if (i > 0) {
    //     if (p > r + s || r > p + s || s > p + r) return "";
    // }
    string& res = mem[i][p][r][w];
    if (u[i][p][r][w]) return res;
    u[i][p][r][w] = true;

    if (i == 0) {
        if (w == 0 && p == 1) return res = "P";
        if (w == 1 && r == 1) return res = "R";
        if (w == 2 && s == 1) return res = "S";
        return res = "";
    }

    int cl = (p + r + s) >> 1;
    int w1 = w;
    int w2 = (w1 + 1) % 3;
    forn(lp, min(p, cl) + 1)
        forn(lr, min(r, cl - lp) + 1) {
            int ls = cl - lp - lr;
            if (ls > s) continue;
            {
                const string& sl = get(i - 1, lp, lr, ls, w1);
                if (!sl.empty()) {
                    const string& sr = get(i - 1, p - lp, r - lr, s - ls, w2);
                    if (!sr.empty()) {
                        if (res.empty() || sl + sr < res) {
                            res = sl + sr;
                        }
                    }
                }
            }
            {
                const string& sl = get(i - 1, lp, lr, ls, w2);
                if (!sl.empty()) {
                    const string& sr = get(i - 1, p - lp, r - lr, s - ls, w1);
                    if (!sr.empty()) {
                        if (res.empty() || sl + sr < res) {
                            res = sl + sr;
                        }
                    }
                }
            }
        }

    // cout << p << " " << r << " " << s << ", w " << w << ": " << res << endl;

    return res;
}
*/
vector<string> ss;
void solve() {
    int n, p, r, s;
    scanf("%d %d %d %d", &n, &r, &p, &s);
    // string ans = get(n, p, r, s, 0);
    // const string& ans2 = get(n, p, r, s, 1);
    // const string& ans3 = get(n, p, r, s, 2);
    // if (ans.empty() || (ans2.size() && ans2 < ans)) ans = ans2;
    // if (ans.empty() || (ans3.size() && ans3 < ans)) ans = ans3;
    // if (ans == "") ans = "IMPOSSIBLE";
    string ans = "";
    for (const string& st : ss) {
        int cr = 0, cp = 0, cs = 0;
        for (const char c : st) {
            cr += c == 'R';
            cp += c == 'P';
            cs += c == 'S';
        }
        if (cr == r && cp == p && cs == s) {
            ans = st;
        }
    }
    if (ans.empty()) ans = "IMPOSSIBLE";
    printf("%s\n", ans.c_str());
}


struct Item {
    int w, r, p, s;
    string x;
};



void gen() {
    vector<Item> items;
    items.push_back(Item{0, 1, 0, 0, "R"});
    items.push_back(Item{1, 0, 1, 0, "P"});
    items.push_back(Item{2, 0, 0, 1, "S"});

    for (int n = 1; n <= 12; n++) {
        vector<Item> newItems;
        for (const Item& il : items)
            for (const Item& ir : items)
                if (il.w != ir.w) {
                    int nw = ir.w;
                    if (ir.w == (il.w + 1) % 3) nw = il.w;
                    string nx = il.x + ir.x;
                    bool found = false;
                    for (Item& ii : newItems)
                        if (ii.r == il.r + ir.r && ii.p == il.p + ir.p) {
                            if (ii.x > nx) ii.x = nx;
                            found = true;
                            break;
                        }
                    if (!found) {
                        newItems.push_back(Item{nw, il.r + ir.r, il.p + ir.p, il.s + ir.s, nx});
                    }
                }
        items = newItems;
        for (const Item& s : items) ss.push_back(s.x);
        fprintf(stderr, "%d...\n", n);
    }
}

int main() {
    gen();
    int tc;
    scanf("%d", &tc);
    for (int q = 1; q <= tc; q++) {
        printf("Case #%d: ", q);
        solve();
    }
    return 0;
}

