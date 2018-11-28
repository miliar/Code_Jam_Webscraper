#include<bits/stdc++.h>
using namespace std;

#define ll long long

ll a[1000005];

ll find_digits(ll x,ll c[],ll s){
    ll rem;
    while(x){
        rem = x%10;
        x/=10;
        if(!c[rem]){
            c[rem]=1;
            s++;
        }
    }
    return s;
}

int main(){
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    ll i,j; ll c[10]; ll s,x,v;
    for(i=1;i<=1000000;i++){
        for(j=0;j<10;j++)
            c[j]=0;
        s=0; x = i; v = 1;
        while(s!=10){
            s = find_digits(v*x,c,s);
            v++;
        }
        a[i] = (v-1)*i;
    }
    int t; scanf("%d",&t);
    j=1; ll n;
    while(t--){
        scanf("%lld",&n);
        if(n)
            printf("Case #%lld: %lld\n",j,a[n]);
        else
            printf("Case #%lld: INSOMNIA\n",j);
        j++;
    }
    return 0;
}
