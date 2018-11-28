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
        ll cnt=0,n,arr[10]={0},j=1;
        cin>>n;
        if(n==0){cout<<"Case #"<<i<<": INSOMNIA"<<endl;continue;}
        while(cnt!=10){
            ll tmp=n*j;
            j++;
            ll dig;
            while(tmp){
                dig=tmp%10;
                tmp/=10;
                if(arr[dig]==0){
                    arr[dig]=1;
                    cnt++;
                }
            }
        }
        j--;
        cout<<"Case #"<<i<<": "<<n*j<<endl;
    }
    
    
    return 0;
}