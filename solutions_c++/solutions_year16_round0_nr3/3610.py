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

ll arr[10];
int n,jj;

ll power(int a,int b){
    ll ans = 1;
    rep(i,b){
        ans *= a;
    }
    return ans;
}

ll chk(int a,int b){
    ll num=0;
    rep(i,n){
        if((1<<i) & a){
            num += power(b,i);
        }
    }
    ll k = (ll)sqrt(num);
    for(ll i=2;i<=k;i++){
        if(num%i ==0 ) return i;
    }
    return -1;
}

void print(ll a){
    for(int i=n-1;i>=0;i--){
        if((1<<i) & a){
            printf("1");
        }
        else printf("0");
    }
    printf(" ");
}

int main(){
    int t; si(t);
    sii(n,jj);
    ll k = 1<<n;
    printf("Case #1:\n");
    int c=0;
    for(ll i = (1<<(n-1))+1; i<k ; i+= 2){
        int f=0,h=0;
        REP(j,2,10){
            ll p = chk(i,j);
            if(p == -1) {f=1 ; break; }
            arr[h++] = p;
        }
        if(!f){
            c++;
            print(i);
            rep(j,h) printf("%lld ",arr[j]);
            printf("\n");
            if(c == jj) break;
        }
    }
    return 0;
}