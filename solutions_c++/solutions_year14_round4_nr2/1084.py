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
const int inf = 0x3fffffff;

int n;
int solve(vector<int>& num, int way) {
    vector<int> left, right;
    for(int i = 0; i < n; i ++) {
        if (way & (1 << i)) {
            left.push_back(num[i]);
        } else {
            right.push_back(num[i]);
        }
    }
    sort(left.begin(), left.end());
    sort(right.begin(), right.end(), greater<int>());
    vector<int> pos(n);
    for(int i = 0; i < n; i ++) {
        for(int j = 0; j < left.size(); j ++) {
            if (left[j] == num[i]) {
                pos[i] = j;
            }
        }
        for(int j = 0; j < right.size(); j ++) {
            if (right[j] == num[i]) {
                pos[i] = left.size() + j;
            }
        }
    }
    vector<int> tmp = num;
    vector<int> to(n);
    for(int i = 0; i < n; i ++) {
        to[pos[i]] = i;
    }
    int ret = 0;
    for(int i = 0; i < n; i ++) {
        int a = num[to[i]];
        int p = 0;
        for(int j = 0; j < n; j ++) {
            if (tmp[j] == a) {
                for(int k = j; k > i; k --) {
                      ret ++;
                      swap(tmp[k], tmp[k - 1]);
                }
                break;
            }
        }
    }
    return ret;
}
void solve(int ncase) {
    cin >> n;
    vector<int> num(n);
    for(int i = 0; i < n; i ++) {
        cin >> num[i];
    }
    int ans = inf;
    for(int k = 0; k < (1 << n); k ++) {
        ans = min(ans, solve(num, k));
    }
    cout << "Case #" << ncase << ": " << ans << endl;
}

int main() {
    ios::sync_with_stdio(false);
    //cout << setprecision(16) << endl;
#ifdef _zzz_
  freopen("B-small-attempt0.in", "r", stdin);
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
