#include<iostream>
#include<math.h>
#include<bits/stdc++.h>
#include<cstdio>
using namespace std;
int main()
{
    int t,mx,sum,ans,l,i,t1;
    string a;
    freopen("A-small-attempt2.in","r",stdin);
    freopen("output.in","w",stdout);
    cin>>t;
    t1=t;
    while(t--)
    {
        sum=0;
        ans=0;
        cin>>mx;
        cin>>a;
        l=a.length();
        for(i=0;i<l;i++)
        {
            sum+=a[i]-48;
            //cout<<sum<<" "<<ans<<" "<<i<<endl;
            if(sum<i+1&&(a[i+1]-48)!=0)
            {
                ans+=i+1-sum;
                sum=sum+ans;
            }

        }
        cout<<"Case #"<<t1-t<<": "<<ans<< endl;
    }
}
