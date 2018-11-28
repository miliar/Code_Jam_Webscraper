#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int x[15];

void P(ll n){
    while(n > 0){
        x[n % 10] = 1;
        n /= 10;
    }
}

int Yes(){
    int ret = 0;
    for(int i=0;i<=9;i++) ret += x[i];
    return (ret == 10);
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large-out","w",stdout);
    int test,no = 0; scanf("%d",&test);
    while(test--){
        ll n; scanf("%lld",&n);
        memset(x , 0 , sizeof x);
        if(n == 0){
            printf("Case #%d: INSOMNIA\n",++no);
        }else {
            for(ll a = 1;  ; a++){
                P(a * n);
                if(Yes()){
                    printf("Case #%d: %lld\n",++no,a * n);
                    break;
                }
            }
        }
    }
    return 0;
}
