#include<bits/stdc++.h>
using namespace std;
typedef long long int i64;
int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cs = 1;cs<=t;cs++)
    {
        double c,f,x,sum=0.0;
        scanf("%lf%lf%lf",&c,&f,&x);
        int n = 0;
        while(c/(2+n*f) + x/(2+(n+1)*f) < x/(2+n*f))
        {
            sum += c/(2+n*f);
            n++;
        }
        sum += x/(2+n*f);
        printf("Case #%d: %.7lf\n",cs,sum);
    }
	return 0;
}
