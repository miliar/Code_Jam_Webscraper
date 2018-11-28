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
int calc_war(vector<double>& a, vector<double>& b) {
    int n = a.size();
    int win = 0, big = n - 1;
    for(int i = n - 1; i >= 0; i --) {
        if (a[i] < b[big]) {
            big --;
            win ++;
        }
    }
    return win;
}
void solve(int ncase) {
    int n;
    cin >> n;
    vector<double> a(n), b(n);
    for(int i = 0; i < n; i ++) {
        cin >> a[i];
    }
    for(int i = 0; i < n; i ++) {
        cin >> b[i];
    }
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    cout << "Case #" << ncase << ": " << calc_war(b, a) << " " << n - calc_war(a, b) <<endl;
}
int main() {
    ios::sync_with_stdio(false);
    //cout << setprecision(16) << endl;
#ifdef _zzz_
    freopen("D--large.in", "r", stdin);
    freopen("D-out.txt", "w", stdout);
#endif
    int T = 1;
    cin >> T;
    int ncase = 0;
    while(T --) {
        solve(++ ncase);
    }
}
