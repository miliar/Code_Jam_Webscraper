#include <vector>
#include<cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <deque>
#include <set>
#ifdef __GXX_EXPERIMENTAL_CXX0X__
#include <unordered_map>
#include <cassert>
#endif
#include <ctime>
#include <queue>
#include <stack>
#include<iomanip>
#include <sstream>
#include <cmath>
using namespace std;
typedef pair<int, int> PII;
typedef long long ll;
void solve(int ncase) {
    double c, f, x;
    cin >> c >> f >> x;
    double ans = 0.5 * x;
    double r = 2, pre = 0;
    for(int i = 1;pre <= ans ; i ++) {
        pre += c / r;
        r += f;
        ans = min(ans, pre + x / r);
    }
    cout << "Case #" << ncase << ": " << setprecision(16) << ans <<endl;
}
int main() {
    ios::sync_with_stdio(false);
    //cout << setprecision(16) << endl;
#ifdef _zzz_
    freopen("B--large.in", "r", stdin);
    freopen("B-out.txt", "w", stdout);
#endif
    int T = 1;
    cin >> T;
    int ncase = 0;
    while(T --) {
        solve(++ ncase);
    }
}
