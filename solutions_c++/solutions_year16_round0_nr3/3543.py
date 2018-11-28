#include<cstdio>
#include<vector>
#include<cstring>
#include<algorithm>
using namespace std;
typedef long long LL;
LL Pow[12][20];
int n,J;
int digit[20];
vector<LL> ans;
bool isprime(LL c){
    for(LL i = 2 ; i * i <= c ; i ++)
        if(c % i == 0) return 0;
    return 1;
}
void dfs(int dep){
    if(dep == 0){
        int cnt = 0;
        LL tv;
        for(int base = 10 ; base >= 2 ; base --){
            tv = 0;
            for(int i = 0 ; i < n ; i ++)
                tv += Pow[base][i] * digit[i];
            if(isprime(tv)) return;
            bool ok = 0;
            for(LL i = 2 ; i * i <= tv ; i ++){
                if(tv % i == 0) ok = 1;
            }
            if(ok) cnt ++;
        }
        if(cnt == 9) ans.push_back(tv);
        return;
    }
    if(int(ans.size()) == J) return;
    digit[dep] = 0;
    dfs(dep - 1);
    digit[dep] = 1;
    dfs(dep - 1);
}
void output(LL c){
    if(c == 0) return;
    output(c / 2);
    printf("%I64d",c % 2);
}
void solve(){
    ans.clear();
    scanf("%d%d",&n,&J);
    digit[n - 1] = digit[0] = 1;
    dfs(n - 2);
    for(int i = 0 ; i < J ; i ++){
        output(ans[i]);
        for(int base = 2 ; base <= 10 ; base ++){
            LL tv = ans[i],resv = 0;
            for(int j = 0 ; j < n ; j ++){
                resv += Pow[base][j] * (tv % 2);
                tv /= 2;
            }
            for(LL j = 2 ; j * j <= resv ; j ++){
                if(resv % j == 0){
                    printf(" %I64d",j);
                    break;
                }
            }
        }
        printf("\n");
    }
}
void init(){
    for(int i = 2 ; i <= 10 ; i ++){
        Pow[i][0] = 1;
        for(int j = 1 ; j < 16 ; j ++)
            Pow[i][j] = Pow[i][j - 1] * i;
    }
}
int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    init();
    int _,txt = 1;
    scanf("%d",&_);
    while(_--){
        printf("Case #%d:\n",txt ++);
        solve();
    }
    return 0;
}
