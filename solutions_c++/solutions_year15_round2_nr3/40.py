#include <iostream>
#include <sstream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cstring>
#include <cmath>
#include <bitset>
#include <cstdlib>
#include <memory>
#include <ctime>

#define FILE

using namespace std;

struct stru {
    int d;
    long long m;
};

void solve() {
    int n;
    cin >> n;
    vector<stru> vec;
    vec.clear();
    for (int i = 0; i < n; i++) {
        int d, h, m;
        cin >> d >> h >> m;
        for (int j = m; j < m + h; j++) {
            stru s;
            s.d = d;
            s.m = j * 360LL;
            vec.push_back(s);
        }
    }
    n = vec.size();
    vector<long long> v;
    v.clear();
    long long l = -1;
    long long r = 1e18;
    for (int i = 0; i < n; i++) {
        int d = vec[i].d;
        long long m = vec[i].m;
        r = min(r, (720 - d) * m / 360);
        l = max(l, (360 - d) * m / 360);
        v.push_back((360 - d) * m / 360);
        for (int k = 0; k < n; k++) {
            v.push_back((k + (360 - d)) * m / 360);
        }
    }
    int ans = n - 1;
    for (int i = 0; i < v.size(); i++) {
        long long ma = v[i];

        int c = 0;
        for (int k = 0; k < n; k++) {
            int d = vec[k].d;
            long long mb = vec[k].m;
            if (ma == mb)
                continue;
            if (ma < mb)
                c += (360 - d) * mb / 360 > ma;
            else
                c += (ma * 360 / mb - (360 - d)) / 360;
        }
        if (c < ans)
            ans = c;

        c = 0;
        for (int k = 0; k < n; k++) {
            int d = vec[k].d;
            long long mb = vec[k].m;
            if (ma == mb)
                continue;
            if (ma < mb)
                c += (360 - d) * mb / 360 >= ma;
            else
                c += (ma * 360 / mb - (360 - d)) / 360 - ((ma * 360 / mb - (360 - d)) % 360 == 0);
        }
        if (c < ans)
            ans = c;
    }
    cout << ans << endl;
}

int main() {
#ifdef FILE
    freopen("E:/1.in", "r", stdin);
    freopen("E:/1.out", "w", stdout);
#endif // FILE

    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
