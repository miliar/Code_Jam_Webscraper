#include<iostream>
#include<cstdio>
#include<iomanip>
using namespace std;
int main()
{
    int t,k;
    cin>>t;
    for(k=1;k<=t;k++)
    {
         double c,f,x;
        cin>>c>>f>>x;
         double ans=0,ti=2;

        while(1)
        {
             double time1=x/ti;
           // cout<<time1<<endl;
             double time2=(c/ti)+(x/(ti+f));
           // cout<<time2<<endl;
            if(time1<time2)
            {
                ans+=time1;
                break;
            }
            ans+=(c/ti);
            ti+=f;

        }
        cout<<"Case #"<<k<<": ";
           printf("%.7lf\n",ans);
       // cout<<setprecision(7)<<ans<<endl;
    }


    return 0;
}

