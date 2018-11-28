#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<iostream>
#include<cstdio>
#include<vector>
#include<map>

#define maxn 1000000
using namespace std;

char str[110];
int dp[110];
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("ans.out","w", stdout);
    int T;
    scanf("%d", &T);
    for (int kase=1;kase<=T;kase++)
    {
        scanf("%s", str);
        int l = strlen(str);
        if (str[0] == '+') dp[0] = 0;
        else dp[0] = 1;
        for (int i=1;i<l;i++)
            if (str[i] == str[i-1]) dp[i] = dp[i-1];
            else if (str[i] == '+') dp[i] = dp[i-1];
            else dp[i] = dp[i-1]+2;
        printf("Case #%d: ", kase);
        printf("%d\n", dp[l-1]);
    }
    return 0;
}
