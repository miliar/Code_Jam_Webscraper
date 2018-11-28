#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <string>
#include <time.h>
#define clr(x,c) memset(x, c, sizeof(x))
#define pb push_back
#define mp make_pair
#define pii pair<int, int>
#define psi pair<string, int>
#define LLD_MAX 9223372036854775807LL
#define LLD_MIN (-LLD_MAX - 1LL)
#define inf 0x3f3f3f3f
typedef long long lld;
typedef unsigned long long ulld;
using namespace std;

//inline void R(string & str, int s, int e)
//{
//    reverse(begin(str) + s, begin(str) + e + 1);
//    for (int i = s; i <= e; ++i) str[i] = str[i] == '-' ? '+' : '-';
//}

const int MAXN = 111;
int dp[MAXN][2];

int main ()
{
//    freopen("C:/Users/ywy/Desktop/large.in", "r", stdin);
//    freopen("C:/Users/ywy/Desktop/in.txt", "r", stdin);
//    freopen("C:/Users/ywy/Desktop/large-out.txt", "w", stdout);
//    freopen("C:/Users/ywy/Desktop/out.txt", "w", stdout);
    int t, cas = 1;
    string str;
    cin >> t;
    while (t--) {
        clr(dp, 0);
        cin >> str;
        int n = str.length();
        dp[0][0] = str[0] == '+';
        dp[0][1] = str[0] == '-';
        for (int i = 1; i < n; ++i) {
            if (str[i] == '+') {
                dp[i][0] = min(dp[i-1][1] + 1, dp[i-1][0] + 2);
                dp[i][1] = min(dp[i-1][1], dp[i-1][0] + 1);
            } else {
                dp[i][0] = min(dp[i-1][0], dp[i-1][1] + 1);
                dp[i][1] = min(dp[i-1][1] + 2, dp[i-1][0] + 1);
            }
        }
        printf("Case #%d: %d\n", cas++, min(dp[n-1][1], dp[n-1][0]+1));
    }
    return 0;
}
