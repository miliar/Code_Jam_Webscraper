#include<iostream>
#include<cstdio>
#include <iomanip>
using namespace std;

int main()
{
    int t,flag,n;
    long double C,F,X,rate,time,mini;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    n=0;
    while(t--)
    {
        n++;
        flag=0;
        cin>>C>>F>>X;
        rate=2.0;
        time=X/rate;
        mini=time;
       while(!flag)
       {
           time-=(X/rate);
           time+=(C/rate);
           rate+=F;
           time+=X/rate;
           if(time>mini)
                {flag=1;}
            else
                mini=time;
       }

        cout<<setprecision(12)<<"Case #"<<n<<": "<<mini<<endl;
        //printf("Case #%d: %ld\n",n,mini);

    }
    return 0;
}

