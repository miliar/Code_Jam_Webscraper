#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#define inf 0x3f3f3f3f
#define ll __int64
using namespace std;

int t,cas;
double s,f,c,x,ti;


int main()
{
  //  freopen("B-large.in","r",stdin);
 //   freopen("test.out","w",stdout);
    scanf("%d",&t);
    cas=1;
    while(t--)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        s=2.0;ti=0;
        while(x/s > c/s+x/(s+f))
        {
            ti+=c/s;
            s+=f;
        }
        ti+=x/s;
        printf("Case #%d: %.7lf\n",cas++,ti);
    }
    return 0;
}
