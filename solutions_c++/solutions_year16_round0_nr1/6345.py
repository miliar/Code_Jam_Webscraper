#include<bits/stdc++.h>
using namespace std;
int T,N,ck,ans;
void work(int &x,int v)
{
    while(v)
    {
        x|=(1<<(v%10));
        v/=10;
    }
}
int main()
{
    cin>>T;
    for(int data=1;data<=T;data++)
    {
        cout<<"Case #"<<data<<": ";
        cin >> N;
        if(N==0){cout<<"INSOMNIA"<<endl;continue;}
        ck=0;
        for(int i=1;ck!=(1<<10)-1;i++)
        {
            int tnow = i * N;
            work(ck,tnow);
            ans=tnow;
        }
        cout<<ans<<endl;
    }
}
