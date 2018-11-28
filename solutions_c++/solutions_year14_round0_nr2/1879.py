#include<bits/stdc++.h>
using namespace std;
int main()
{
    //freopen("Inp2.txt","r",stdin);
    //freopen("Output3.txt","w",stdout);
    int t,test=0;
    double c,f,x,maxval,run,ans;
    cin>>t;
    while(t--)
    {
        test++;
        ans=0.000000;
        scanf("%lf %lf %lf",&c,&f,&x);
        if(x<=c)
        {
            printf("Case #%d: %.7lf\n",test,x/2);
        }
        else
        {
            maxval = f*(x/c-1);
            run=2.0;
            while(run<maxval)
            {
                ans+=(c/run);
                run+=f;
            }
            ans+=(x/run);
            printf("Case #%d: %.7lf\n",test,ans);
        }
    }
    return 0;
}
