#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("b.txt","w",stdout);
    int cas;
    scanf("%d",&cas);
    for (int nn=0;nn<cas;nn++)
    {
        double c,f,x,tmax=220000000.0;
        scanf("%lf%lf%lf",&c,&f,&x);
        for (int i=0;i<int(x+1);i++)
        {
            double t=0.0;
            t+=x/(2.0+i*f);
            for (int j=0;j<i;j++)
                t+=c/(2.0+j*f);
            if (t<tmax) tmax=t;
            //cout<<"..."<<t<<"..."<<i<<endl;
        }
        printf("Case #%d: %.7lf\n",nn+1,tmax);

    }
    return 0;
}
