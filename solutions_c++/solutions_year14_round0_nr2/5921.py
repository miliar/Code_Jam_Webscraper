#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("ttt1.in","r",stdin);
    freopen("ttt1.out","w",stdout);
    int t,cc=1;cin>>t;
    while(t--)
    {
        double c,f,x,ans=0.0;
        scanf("%lf%lf%lf",&c,&f,&x);
        int i=0;
        while((double)(f*c*i)<(double)(f*x-(f+2.0)*c))
        {
            ans+=(double)(c/(2.0+f*i));i++;
        }
        ans+=(double)(x/(2.0+f*i));
        printf("Case #%d: %.7lf\n",cc++,ans);
    }
    return 0;
}
