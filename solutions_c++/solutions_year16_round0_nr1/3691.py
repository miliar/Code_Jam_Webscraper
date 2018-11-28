#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-largeHai.out","w",stdout);
    ll t,j=1;
    scanf("%lld",&t);
    while(t--){
        ll n;
        scanf("%lld",&n);
        ll arr[10]={0},c=0,r,q,i=1;
        if( n == 0 )
            printf("Case #%lld: INSOMNIA\n",j);
        else{
            while(1){
                ll p = n*i;
                q = p;
                while(p > 0){
                    r = p%10;
                    if(arr[r] == 0){
                        arr[r]++;
                        c++;
                    }
                    p /= 10;
                }
                if( c == 10 )
                    break;
                i++;
            }
            printf("Case #%lld: %lld\n",j,q);
        }
        j++;
    }
}
