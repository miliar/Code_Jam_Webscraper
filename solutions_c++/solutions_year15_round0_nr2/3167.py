#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
const int N = 1005;
int panc[N],n;
int txt = 1;
void solve(){
    int n,ans = 1001;
    scanf("%d",&n);
    for(int i = 1 ; i <= n ; i ++) scanf("%d",&panc[i]);
    for(int i = 1 ; i <= 1000 ; i ++){
        int res = 0;
        for(int j = 1 ; j <= n ; j ++){
            res += panc[j] / i + (panc[j] % i != 0) - 1;
        }
        res += i;
        ans = min(ans,res);
    }
    printf("Case #%d: %d\n",txt ++,ans);
}
int main()
{
    freopen("data2.in","r",stdin);
    freopen("data2.out","w",stdout);
    int _;
    scanf("%d",&_);
    while(_--) solve();
    return 0;
}
