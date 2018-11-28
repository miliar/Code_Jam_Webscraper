#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    int t,k;
    cin>>t;
    for(k=1;k<=t;k++)
    {
    int smax;
    cin>>smax;
    string s;
    cin>>s;
    int sum=s[0]-'0',a=0;
    for(int i=1;i<=smax;i++)
    {
            a+=max(0,i-sum);
            sum=sum+s[i]-'0'+max(i-sum,0);
    }
    cout<<"Case #"<<k<<": "<<a<<endl;
    }
    return 0;
}
