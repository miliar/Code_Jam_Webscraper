#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
typedef long long LL;
int digit[11];
void solve(){
    LL n;
    scanf("%I64d",&n);
    if(n == 0){
        printf("INSOMNIA\n");
        return;
    }
    int cnt = 10000;
    LL res = 0,nn = n;
    for(int i = 0 ; i < 10 ; i ++) digit[i] = 1;
    while(1){
        LL tn = nn;
        while(tn){
            res += digit[tn % 10];
            digit[tn % 10] = 0;
            tn /= 10;
        }
        if(res == 10) break;
        nn += n;
    }
    printf("%I64d\n",nn);
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int _,txt = 1;
    scanf("%d",&_);
    while(_--){
        printf("Case #%d: ",txt ++);
        solve();
    }
    return 0;
}
