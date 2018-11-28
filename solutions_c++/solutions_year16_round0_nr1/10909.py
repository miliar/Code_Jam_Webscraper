#include <bits/stdc++.h>

#define ll long long int
using namespace std;
ll mod=1000000007;
ll pwr(ll a,ll b,ll mod) {a%=mod;if(a<0)a+=mod;ll ans=1; while(b) {if(b&1) ans=(ans*a)%mod; a=(a*a)%mod; b/=2; } return ans; }


void hashing(int *a,ll n)
{
    while(n!=0)
    {
        a[n%10]++;
        n=n/10;
    }
    //return a;
}

bool chk(int *a)
{
    int c=0;
    for(int i=0;i<10;i++)
    {
        if(a[i]>0)
        {
            c++;
        }
    }
    if(c==10)
    {
        return true;
    }
    else
    {
        return false;
    }
}

int main()
{
    int t;
    cin>>t;
    int l=t;
    while(t--)
    {   
        ll n;
        int a[10]={0};
        cin>>n;
        bool flag=false;
        ll k=2,s=n;
        if(n==0)
        {
            cout<<"case #"<<l-t<<": "<<"INSOMNIA"<<endl;
        }
        else
        {
        
        while(1)
        {
            hashing(a,n);
            flag=chk(a);
            if(flag==true)
            {
                break;
            }
            n=s*k;
            k++;
        }
        cout<<"case #"<<l-t<<": "<<n<<endl;
        
        
        }
        
        
    }
    

}