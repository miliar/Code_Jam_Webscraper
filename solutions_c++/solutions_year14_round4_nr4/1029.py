#include <set>
#include <map>
#include <cmath>
#include <stack>
#include <queue>
#include <string>
#include <cstdio>
#include <vector>
#include <utility>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#define INF 2e9
#define pb push_back
#define mp make_pair
#define forn(i,n) for (int i = 0; i < n; i++)
#define MAXN 10

using namespace std;

typedef long long ll;
typedef vector <int> vi;
typedef vector <long long> vll;

int tests, n, m;
string s[MAXN];
int u[MAXN], mx = 0, ways  = 0;

void calc() {
    set <string> st[MAXN];
    for (int i = 0; i < m; i++) {
        string t = "";
        st[u[i]].insert(t);
        for (int j = 0; j < s[i].size(); j++) {
            t += s[i][j];
            st[u[i]].insert(t);
        }
    }
    int res = 0;
    forn (i, m) {
        res += st[i].size();
    }
    if (res == mx) {
        ways++;
    }
    if (res > mx) {
        mx = res;
        ways = 1;
    }
}

void gen(int pos = 0) {
    if (pos == m) {
        calc();
        return;
    }
    for (int i = 0; i < n; i++) {
        u[pos] = i;
        gen(pos + 1);
    }
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> tests;
    forn (it, tests) {
        mx = 0;
        cin >> m >> n;
        forn (i, m) {
            cin >> s[i];
        }
        gen();
        cout << "Case #" << it + 1 << ": " << mx << " " << ways << endl;
    }
    return 0;
}
