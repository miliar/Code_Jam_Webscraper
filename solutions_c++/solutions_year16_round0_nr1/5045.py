#include<bits/stdc++.h>

using namespace std;

#define ll long long int

ll arr[10]={0};

ll calculate(ll n)
{
    while(n)
    {
        arr[n%10]=1;
        n/=10;
    }
    for(ll i=0;i<10;i++)
        if(arr[i]==0)
            return 0;
    return 1;
}

int main()
{
    ll t,n,k,i,d,count=0;
    cin>>t;
    while(t--)
    {
        count++;
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<count<<":"<<"INSOMNIA\n";
            continue;
        }
        k=n;
        i=1;
        while(1)
        {
            k=i*n;
            d=calculate(k);
            if(d==1)
            {
                cout<<"Case #"<<count<<":"<<k<<"\n";
                for(ll j=0;j<10;j++)
                    arr[j]=0;
                break;
            }
            i++;
        }
    }
    return 0;
}
