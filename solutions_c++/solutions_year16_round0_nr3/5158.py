#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

string tos(long long n)
{
    string s="";
    while(n)
    {
        if(n%2==0)  s+='0';
        else s+='1';
        n/=2;
    }
    return s;
}

ll power(ll n,ll i)
{
    ll ret=1;
    for(ll j=0;j<i;j++)
        ret*=n;
    return ret;
}

ll check(string x,long long base)
{
    long long n=0;
    for(ll i=0;i<x.size();i++)
        n+=(x[i]-'0')*power(base,i);
    for(ll j=2;j<=sqrt(n);j++)
        if(n%j==0)
            return j;
    return 0;
}
int main()
{
    freopen( "C-small-attempt1.in", "r", stdin );
	freopen( "C-small-attempt0.out", "w", stdout );
    long long t,n,k,i,cnt=0;
    cin >> t >> n >> k ;
    string x,s;
    bool f=true;
    printf("Case #1:\n");
    for(i=1<<15;cnt<k&&i<1<<16;i++)
    {
        if((i&1)&&(i&(1<<15))){
            x=tos(i);
            for(int j=2;j<=10;j++){
                if(!check(x,j))
                    f=false;
            }
            s=x;
            reverse(s.begin(),s.end());
            if(f){
                cout<<s<<" ";
                for(int j=2;j<=10;j++){
                    cout<<check(x,j)<<" ";
                }
                cout<<endl;
                cnt++;
            }
            f=true;
        }
    }
}
