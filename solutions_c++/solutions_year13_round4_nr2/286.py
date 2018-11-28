//Fruit of Light
//FoL CC
//Apple Strawberry

#include<cstdio>
#include<algorithm>
#include<vector>
#include<iostream>
#include<set>
#include<map>
#include<queue>
#include<cmath>
#include<cstring>

using namespace std;

#define For(i, n) for(int i = 0; i<(n); ++i)
#define ForEach(it, i) for(typeof i.begin() it = i.begin(); it!=i.end(); ++it)
#define INF 1023456789
#define eps 1e-9

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

ll lucky(ll n, ll p){
    ll m = (1LL<<n);
    ll res = 0;
//    p/=2;
    while(p>1) {
        p/=2;
        m/=2;
        res+=m;
    }
    return res;
}

ll sad(ll n, ll p){
    ll m = (1LL<<n);
    if (p == m) return m-1;
    ll res = 0;
    ll q = 1;
    m/=2;
    p-=m;
    while(p>0) {
        q*=2;
        m/=2;
        p-=m;
        res+=q;
    }
    return res;
}


int extra(){
    ll n, p;
    scanf("%lld %lld",&n,&p);
    printf("%lld %lld\n", sad(n,p), lucky(n,p));
}

int main(){
    int T;
    scanf("%d",&T);
    For(i,T){
        printf("Case #%d: ",i+1);
        extra();
    }
}
