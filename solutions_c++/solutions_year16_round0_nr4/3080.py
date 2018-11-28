#include<bits/stdc++.h>
using namespace std;
typedef unsigned long long int ll;
ll f(ll a,ll b){
    if(b == 0)
        return 1;
    ll temp = f(a,b/2);
    if(b&1)
        return temp*temp*a;
    return temp*temp;
}
int main(){
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-smallHai.out","w",stdout);
    ll t,j=1;
    scanf("%lld",&t);
    while(t--){
        ll k,c,s,i,term=1;
        scanf("%lld%lld%lld",&k,&c,&s);
        ll c_d = f(k,c-1);
        printf("Case #%llu: ",j);
        for( i=0; i<k; i++ ){
            printf("%llu ",term);
            term = term+ c_d;
        }
        printf("\n");
        j++;
    }
    return 0;
}
