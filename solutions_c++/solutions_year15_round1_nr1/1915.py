#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<string>
using namespace std;
typedef long long ll;
const int N = 1000+10;
const int mod = 100007;
ll a[N];
int main(){
    freopen("A-large.in","r",stdin);
    freopen("4_18.txt","w",stdout);
    int t , n, cas= 0;
    cin>>t;
    while(t--){
        scanf("%d",&n);
        for(int i=1;i<=n;i++) scanf("%lld",&a[i]);
        ll ans1 = 0 , ans2 = 0;
        for(int i=2;i<=n;i++) if(a[i]<a[i-1]) ans1 += a[i-1] - a[i];
        ll v = 0;
        for(int i=2;i<=n;i++) if(a[i]<a[i-1]) v = max(v,a[i-1]-a[i]);
        for(int i=1;i<=n-1;i++) ans2 += min(v,a[i]);
        printf("Case #%d: %lld %lld\n",++cas,ans1,ans2);
    }
    return 0;
}
