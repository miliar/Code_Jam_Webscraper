#include <bits/stdc++.h>
#define ll long long int
#define s(a) scanf("%lld",&a)
#define pb push_back
#define mp make_pair

using namespace std;

int main()
{
    //freopen("inp.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    ll t,i,j,n,tot,ans;
    string s;
    s(t);
    for(j=1;j<=t;j++) {
        printf("Case #%lld: ",j);
        s(n);
        s.clear();
        cin>>s;
        tot=0;
        ans=0;
        for(i=0;i<=n;i++) {
            if(tot < i) {
                ans=ans+i-tot;
                tot=tot+i-tot;
            }
            tot=tot+s[i]-'0';
        }
        printf("%lld\n",ans);
    }
    return 0;
}
