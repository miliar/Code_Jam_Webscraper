#include<bits/stdc++.h>

using namespace std;
typedef long long ll;
ll t,k,c,s;
ll moc(ll a,ll b)
{
    if(b==0LL)return 1LL;
    if(b%2LL==1LL)return a*moc(a,b-1LL);
    ll cast=moc(a,b/2LL);
    return cast*cast;
}
int main()
{
    cin>>t;
    for(int xyz=1;xyz<=t;xyz++)
    {
        cin>>k>>c>>s;
        cout <<"Case #"<<xyz<<":";
        ll xx=moc(k,c-1LL);
        for(int i=0;i<s;i++)cout <<" "<<1LL+i*xx;
        cout <<endl;
    }
    return 0;
}
