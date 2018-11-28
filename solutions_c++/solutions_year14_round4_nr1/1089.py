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
typedef long long ll;
typedef pair<int, int> PII;

void solve(int ncase) {
    int n, x;
    cin >> n >> x;
    vector<int> f(n);
    for(int i = 0; i < n; i ++) {
        cin >> f[i];
    }
    sort(f.begin(), f.end());
    vector<int> mark(n, 0);
    int ans = 0;
    for(int i = 0; i < n; i ++) {
        if (mark[i] == 0) {
            mark[i] = 1;
            ans  ++;
            for(int j = n - 1; j >= 0; j --) {
                if (mark[j] == 0 && f[j] + f[i] <= x) {
                    mark[j] = 1;
                    break;
                }
            }
        }
    }
    cout << "Case #" << ncase << ": " << ans << endl;
}

int main() {
    ios::sync_with_stdio(false);
    //cout << setprecision(16) << endl;
#ifdef _zzz_
  freopen("A-large.in", "r", stdin);
   freopen("out.txt", "w", stdout);
#endif
    int T = 1;
    cin >> T;
    //scanf("%d", &T);
    int ncase = 0;
    while(T --) {
        solve(++ ncase);
    }
}
