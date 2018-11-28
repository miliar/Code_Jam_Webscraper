#include<bits/stdc++.h>

using namespace std;

char str[100007];
int main()
{
    int t,n,sum,ans,added_val,i,strval,x,k;
    cin>>t;
    for(k=1;k<=t;k++)
    {
    cin>>n;
    cin>>str;
    sum=str[0]-'0';
    ans=0;
    for(i=1;i<=n;i++)
    {
        strval=i;
        x=str[i]-'0';
        if(sum>=strval)
        {
            sum+=(x);
        }
        else
        {
            added_val=strval-sum;
            sum+=(added_val+x);
            ans+=(added_val);
        }
    }
    cout<<"Case #"<<k<<": "<<ans<<"\n";
    }
    return 0;
}
