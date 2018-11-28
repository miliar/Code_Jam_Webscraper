#include<stdio.h>
#include<iostream>
#include<queue>
using namespace std;
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B.codeout","w",stdout);
    int t;
    cin>>t;
    for(int cnt=1;cnt<=t;cnt++)
    {
        double c,f,x,ans;
        scanf("%lf%lf%lf",&c,&f,&x);
        ans=x/2;
        for(int i=1;i<1000000;i++)
        {
            double tans = x/(2.0+i*f);
            for(int j=0;j<i;j++)tans+=(c/(2.0+j*f));
            if(tans>ans)break;
            else ans = tans;
        }
        printf("Case #%d: %.7lf\n",cnt,ans);
//        cout<<"Case #"<<cnt<<": "<<ans<<endl;

    }
}
