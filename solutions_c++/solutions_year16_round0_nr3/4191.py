#include<bits/stdc++.h>

using namespace std;

#define ll long long int

ll powe(ll i,ll j)
{
    ll m=1;
    if(j==0)
        return 1;
    for(ll k=0;k<j;k++)
        m*=i;
    return m;
}

void getbinary(ll* arr,ll m,ll n)
{
    for(ll i=n-1;i>=0;i--)
    {
        if(m>=powe(2,i))
        {
            arr[i]=1;
            m-=powe(2,i);
        }
        else
            arr[i]=0;
    }
}

ll getval(ll* arr,ll i,ll n)
{
    ll sum=0;
    for(ll j=0;j<n;j++)
    {
        if(arr[j]==1)
            sum+=powe(i,j);
    }
    return sum;
}

ll checkprime(ll val)
{
    if(val%2==0)
        return 2;
    for(ll j=3;j<=sqrt(val);j+=2)
    {
        if(val%j==0)
            return j;
    }
    return 0;
}

int main()
{
    ll t,n,j,i,val,d,c=0;;
    cin>>t;
    while(t--)
    {
        c++;
        cin>>n>>j;
        ll m=1;
        for(i=0;i<n-1;i++)
            m*=2;
        m+=1;
        ll arr[n];
        ll countt=0;
        ll flag;
        cout<<"Case #"<<c<<":\n";
        while(1)
        {
            ll store[9];
            getbinary(arr,m,n);
            for(ll p=2;p<=10;p++)
            {
                flag=0;
                val=getval(arr,p,n);
                d=checkprime(val);
                //cout<<val<<" "<<d<<" ";
                if(d==0)
                {
                    flag=1;
                    break;
                }
                else
                {
                    store[p-2]=d;
                }
            }
            m+=2;
            if(flag==0)
            {
                for(ll i=n-1;i>=0;i--)
                    cout<<arr[i];
                cout<<" ";
                for(ll k=0;k<9;k++)
                    cout<<store[k]<<" ";
                countt++;
                cout<<"\n";
            }

            if(countt==j)
                break;
        }
    }
    return 0;
}
