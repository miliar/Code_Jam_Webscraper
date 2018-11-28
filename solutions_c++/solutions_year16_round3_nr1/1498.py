#include<bits/stdc++.h>
#define ll long long int
#define s(a) scanf("%lld",&a)
#define f first
#define sc second
#define pb push_back
#define mp make_pair
#define inf 10e16
#define sd(a) scanf("%lf",&a)

using namespace std;

ll a[101];

ll emptyA(ll n)
{
    ll i;
    for(i=1;i<=n;i++) {
        if(a[i]==0) continue;
        return 0;
    }
    return 1;
}

int main()
{
    ll t,n,i,j,k,l,w,ww,x,y,z,tt;

        freopen("inp.txt","r",stdin);
        freopen("out.txt","w",stdout);
    s(t);
    for(tt = 1;tt <= t;tt++) {
        s(n);
        for(i=1;i<=n;i++) {
            s(a[i]);
        }
        vector<ll>v;
        cout<<"Case #"<<tt<<": ";
        while(emptyA(n)==0) {
            ll mx = 0;
            v.clear();
            for(i=1;i<=n;i++) {
                if(a[i]>mx) {
                    mx = a[i];
                    v.clear();
                    v.pb(i);
                }
                else if(a[i]==mx) {
                    v.pb(i);
                }
            }
            if(v.size()==2) {
                w = v[0];
                a[w]--;
                w--;
                w=w+'A';
                printf("%c",w);
                w = v[1];
                a[w]--;
                w--;
                w=w+'A';
                printf("%c ",w);

            }
            else {
                w = v[0];
                a[w]--;
                w--;
                w=w+'A';
                printf("%c ",w);
            }
        }
        cout<<endl;
    }
    return 0;
}
