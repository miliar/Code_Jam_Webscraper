#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t;
    int n;
    char shy[10005];
    scanf("%d", &t);
    int ans;
    int sum;
    for (int cases = 1; cases <= t; ++cases)
    {
        ans = 0;
        sum = 0;
        scanf("%d", &n);
        scanf("%s", shy);
        for (int i=0;i<=n;++i)
        {
            if (sum<i) {ans += i-sum; sum = i;}
            sum += shy[i]-'0';
        }
        printf("Case #%d: %d\n",cases, ans);
    }
    return 0;
}
