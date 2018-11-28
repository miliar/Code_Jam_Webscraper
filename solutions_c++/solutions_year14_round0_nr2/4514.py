//GCJ 2014 Q B
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <string>
#include <queue>
#define INF 1e9
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int Case;
    double C,F,X,m,ans,c,s;
    scanf("%d",&Case);
    for(int ca=1;ca<=Case;++ca)
    {
        scanf("%lf%lf%lf",&C,&F,&X);
        ans=INF;
        s=2.0;
        m=0.0;
        while(m+X/s<ans)
        {
            ans=m+X/s;
            m+=C/s;
            s+=F;
        }
        printf("Case #%d: %.7lf\n",ca,ans);
    }
    return 0;
}
