#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>

#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<set>
#include<queue>
#include<stack>
#include<algorithm>
using namespace std;

#define fori(a,b) for(i = a; i <= b; i++)
#define forj(a,b) for(j = a; j <= b; j++)
#define fork(a,b) for(k = a; k <= b; k++)
#define scani(a) scanf("%d",&a);
#define scanlli(a) scanf("%lld", &a);
#define scanc(c) scanf("%c",&c);
#define scans(s) scanf("%s", s);
#define mp(a,b) make_pair(a, b)
#define ll(a) (long long int)(a)
#define vi vector<int>
#define vc vector<char>
#define vs vector<string>
#define println printf("\n");
#define sz(v) v.size()
#define len(s) s.length()
#define max(a,b) ((a > b) ? a : b)
#define min(a,b) ((a < b) ? a : b)

int main() {
    int i, j, t, len;
    scani(t)
    fori(1, t) {
        string str;
        cin >> str;
        len = str.length();
        int dp[len];
        if (str[0] == '+') {
            dp[0] = 0;
        } else {
            dp[0] = 1;
        }
        forj(1, len-1) {
            if (str[j] == str[j-1] || str[j] == '+') {
                dp[j] = dp[j-1];
            } else {
                dp[j] = dp[j-1] + 2;
            }
        }
        printf("Case #%d: %d\n", i, dp[len-1]);
    }
    return 0;
}