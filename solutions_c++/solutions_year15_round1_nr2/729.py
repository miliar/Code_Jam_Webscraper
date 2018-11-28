#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
ll b,n;
ll m[1005];
int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int T;
    scanf("%d",&T);
    int ca = 0;
    while (T--) {
        scanf("%lld%lld",&b,&n);
        ll ma = 0;
        for (int i = 0; i<b; i++) {
            scanf("%lld",&m[i]);
            ma = ma>m[i]?ma:m[i];
        }
        ll r = ma*n;
        ll l = 0;
        ll mid;
        ll ans;
        while (l<r) {
            mid = (l+r)/2;
            ll cnt = 0;
            for (int i = 0; i<b; i++)
                cnt += mid/m[i]+1;
            if (cnt<n) l = mid+1;
                  else r = mid;
        }
        //cout<<mid<<endl;
        ll cnt = 0;
        for (int i = 0; i<b; i++)
            cnt += l/m[i]+((l%m[i]==0)?0:1);
        for (int i = 0; i<b; i++) {
            cnt += (l%m[i]==0)?1:0;
            if (cnt==n) {ans=i+1; break;}
        }
        printf("Case #%d: %lld\n",++ca,ans);

    }
}
