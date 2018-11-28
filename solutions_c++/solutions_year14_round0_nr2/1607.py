#include <iostream>
#include <cstdio>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <functional>
#include <queue>
#include <vector>
#include <cstdlib>
#include <string>
#include <set>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T,cas=0;
    scanf("%d",&T);
    while(T--)
    {
        double c,f,x;
        scanf("%lf%lf%lf",&c,&f,&x);
        double ans=x/2.0,now=0.0f,v=2.0,temp;
        for(int i=1;;i++)
        {
            now=now+c/v;
            v=v+f;
            temp=now+x/v;
            if(temp<ans)
                ans=temp;
            else
                break;
        }
        printf("Case #%d: %.7f\n",++cas,ans);
    }
    return 0;
}
