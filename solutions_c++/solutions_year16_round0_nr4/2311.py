#include <bits/stdc++.h>
#define ll long long int
#define ull unsigned long long int
#define s(a) scanf("%lld",&a)
#define pb push_back
#define mp make_pair
#define f first
#define sc second
#define inf 10e16

using namespace std;

int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    ll t,tt,n,i,j,k,l,w,ww,x,y,z,c;
    s(t);
    for(tt=1;tt<=t;tt++) {
        s(k);s(c);s(x);
        w=pow(k,c);
        ww=pow(k,c-1);
        cout<<"Case #"<<tt<<": ";
        for(i=1;i<=k;i++) {
            ll pos=i;
            for(j=2;j<=c;j++) {
                pos = (pos-1)*k + i;
            }
            cout<<pos<<" ";
        }
        cout<<endl;
    }
    return 0;
}
