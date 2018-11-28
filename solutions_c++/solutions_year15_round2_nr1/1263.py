#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <stdio.h>
#include <map>
#include <sstream>
#include <string.h>

using namespace std;
int test[1000000];
int r(int i)
{
    int ret = 0;
    while(i!=0)
    {
        ret*=10;
        ret += i%10;
        i/=10;
    }
    return ret;
}
int main()
{
    int m,n;
    int T,cas = 1;
    memset(test,0x3f,sizeof(test));
    test[1] = 1;
    for(int i=1;i<=999999;i++)
    {
        test[i+1] = min(test[i+1],test[i]+1);
        int ri = r(i);
        test[ri] = min(test[ri],test[i]+1);
    }
    test[1000000] = test[999999] + 1;
    freopen("d:\\codejam\\A-small-attempt0.in","r",stdin);
    freopen("d:\\codejam\\A-small-attempt0.out","w",stdout);

    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&n);
        printf("Case #%d: %d\n",cas++,test[n]);
    }

    return 0;
}
