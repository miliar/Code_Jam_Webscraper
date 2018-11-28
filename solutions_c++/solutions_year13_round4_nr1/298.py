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
#include<stack>

using namespace std;

#define For(i, n) for(int i = 0; i<(n); ++i)
#define ForEach(it, i) for(typeof i.begin() it = i.begin(); it!=i.end(); ++it)
#define INF 1023456789
#define eps 1e-9
#define MOD 1000002013LL

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;


int extra(){
    int n, m, a, b, c;
    vector<pll> E;
    ll pocena = 0;
    scanf("%d %d",&n, &m);
    For(i,m) {
        scanf("%d %d %d", &a, &b, &c);
        E.push_back(pii(a,-c));
        E.push_back(pii(b,c));
        ll posun = b-a;
        pocena+= ((ll(n)*posun - (posun*(posun-1))/2)%MOD)*c;
        pocena%=MOD;
    }
    sort(E.begin(), E.end());
    ll prevz = 0;
    stack<pll> veci;
    For(i, E.size()){
        ll z = E[i].first;
        ll delta = -E[i].second;
        if (delta>0) veci.push(pll(z, delta));
        else {
            while (delta<0) {
                while (!veci.empty() && veci.top().second==0) veci.pop();
                ll take = min(-delta, veci.top().second);
                ll posun = z-veci.top().first;
                pocena -= ((ll(n)*posun - (posun*(posun-1))/2)%MOD)*take;
                pocena%=MOD;
                veci.top().second-=take;
                delta+=take;
            }
        }        
    }
    pocena = (pocena%MOD+2LL*MOD)%MOD;
    printf("%lld\n",pocena);
}

int main(){
    int T;
    scanf("%d",&T);
    For(i,T){
        printf("Case #%d: ",i+1);
        extra();
    }
}
