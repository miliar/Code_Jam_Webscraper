#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
#include <cmath>
using namespace std;

int a, b;
int dig[20],p;
bool ok(int x)
{
    p=0;
    while(x)
    {
        dig[p++]=x%10;
        x/=10;
    }
    for(int i=0;i<p;i++)
        if(dig[i]!=dig[p-i-1])
            return false;
    return true;
}

int main()
{
//    freopen("D:\\data.in","r",stdin);
//    freopen("D:\\data.out","w",stdout);
    int cas, t = 0;
    scanf("%d", &cas);
    while (cas--)
    {
        scanf("%d %d", &a, &b);
        int ans = 0;
        for (int i = 1; i <= sqrt(b) + 2; i++)
        {
            if (i * i < a)continue;
            if (i * i > b)continue;
            if (ok(i) && ok(i * i))
                ans++;
        }
        printf("Case #%d: %d\n",++t,ans);
    }
    return 0;
}