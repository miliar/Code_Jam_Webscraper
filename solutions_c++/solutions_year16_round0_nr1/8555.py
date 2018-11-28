#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int t1=1;t1<=t;t1++)
    {
        ll n,idx=0,j=1,rem=0,num;
        cin>>n;
        int hash[10];
        memset(hash,0,sizeof(hash));
        if(n==0)
        {
            idx=1;
            cout<<"Case #"<<t1<<": INSOMNIA"<<endl;
            continue;
        }
        for(ll i=n;;i=j*n)
        {
            //cout<<i<<endl;
            ll temp=i;
            while(temp!=0)
            {
                rem=temp%10;
                hash[rem]=1;
                temp/=10;
            }
	    int flag=0;
            for(ll x=0;x<10;x++)
            {
                if(hash[x]==0) flag=1;
            }
            if(flag==0)
            {
                num=i;
                break;
            }
            j++;
        }
            cout<<"Case #"<<t1<<": "<<num<<endl;
    }
    return 0;
}
