#include <cstdio>
#include <algorithm>

using namespace std;

typedef long long ll;
int cnt;
int a,b,k;
ll ans;
void solve(){
    printf("Case #%d: ",++cnt);
    scanf("%d%d%d",&a,&b,&k);
    ans = 0;
    for(int i = 0;i < a;i ++) {
        for(int j = 0;j < b;j ++) {
            if((i & j) < k) ans ++;
        }
    }
    printf("%I64d\n",ans);
}
int main() {
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int t;
    scanf("%d",&t);
    while(t --) {
        solve();
    }
    return 0;
}
