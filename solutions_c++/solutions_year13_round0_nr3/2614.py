//Fruit of Light
//FoL CC
//Apple Strawberry

#include<cstdio>
#include<algorithm>
#include<vector>

using namespace std;

#define For(i, n) for(int i = 0; i<(n); ++i)
#define ForEach(it, i) for(typeof i.begin() it = i.begin(); it!=i.end(); ++it)
#define eps 1e-9

typedef long long ll;
typedef pair<int, int> pii;

bool ispal(ll x){
    //printf("%lld\n", x);
    if (x%10 == 0) return false;
    ll p = x, r =0;
    while(p>0){
        r = r*10 + p%10;
        p/=10;
    }
    return x == r;
}

ll get(ll x){
    int res = 0;
    for(int i = 1; i <= 10000; ++i){
        ll p = i, q = i, a = 0;
        while(p > 0){
            a = a*10 + p%10;
            p/=10;
            q*=10;
        }
        //printf("%lld %lld %lld \n", p, q, a);
        ll b = (q + a)*(q + a);
        q = (q/100)*10;
        ll c = (q + a)*(q + a);
        res+=( b<=x && ispal(b));
        res+=( c<=x && ispal(c));
    }
    return res;
}


ll a,b;

int extra(){
    scanf("%lld %lld",&a, &b);
    // printf("gb %lld\n", get(b));
    printf("%lld\n", get(b) - get(a-1));
}

int main(){
    int T;
    scanf("%d",&T);
    For(i,T){
        printf("Case #%d: ",i+1);
        extra();
    }
}
