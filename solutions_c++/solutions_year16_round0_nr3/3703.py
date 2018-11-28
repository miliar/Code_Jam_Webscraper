#include <bits/stdc++.h>
#define ll unsigned long long

using namespace std;

vector<string> vec;

ll d_mulmod(ll a,ll b)
{
    ll x=0,y=a;
    while(b>0)
    {
        if(b&1)
            x=(x+y);
        y=(y<<1);
        b>>=1;
    }
    return x;
}

ll d_pow(ll a,ll b)
{
    ll x=1,y=a;
    while(b>0)
    {
        if(b&1)
            x=d_mulmod(x,y);
        y=d_mulmod(y,y);
        b>>=1;
    }
    return x;
}

ll convert_base(string & str,ll base)
{
    ll num=0;
    for(ll i=0;i<str.size();i++)
    {
        num+=(str[i]-48)*d_pow(base,str.size()-i-1);
    }
    return num;
}

void build(ll n)
{
    string str;
    for(ll i = 0; i < d_pow(2,n); i++)
    {
        str= "";
        ll temp = i;
        for (ll j = 0; j < n; j++)
        {
            if (temp%2 == 1)
                str = '1'+str;
            else
                str = '0'+str;
            temp = temp/2;
        }
        vec.push_back("1"+str+"1");
    }
} 

int isPrime(ll num)
{
    int ans;
    for(ll i=1;i*i<=num;i++)
    {
        if(num%i==0)
        {
            ans=i;
        }
    }
    return ans;
}
int main(void)
{
    ll t,N,J,num,ans,cnt;

    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);
    
    scanf("%llu",&t);
    scanf("%llu %llu",&N,&J);
    N-=2;
    cout << "Case #" << t << ":\n";
    build(N);
    for(ll i=0,cnt=0;i<vec.size() && cnt<J;i++)
    {
        vector<ll> div;
        for(ll j=2;j<=10;j++)
        {
            num=convert_base(vec[i],j);
            ans=isPrime(num);
            if(ans!=1 && ans!=num)
                div.push_back(ans);
        }
        if(div.size()==9)
        {
            cnt++;
            cout << vec[i] << " ";
            for(ll i=0;i<div.size();i++)
                cout << div[i] << " ";
            cout << "\n"; 
        }
          
    }

    return 0;
}