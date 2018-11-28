#include <bits/stdc++.h>

typedef long long int ll;

#define mod 1000000007
#define sl(x) scanf("%lld",&x)
#define s(x) scanf("%d",&x)
#define pb push_back
#define mp make_pair
#define INF 1000000000

using namespace std;

ll powr (ll a, ll b)
{
    if (b == 0)
        return 1;
    ll x = powr(a, b/2);
    if (b % 2 == 0)
        return (x*x)%mod;
    else
        return (((x*x)%mod)*a)%mod;
}

int main()
{
    freopen("aa.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,p = 0;
    string s,str,str1;
    ll n,i;
    cin>>t;
    while(t--) {
        p++;
        str = "";
        str1 = "";
        cin>>s;
        int n = s.length();
        char prev = '#';
        for(i = 0; i < n; i++) {
            if(s[i] != prev) {
                str.pb(s[i]);
                prev = s[i];
            }
        }
        n = str.length();
        for(i = 0; i < n; i++) {
            if(str[i] == '-')
                str1[i] = '+';
            else str1[i] = '-';
        }
        reverse(str1.begin(),str1.end());
        ll ans = 0;
        for(i = 0; i < n; i++) {
            if(str[i] == '-') {
                if(i > 0) {
                    ans += 2;
                } else ans += 1;
            }
        }
        ll ans1 = 1;
        for(i = 0; i < n; i++) {
            if(str1[i] == '-') {
                if(i > 0) {
                    ans1 += 2;
                } else ans1 += 1;
            }
        }
        printf("Case #%d: %lld\n",p,min(ans,ans1));
    }
    return 0;
}
