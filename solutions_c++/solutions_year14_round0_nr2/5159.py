#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    int t,v;cin>>t;v=t;
    double c,f,x,d,b,n,p,q,r,sum;
    while(t--)
    {
        cin>>c>>f>>x;d=2.0;
        b=d;n=d+f;sum=0.0;
        p=x/d;q=c/d;r=x/n;
        while(p>q+r)
        {
            //cout<<p<<" "<<q<<" "<<r<<endl;
            sum+=q;
            d=n;n=d+f;
            p=x/d;q=c/d;r=x/n;
            //cout<<"sum = "<<sum<<endl;
        }
        sum+=p;
        printf("Case #%d: %0.7lf\n",v-t,sum);
    }
    return 0;
}
