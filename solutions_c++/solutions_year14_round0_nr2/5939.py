#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <queue>
#define ll long long
using namespace std;
int main()
{
    int t, i;
    double c, f, x, s, s0, s1, d;
    freopen("10.txt","r",stdin);
    freopen("8.txt","w",stdout);
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        printf("Case #%d: ",i);
        s=0;
        d=2;
        if(x<=c)
        {
            s=x/2;
            printf("%.7lf\n", s);
        }
        else
        {
            while(1)
            {
                s0=c/d+x/(f+d);
                s1=x/d;
                if(s0>s1)
                {
                    s+=s1;
                    break;
                }
                else
                {
                    s+=c/d;
                    d+=f;
                }
            }
            printf("%.7lf\n",s);
        }
    }
    return 0;
}
