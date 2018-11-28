#include <bits/stdc++.h>
using namespace std;
int main()
{
    long long int i,j,t,sum,ct,num;
    cin>>t;
    for(j=1;j<=t;j++)
    {
        char *str;
        cin>>num;
        str = new char[num+1];
        cin>>str;
        sum=0;ct=0;
        for(i=0;i<=num;i++)
        {
            if(i>sum&&str[i]!='0')
            {
                ct+=(i-sum);
                sum+=str[i]-'0'+ct;
            }
            else if(i<=sum&&str[i]!='0')
                sum+=str[i]-'0';
        }
        cout<<"Case #"<<j<<": "<<ct<<endl;
    }
    return 0;
}
