#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<string>
#include<algorithm>
#include<cmath>
#include<vector>
using namespace std;

#define CLR(a,b) memset(a,b,sizeof(a))
const int N = 1000;

double c,f,x;
bool judge(int i)
{
    return 2 * c + ((i + 1) * c - x) * f > 0;
}
double calc(int k)
{
    double ans = 0;
    for(int i = 0 ; i < k ; i++){
        ans += 1.0 / (2 + i * f);
    }
    ans *= c;
    ans += x / (2 + k * f);
    return ans;
}

void solve()
{
    scanf("%lf%lf%lf",&c,&f,&x);
    int l = 0,r = 200001;
    while(l + 1 < r){
        int mid = (l + r) / 2;
        if(judge(mid)) r = mid;
        else l = mid;
    }
    double ans = min(calc(l),calc(r));
    printf("%.7lf\n",ans);
}
int main()
{
   // freopen("BinputLarge.txt","r",stdin);
   // freopen("BoutputLarge.txt","w",stdout);
    int cas = 0;
    int T;
    scanf("%d",&T);
    while(T--){
        cas ++ ;
        printf("Case #%d: ",cas);
        solve();
    }
    return 0;
}
