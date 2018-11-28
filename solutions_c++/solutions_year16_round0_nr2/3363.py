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
string s;

bool check(string &cur){
    for (int i = 0; i < cur.length(); ++ i) {
        if (cur[i] == '-') {
            return false;
        }
    }
    return true;
}

int main() {
    freopen("/Users/ybc/Project/CCPP/ACM/B-large.in", "r", stdin);
    freopen("/Users/ybc/Project/CCPP/ACM/out.txt", "w", stdout);
    int T;
    cin>>T;
    for (int cas = 1; cas <= T; ++ cas) {
        cin>>s;
        int ans = 0, bnd = (int)s.length() - 1;
        for (; bnd >= 0; -- bnd) {
            if (s[bnd] == '-') {
                ++ bnd;
                break;
            }
        }
        while (bnd > 0) {
            int idx = 0;
            for (; idx < bnd; ++ idx) {
                if (s[idx] == '-') {
                    -- idx;
                    break;
                }
            }
            if (idx == -1) {
                idx = 0;
                ++ ans;
                for (; idx < bnd; ++ idx) {
                    if (s[idx] == '+') {
                        -- idx;
                        break;
                    }
                }
                string t="";
                for (int i = bnd - 1; i > idx; -- i) {
                    if (s[i] == '+') {
                        t += '-';
                    } else {
                        t += '+';
                    }
                }
                for (int i = 0; i < idx; ++ i) {
                    -- bnd;
                }
                for (int i = 0; i < bnd; ++ i) {
                    s[i] = t[i];
                }
            } else {
                ++ ans;
                for (int i = 0; i <= idx; ++ i) {
                    s[i] = '-';
                }
            }
        }
        cout<<"Case #"<<cas<<": ";
        cout<<ans<<endl;
    }
    return 0;
}