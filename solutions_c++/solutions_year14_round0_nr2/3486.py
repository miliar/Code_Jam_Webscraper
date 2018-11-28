#include<cstdio>
#include <iostream>
#include <cstring>
#include<fstream>
#include <cstdlib>
#include <sstream>
#include <string>
#include <algorithm>
#include <cmath>
#include <vector>
#include <limits>
#define gc getchar_unlocked
#define NMAX 1561252

using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out_cookie.txt","w",stdout);
    int n;
    double c,f,x,t1,t2,t,tlast,r,rlast=0.0;
    scanf("%d",&n);
    for(int tt=1; tt<=n; tt++)
    {
        scanf("%lf %lf %lf",&c,&f,&x);
        //printf("c=%lf, x=%lf, r=%lf\n",c,x,r);
        t=1000000.0, tlast=1000001.0, t1=0.0,r=2.0;
        bool cond= false;
        while(t<tlast)
        {
            //printf("ini: tlast=%lf, t=%lf\n",tlast,t);
            if(cond==true) t1+= c/rlast;
            //printf("x=%lf, r=%lf\n",x,r);
            t2=double(x)/double(r);
            tlast=t;
            //printf("t1=%lf, t2=%lf\n",t1,t2);
            t=t1+t2;
            rlast=r;
            r+=f;
            cond=true;
           // printf("fin: tlast=%lf, t=%lf\n",tlast,t);
        }
        printf("Case #%d: %.7lf\n",tt,tlast);
    }
    return 0;
}
