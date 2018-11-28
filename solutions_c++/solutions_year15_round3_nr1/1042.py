#include<iostream>
#include<cstring>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cmath>

using namespace std;

int main()
{
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
long long int t,tt,ans,r,c,w;
    t=0,ans;
    cin>>t;
    tt=t;
    while(t)
    {
       cin>>r>>c>>w;
       if(c%w==0)
       ans=r*(c/w)+(w-1);
       else
         ans=r*(c/w)+w;
        cout<<"Case #"<<tt-t+1<<": "<<ans<<endl;
        t--;

    }

    return 0;
}


