#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cassert>
//#include <memory>
//#include <thread>
using namespace std;


#define INF 1e+9
#define mp make_pair
#define lint long long
#define pii pair<int, int>
#define MAXN 10000

int fibs[MAXN];
int n;

void init() {
    fill(fibs, fibs + n, 0);
}

void update(int x, int v) {
    while (x < n) {
        fibs[x] += v;
        x = x|(x + 1);
    }
}

int get(int x) {
    int ans = 0;
    while (x >= 0) {
        ans += fibs[x];
        x = (x & (x + 1)) - 1;
    }
    return ans;
}

pii buf[MAXN];
int a[MAXN];

int main() {
    ios_base::sync_with_stdio(false);
    int t; 
    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> n;
        for (int i = 0; i < n; i++)
            cin >> a[i];
        for (int i = 0; i < n; i++)
            buf[i] = mp(a[i], i);
        sort(buf, buf + n);
        init();
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int dn = n - i;
            int ss = buf[i].second - get(buf[i].second);
            ans += min(ss, dn - 1 - ss);
            update(buf[i].second, 1);
        }
        cout << "Case #" << i + 1 << ": " << ans << endl;
    }
}
