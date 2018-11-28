#include <iostream>
#include <fstream>
#include <queue>
#include <iomanip>
#include <cstdio>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <time.h>
#include <cassert>
#include <map>
#include <set>
#include <unordered_set>
#include <stack>
#include <time.h>
#include <cstdlib>
#include <cstring>
#include <string.h>

#define llong long long int
#define pb push_back
#define mp make_pair
#define pr pair <int, int>

using namespace std;
const int MAXN = 2e6 + 7;
int T;
int main() {
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#else
    //#define FNAME "sum2"
    //freopen(FNAME".in", "r", stdin);
    //freopen(FNAME".out", "w", stdout);
#endif
    //ios_base::sync_with_stdio(false);cin.tie();
    scanf("%d", &T);
    for (int test = 1; test <= T; test++) {
        int res = 0, cnt = 0, n;
        string st;
        scanf("%d", &n);
        cin >> st;
        for (int i = 0; i < st.size(); i++) {
            int x = st[i] - '0';
            if (!x) {
                continue;
            }
            if (i <= cnt) {
                cnt += x;
            } else {
                res += i - cnt;
                cnt += x + i - cnt;
            }
        }
        printf("Case #%d: %d\n", test, res);
    }
    return 0;
}