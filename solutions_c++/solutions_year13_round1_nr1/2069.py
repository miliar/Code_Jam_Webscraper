#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<string>
#include<set>
#include<map>
#define pi acos(-1)
using namespace std;


int main()
{
    freopen("C:\\Users\\vivek\\Desktop\\in.txt","r",stdin);
    freopen("C:\\Users\\vivek\\Desktop\\out.txt","w",stdout);
    int T,i,ans,j;double r,t,ar,totar=0.0;
    //cout<<pi<<endl;
    cin>>T;
    for(i=1;i<=T;i++)
    {
       cin>>r>>t;
       ans= (int)floor((1.0- 2.0*r + sqrt((2.0*r-1.0)*(2.0*r-1.0) + 8.0*t))/4.0);
       cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}

                     
