#include <vector>
#include <string>
#include <cstring>
#include <cstdio>
#include <map>
#include <algorithm>

#define ll long long 
using namespace std;
ll gcd(ll x, ll y){
    ll tmp = y%x;
    while(tmp){
        y = x;
        x = tmp;
        tmp = y%x;
    }
    return x;
}

int main(){
    int T;
    long long  P, Q;
    scanf("%d", &T);
    for(int i = 1; i <= T; i++){
        printf("Case #%d: ", i);
        scanf("%lld/%lld", &P, &Q);
        if(P > Q){
            printf("impossible\n");
            continue;
        }
        int div = gcd(P, Q);
        P /= div; Q/=div;
       if(Q&(Q-1)){
            printf("impossible\n");
            continue;
       }
        int num = 0, len = 0;
        while(P >= 2<< num){
            num++;
        }
        while(Q>= 2<<len)
            len++;
        printf("%d\n", len- num);
    }
    return 0;
}
