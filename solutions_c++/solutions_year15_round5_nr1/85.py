#include <iostream>
#include <cstdio>
#include <string>
#include <string.h>
#include <queue>
#include <math.h>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <bitset>
#include <ctype.h>
#include <cassert>
#include <stack>
#include <fstream>
#include <unordered_map>
#include <unordered_set>
#include <ctime>
#include <functional>

using namespace std;

#define snd second
#define fst first
#define mp make_pair
#define ll long long
#define ull unsigned long long
#define ld long double
#define pb push_back
#define left _left
#define right _right

const ld pi = 3.14159265359;

template<typename T>
T abs(T x) {
    return x > 0 ? x : -x;
}

template<typename T>
T sqr(T x) {
    return x * x;
}

const int maxn = 1e6 + 5;

int pr[maxn];
vector<int> ch[maxn];
int cost[maxn];
int intree[maxn];
int sz = 0;

int l, r;


void add(int x) {
    if (x && !intree[pr[x]]) {
        return;
    }

    if (intree[x]) {
        return;
    }

    intree[x] = 1;
    sz++;

    queue<int> q;
    q.push(x);
    while (!q.empty()) {
        int v = q.front();
        q.pop();
        for (int to : ch[v]) {
            if (!intree[to] && l <= cost[to] && cost[to] <= r) {
                intree[to] = 1;
                sz++;
                q.push(to);
            }
        }
    }
}

void remove(int x) {
    if (!intree[x]) {
        return;
    }

    intree[x] = 0;
    sz--;
    queue<int> q;
    q.push(x);
    while (!q.empty()) {
        int v = q.front();
        q.pop();
        for (int to : ch[v]) {
            if (intree[to]) {
                intree[to] = 0;
                sz--;
                q.push(to);
            }
        }
    }
}

ll d;

map<int, vector<int>> byC;

void init() {
    int n;
    ll s0, as, cs, rs;
    ll m0, am, cm, rm;

    cin >> n >> d;
    cin >> s0 >> as >> cs >> rs;
    cin >> m0 >> am >> cm >> rm;

    for (int i = 0; i < n; i++) {
        ch[i].clear();
        intree[i] = 0;
    }
    sz = 0;

    byC.clear();
    cost[0] = s0;

    for (int i = 1; i < n; i++) {
        s0 = (s0 * as + cs) % rs;;
        m0 = (m0 * am + cm) % rm;;

        pr[i] = m0 % i;
        cost[i] = s0;
        ch[pr[i]].pb(i);
    }

    for (int i = 0; i < n; i++) {
        byC[cost[i]].pb(i);
    }
}


int main() {
    srand(time(NULL));
    //gen();
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int t;
    cin >> t;
    for (int tt = 1; tt <= t; tt++) {
        cerr << tt << endl;
        init();

        l = cost[0] - d;
        r = cost[0];

        int ans = 0;

        for (int i = l; i <= r; i++) {
            if (byC.count(i)) {
                for (int x : byC[i]) {
                    //cout << x << endl;
                    add(x);
                }
            }
        }

        ans = max(ans, sz);

        for (int i = l; i < cost[0]; i++) {
            l++;
            r++;
            if (byC.count(i)) {
                for (int x : byC[i]) {
                    remove(x);
                }
            }

            if (byC.count(r)) {
                for (int x : byC[r]) {
                    add(x);
                }
            }

            ans = max(ans, sz);
        }

        printf("Case #%d: %d\n", tt, ans);
    }

    return 0;
}