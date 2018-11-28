#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define MST(a,b) memset(a,b,sizeof(a))

int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int nn;

    scanf("%d",&nn);
    FOR(ii,1,nn)
    {
        printf("Case #%d: ",ii);
        double c,f,x,tnow=0,snow=2;
        scanf("%lf%lf%lf",&c,&f,&x);
        while(624)
        {
            if(c/snow+x/(snow+f)>=x/snow)break;
            tnow=tnow+c/snow;
            snow=snow+f;
        }
        printf("%.10lf\n",tnow+x/snow);
    }
    return 0;
}
