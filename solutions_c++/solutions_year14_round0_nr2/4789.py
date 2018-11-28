#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int t,hh=0;
    cin>>t;
    while(t--)
    {
        hh++;
        printf("Case #%d: ",hh);
        
        double c,f,x;
        cin>>c>>f>>x;
        double ans=x/2.0;
        double speed =2.0;
        double temp=c/speed;
        double k=c/speed + x/(speed+f);
        while(k<ans)
        {
            ans=k;
            speed+=f;
            temp+=c/speed;
            k=temp+x/(speed+f);
        }
        printf("%.7lf\n",ans);
        
        
    }
    
}


