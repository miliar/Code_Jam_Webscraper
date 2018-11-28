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

ll match1[1111];
ll match2[1111];

ll match(ll w,string a)
{
    vector<ll>v;
    ll ww=w;
    while(ww>0) {
        ll kk = ww%10;
        v.pb(kk);
        ww/=10;
    }
    while(v.size() < a.length()) v.pb(0);
    reverse(v.begin(),v.end());

    for(ll i=0;i<v.size();i++) {
        if(a[i]=='?') continue;
        ll kk = a[i]-'0';
        if(kk==v[i]) continue;
        return 0;
    }
    return 1;
}

ll leng(ll ww)
{
    if(ww==0) return 1;
    ll ans = 0;
    while(ww>0) {
        ww/=10;
        ans++;
    }
    return ans;

}

int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    ll n,t,i,j,k,l,w,ww,x,y,z;
    s(t);
    for(ll tt=1;tt<=t;tt++) {
        ll mn = 10839313131LL;
        ll aa=0,bb=0;
        string a,b;
        cin >> a >> b;
        l = a.length();

        for(i=0;i<=1000;i++) {
            match1[i]=match(i,a);
            match2[i]=match(i,b);

        }

        for(i=0;i<1000;i++) {
            for(j=0;j<1000;j++) {
                if(match1[i]==1 && match2[j]==1) {
                    w = abs(i-j);
                    if(w < mn) {
                        mn = w;
                        aa = i;
                        bb = j;
                    }
                    else if(w == mn) {
                        if(i < aa) {
                            aa = i;
                            bb = j;
                        }
                        else if(i == aa) {
                            if(j < bb) {
                                bb = j;
                            }
                        }
                    }
               }
            }
        }

        cout<<"Case #"<<tt<<": ";
        w = leng(aa);
        for(i=0;i<(l-w);i++) cout<<0;
        cout<<aa<<" ";
        w = leng(bb);
        for(i=0;i<(l-w);i++) cout<<0;
        cout<<bb<<endl;
    }
    return 0;
}
