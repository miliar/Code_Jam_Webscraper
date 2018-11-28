#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
    freopen("x.in","r",stdin);
    freopen("x.out","w",stdout);
    int T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        int n,sum=0,count=0;
        string s;
        cin>>n;
        cin>>s;
        for(int i=0;i<s.length();i++)
        {
            sum+=s[i]-'0';
            if(sum<i+1) count+=i+1-sum,sum=i+1;
            //cout<<sum<<endl;
        }
        cout<<"Case #"<<t<<": "<<count<<endl;
    }
}
