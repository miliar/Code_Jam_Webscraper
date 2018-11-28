#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;
#define PB push_back
#define MP make_pair
#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

int n, t;
long long p;

long long min_rank(long long k) {
    long long num = (1LL << n) - k - 1;
    long long rank = 0;
    for (int i = 0; i < n; ++i) {
        if (num == 0) {
            rank |= 1LL << (n - i - 1);
        } else {
            num = (num - 1) / 2;
        }
    }
    return rank;
}

long long max_rank(long long k) {
    long long num = k;
    long long rank = 0;
    for (int i = 0; i < n; ++i) {
        if (num == 0) {
        } else {
            num = (num - 1) / 2;
            rank |= 1LL << (n - i - 1);
        }
    }
    return rank;
}

void solve() {
    cin >> n >> p;
    long long lb = 0, ub = (1LL << n) - 1;
    while (lb != ub) {
        long long mid = (lb + ub + 1) / 2;
        if (min_rank(mid) < p)
            lb = mid;
        else
            ub = mid - 1;
    }
    long long ans1, ans2;
    ans1 = lb;
    lb = 0;
    ub = (1LL << n) - 1;
    while (lb != ub) {
        long long mid = (lb + ub + 1) / 2;
        if (max_rank(mid) < p)
            lb = mid;
        else
            ub = mid - 1;
    }
    ans2 = ub;
    cout << "Case #" << ++t << ": " << ans2 << ' ' << ans1 << endl;
}

int main() {
    freopen("B.out", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
        solve();
    return 0;
}
