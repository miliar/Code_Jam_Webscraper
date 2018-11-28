#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<string>
#include<iostream>
#include <utility>
#define PI 3.14159265359
#define eps 0.000000001
using namespace std;
typedef long long LL;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t,m,i,j;
    scanf("%d",&t);
    for(int ca=1;ca<=t;ca++)
    {
        double c,f,x;
        scanf("%lf%lf%lf",&c,&f,&x);
        double n=2.0;
        double sum=0.0;
        while(1)
        {
            double ti1=x/n;
            double ti2=c/n+x/(n+f);
            if(ti2-ti1>eps)break;
            sum+=c/n;
            n=n+f;
        }
        sum+=x/n;
        printf("Case #%d: %lf\n",ca,sum);
    }
}
