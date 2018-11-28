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
string s[1010][2];
int dp[1<<16];

bool equals[1010][1010][2];

int solve(int mask) {
    if (dp[mask]>=0) return dp[mask];
    if (mask == (1<<n)-1) return 0;

    int tmp = 0;

    for (int i=0; i<n; i++) if ((mask&(1<<i))==0) {

        bool first = 0, second = 0;

        for (int j=0; j<n; j++) if ((mask&(1<<j))) {

            if (equals[i][j][0]) first = 1;
            if (equals[i][j][1]) second = 1;

        }

        if (second && first) {
            tmp = max(tmp, solve(mask | (1<<i))+1);
        }
        tmp = max(tmp, solve(mask | (1<<i)));

    }

    //cout<<mask<<" "<<tmp<<endl;
    dp[mask] = tmp;

    return tmp;
}

int main() {

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int t;
    cin>>t;
    for (int c=0; c<t; c++) {
        cin>>n;

        for (int i=0; i<n; i++) cin>>s[i][0]>>s[i][1];

        for (int i=0; i<n; i++) {
            for (int j=i+1; j<n; j++) {
                for (int k=0; k<2; k++) {
                    if (s[i][k]==s[j][k]) {
                        equals[i][j][k] = 1;
                        equals[j][i][k] = 1;
                    }
                    else {
                        equals[i][j][k] = 0;
                        equals[j][i][k] = 0;
                    }
                }
            }
        }

        for (int i=0; i<(1<<n); i++) dp[i] = -1;

        int res = solve(0);

        printf("Case #%d: %d\n", c+1, res);

    }

    return 0;

}
