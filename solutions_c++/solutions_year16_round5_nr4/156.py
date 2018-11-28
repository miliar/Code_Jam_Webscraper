#include <iostream>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <queue>
#include <cassert>
#include <map>
#include <set>
#include <ctime>
#include <iomanip>

using namespace std;

#define x first
#define y second
#define mp make_pair
#define pb push_back
#define sz(X) ((int)((X).size()))

const double eps = 1e-10;
const int inf = 1000000000;

const int N = 1000005;
const int mo = 1000000000 + 7;



void work() {
    string bad;
    vector<string> s;
    int n, len;
    cin >> n >> len;
    for (int i = 0; i < n; ++i) {
        string t;
        cin >> t;
        s.pb(t);
    }
    cin >> bad;
    for (int i = 0; i < n; ++i)
        if (s[i] == bad) {
            cout << "IMPOSSIBLE" << endl;
            return;
        }
    string ss = "0?", t = "0";
    for (int i = 0; i < len - 1; ++i) {
        ss += "0?";
        t += "1";
    }
    cout << ss << ' ' << t << endl;
}

int main()
{
    #ifdef LOCAL_TEST
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; ++i) {
        printf("Case #%d: ", i);
        work();
    }
    return 0;
}
