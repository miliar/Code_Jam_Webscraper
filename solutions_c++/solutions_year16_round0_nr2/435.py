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

typedef long long LL;
#define rep(it,s) for(__typeof((s).begin()) it=(s).begin();it!=(s).end();it++)

int n;
int dp[110][2]; //0 [0,i] -, 1 [0,i] +

int main() {

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int ncases;
    cin>>ncases;

    for (int cas=1; cas<=ncases; cas++) {

        string s;
        cin>>s;

        n = s.length();

        dp[0][0] = (s[0]=='+');
        dp[0][1] = (s[0]=='-');

        for (int i=1; i<n; i++) {

            if (s[i]=='-') {
                dp[i][0] = min(dp[i-1][0], dp[i-1][1] + 1);
                dp[i][1] = min(dp[i-1][0] + 1, dp[i-1][1] + 2);
            }
            else {
                dp[i][1] = min(dp[i-1][1], dp[i-1][0] + 1);
                dp[i][0] = min(dp[i-1][0] + 2, dp[i-1][1] + 1);
            }

        }

        int res = dp[n-1][1];

        printf("Case #%d: %d\n", cas, res);

    }

    return 0;

}
