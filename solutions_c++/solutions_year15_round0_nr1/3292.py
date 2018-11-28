#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int txt = 1;
void solve()
{
    int n,now = 0,t;
    int res = 0;
    char c;
    scanf("%d",&n);
    for(int i = 0 ; i <= n ; i ++){
        scanf(" %c",&c);
        t = c - '0';
        res += max(0,i - now);
        now = max(now,i);
        now += t;
    }
    printf("Case #%d: %d\n",txt ++,res);
}
int main()
{
    freopen("data1.in","r",stdin);
    freopen("data1.out","w",stdout);
    int _;
    scanf("%d",&_);
    while(_--) solve();
    return 0;
}
