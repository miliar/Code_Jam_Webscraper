#include    <bits/stdc++.h>

#define     M_PI            3.14159265358979323846
#define     mod             1000000007
#define     inf             1000000000000000000
#define     mp              make_pair
#define     pb              push_back
#define     F               first
#define     S               second
#define     ll              long long
#define     pii             pair<int,int>
#define     pli             pair<ll,int>
#define     pil             pair<int,ll>
#define     pll             pair<ll,ll>
#define     si(t)           scanf("%d",&t)
#define     sii(m,n)        scanf("%d %d",&m,&n);
#define     sl(t)           scanf("%lld",&t)
#define     rep(i,n)        for(int i=0;i<n;i++)
#define     REP(i,a,b)      for(int i=a;i<=b;i++)
#define     RREP(i,a,b)     for(int i=a;i>=b;i--)
#define     N               100050

using namespace std;

int arr[20];

void fun(ll n){
    while(n != 0){
        arr[n%10]++;
        n /= 10;
    }
}

int chk(){
    rep(i,10){
        if(arr[i] == 0) return 0;
    }
    return 1;
}

int main(){
    int t;
    si(t);
    REP(j,1,t){
        ll n; sl(n);
        if(n == 0){printf("Case #%d: INSOMNIA\n",j); continue;}
        rep(i,10) arr[i] = 0;
        ll k = n;
        while(1){
            fun(k);
            if(chk()) break;
            k+=n;
        }
        printf("Case #%d: %lld\n",j,k);
    }
    return 0;
}