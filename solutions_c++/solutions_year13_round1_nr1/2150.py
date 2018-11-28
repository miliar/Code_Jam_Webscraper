#include<iostream>
#include<cmath>
using namespace std;
double T,t,Case,r;
int main()
{   
    //freopen("1.in","r",stdin);
    //freopen("1.out","w",stdout);
    cin>>T;
    Case=0;
    while(T--)
    {
     cin>>r>>t;
     double m1,m2;
     int flag=1;
     long long ans,left=1,right=t/r;
     while(flag)
     {
        ans=(left+right)/2; 
        m1=(2*r+2*ans-1)*ans;
        m2=(2*r+2*(ans+1)-1)*(ans+1);
        if(m1<=t&&m2>t) {cout<<"Case #"<<++Case<<": "<<ans<<endl;break;}
        else if(m1>t) right=ans-1;
        else if(m1<t) left=ans+1;               
     }          
    }      
}
