#pragma comment(linker, "/STACK:64000000")
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <sstream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

#define f first
#define s second
#define pb push_back
#define mp make_pair
#define ll long long
#define pii pair < int, int >
#define pll pair < long long, long long>
#define ull unsigned long long
#define y1 stupid_cmath
#define left stupid_left
#define right stupid_right
#define vi vector <int>
#define sz(a) (int)a.size()
#define forit(it, s) for(__typeof(s.begin()) it = s.begin(); it != s.end(); it++)
#define all(a) a.begin(), a.end()
#define sqr(x) ((x) * (x))

const int inf = (int)1e9;
const int mod = inf + 7;
const double eps = 1e-9;
const double pi = acos(-1.0);

int T, k, c, s;

void solve(int ind) {
    cin >> k >> c >> s;
    if (s < k) printf("Case #%d: IMPOSSIBLE\n", ind);
    else {
        printf("Case #%d:", ind);
        ll st = 1, step = 1;
        for (int i = 0; i < c - 1; i++) step *= k;
        for (int i = 0; i < s; i++) {
            printf(" %lld", st);
            st += step;
        }
        printf("\n");
    }
}

int main(){

    cin >> T;

    for (int i = 1; i <= T; i++) solve(i);

    return 0;
}
