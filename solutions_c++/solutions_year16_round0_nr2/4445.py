#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pdd pair<double,double>
#define X first
#define Y second
#define rep(i,a) for(ll i=0;i<a;++i)
#define repp(i,a,b) for(ll i=a;i<b;++i)
#define FILL(a,x) memset(a,x,sizeof(a))
#define    foreach( gg,itit )	for( typeof(gg.begin()) itit=gg.begin();itit!=gg.end();itit++ )
#define	mp make_pair
#define	pb push_back
#define fastScan ios_base::sync_with_stdio(0); cin.tie(NULL);
#define M 1e9+7



ll mpe(ll base, ll exponent, ll modulus)
{  
    ll result = 1;
    while (exponent > 0)
    {
        if (exponent % 2 == 1)
            result = (result * base) % modulus;
        exponent = exponent >> 1;
        base = (base * base) % modulus;
    }
    return result;
}

int main()
{
    fastScan;
    ll t;
    cin>>t;
    repp(i,1,t+1){
        string str;
        cin>>str;
        int cnt=0;
        repp(i,1,str.size()){
            if(str[i]!=str[i-1])cnt++;
        }
        if(str[str.size()-1]=='-')cnt++;
        cout<<"Case #"<<i<<": "<<cnt<<endl;
    }
    
    
    return 0;
}