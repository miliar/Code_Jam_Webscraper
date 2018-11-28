/*
 *
 * Tag: Implementation
 * Time: O(n)
 * Space: O(n)
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <unordered_map>
#include <unordered_set>
using namespace std;
const int N = 10010000;
const int M = 110;
const long long MOD = 1000000007;
const double eps = 1e-10;
string cur[2], pre[2], s;

int main() {
    freopen("/Users/ybc/Project/CCPP/ACM/A-large.in", "r", stdin);
    freopen("/Users/ybc/Project/CCPP/ACM/out.txt", "w", stdout);
    int T;
    cin>>T;
    for (int cas = 1; cas <= T; ++ cas) {
        printf("Case #%d: ", cas);
        cin>>s;
        pre[0] = cur[0] = s[0];
        pre[1] = cur[1] = s[0];
        for (int i = 1; i < s.length(); ++ i) {
            string tmp = "";
            tmp += s[i];
            if (pre[1] + tmp > pre[0] + tmp) {
                cur[0] = pre[1] + tmp;
            } else {
                cur[0] = pre[0] + tmp;
            }
            if (tmp + pre[1] > tmp + pre[0]) {
                cur[1] = tmp + pre[1];
            } else {
                cur[1] = tmp + pre[0];
            }
            pre[0] = cur[0];
            pre[1] = cur[1];
        }
        string ans;
        if (cur[0] > cur[1]) {
            ans = cur[0];
        } else {
            ans = cur[1];
        }
        cout<<ans<<endl;
    }
    return 0;
}