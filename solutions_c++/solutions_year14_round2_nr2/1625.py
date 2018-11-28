#include <iostream>
#include <cstdio>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <queue>
#include <vector>
#include <cstdlib>
#include <string>
#include <set>
using namespace std;

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int T,cas=0;
    scanf("%d",&T);
    while(T--)
    {
        int a,b,k,i,ans=0,j;
        scanf("%d%d%d",&a,&b,&k);
        for(i=0;i<a;i++)
            for(j=0;j<b;j++)
                if((i&j)<k)
                    ans++;
        printf("Case #%d: %d\n",++cas,ans);
    }
    return 0;
}
