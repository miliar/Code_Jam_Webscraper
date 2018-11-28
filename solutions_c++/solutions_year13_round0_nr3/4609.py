#include <stdio.h>
#include <iostream>
#include <stack>
#include <vector>
#include <string>
#include <math.h>
#include <limits>
#include <algorithm>

using namespace std;

bool isPalin(int n)
{
    int t=0;
    int r=n;
    while (n)
    {
        t=t*10+n%10;
        n/=10;
    }
    return t==r;
}

int main()
{
    freopen("csmall.in","r",stdin);
    freopen("csmall.out","w",stdout);
    bool sqr[1010]={0};
    bool is[1010]={0};
    for (int i=0; i*i<=1000; i++) sqr[i*i]=1;
    for (int i=0; i<=1000; i++) is[i]=isPalin(i);
    int dp[1010]={0};
    for (int i=1; i<=1000; i++)
    {
        dp[i]=dp[i-1];
        if (is[i] && sqr[i])
        {
            int s = (int)sqrt(i);
            if (is[s]) dp[i]++;
        }
    }
    int T,cas,a,b;
    cin>>T;
    for (cas=1; cas<=T; cas++)
    {
        cin>>a>>b;
        printf("Case #%d: %d\n",cas,dp[b]-dp[a-1]);
    }
    return 0;
}
