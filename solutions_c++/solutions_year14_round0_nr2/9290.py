#include <iostream>
#include <cstdio>
#include <string.h>
#include <cmath>
#include <algorithm>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    int i,j;
    double c,f,x;
    double time,buff,cook,time2,time3;
    double ans;
    scanf("%d",&t);
    for(i=1; i<=t; i++)
    {
        cook=0.0;
        buff=2.0;
        time=0.0;
        time2=0.0,time3=0.0;        ans=111111.0;
        scanf("%lf%lf%lf",&c,&f,&x);
        {
            for(j=1; j<=x; j++)
            {
                time=x/buff+time3;
                //		cout<<time<<endl<<time2<<endl<<time3<<endl;
                if(ans<time)
                    break;
                else
					ans=time;
                time3+=c/buff;
                buff+=f;
            }
        }
        printf("Case #%d: %.7lf\n",i,ans);
    }
    return 0;
}
