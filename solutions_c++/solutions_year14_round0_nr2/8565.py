#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
using namespace std;

typedef long long ll;

int main()
{
    freopen("//home//vivek//Desktop//input.txt","r",stdin);
    freopen("//home//vivek//Desktop//output.txt","w",stdout);
    ll t,cases,steps,i;
    double c,f,x,tot;
    cin>>cases;
    for(t=1;t<=cases;t++)
    {
        cin>>c>>f>>x;
        steps=(ll)floor(((x*f)/c -2.0)*(1.0/f));
        if(steps<0) tot=x/2.0;
        else
        {
            //steps=(ll)floor(((x*f)/c -2.0)*(1.0/f));
            tot=0.0;
            for(i=0;i<steps;i++)
            {
               tot+=c/(2.0+(double)i*f);
            }
            tot+=x/(2.0+(double)(steps)*f);
        }
        //cout<<"Case #"<<t<<": "<<tot<<endl;
        printf("Case #%lld: %.7lf\n",t,tot);
    }

}
