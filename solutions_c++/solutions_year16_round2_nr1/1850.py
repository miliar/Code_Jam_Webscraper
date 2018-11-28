/*
 * Author:heroming
 * File:heroming.cpp
 * Time:2016/5/1 0:00:30
 */
#include <vector>
#include <list>
#include <set>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <fstream>
#include <sstream>
#include <iostream>
#include <string>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
using namespace std;

#define px first
#define py second
#define pb push_back
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(), (v).end()
#define clr(v, e) memset(v, e, sizeof(v))
#define rep(it, v) for (auto it : v)
#define forn(i, n) for (int i = 0; i < (n); ++ i)
#define rforn(i, n) for (int i = (n) - 1; i >= 0; -- i)
#define form(i, a, b) for (int i = (a); i <= (b); ++ i)
#define rform(i, a, b) for (int i = (b); i >= (a); -- i)
#define forv(i, v) for (int i = 0; i < sz(v); ++ i)
#define iter(it, v) for (auto it = v.begin(); it != v.end(); ++ it)

typedef long long lint;
typedef vector<int> vint;
typedef vector<string> vstring;
typedef pair<int, int> pint;
typedef vector<lint> vlint;
typedef vector<pint> vpint;

const int maxn = 12;
const int maxm = 2010;
const int letter = 32;

const string P[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

int t, n;
char s[maxm];
int v[maxn], c[letter];

void solve(const char x, const int k) {
    int w = c[x - 'A'];
    if (w > 0) {
        v[k] += w;
        forv (i, P[k]) {
            c[P[k][i] - 'A'] -= w;
        }
    }
}

int main() {
    freopen("heroming.out", "w", stdout);
    scanf("%d", &t);
    form (cas, 1, t) {
        printf("Case #%d: ", cas);
        scanf("%s", s);
        n = strlen(s);
        clr(v, 0);
        clr(c, 0);
        forn (i, n) ++ c[s[i] - 'A'];
        solve('Z', 0);
        solve('X', 6);
        solve('W', 2);
        solve('U', 4);
        solve('G', 8);
        solve('S', 7);
        solve('V', 5);
        solve('R', 3);
        solve('I', 9);
        solve('O', 1);
        form (k, 0, 9) {
            forn (i, v[k]) {
                printf("%d", k);
            }
        }
        printf("\n");
    }
    
    return 0;
}
