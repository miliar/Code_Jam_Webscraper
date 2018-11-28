#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    int t,j;
    cin>>t;
    for(j=1;j<=t;j++)
    {
        int smax;
        cin>>smax;
        string s;
        cin>>s;
        int sum=s[0]-'0',ans=0;
        for(int i=1;i<=smax;i++)
        {
                ans+=max(i-sum,0);
                sum=sum+max(i-sum,0)+s[i]-'0';
        }
        cout<<"Case #"<<j<<": "<<ans<<endl;
    }
    return 0;
}
