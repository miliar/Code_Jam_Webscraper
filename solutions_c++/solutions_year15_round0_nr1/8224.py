#include<bits/stdc++.h>
using namespace std;
#define rep(i,n) for(i=0;i<n;i++)
#define ll long long int
int main()
{
    ios_base::sync_with_stdio(false);
    string s;
    ll t,i,j,n,sum,ctr,x,y;
    cin>>t;
    rep(j,t)
    {
        sum=0;
        ctr=0;
        cin>>n>>s;
        rep(i,n+1)
        {
            x=s[i]-'0';
            if(x==0)
                continue;
            if(i<=sum)
            {
                sum=sum+x;
            }
            else
            {
                y=i-sum;
                ctr=ctr+y;
                sum=sum+x+y;
            }
        }
        cout<<"Case #"<<j+1<<": "<<ctr<<"\n";
    }
    return 0;
}
