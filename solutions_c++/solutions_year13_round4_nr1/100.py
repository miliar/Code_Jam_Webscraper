#include <stdio.h>
#include <algorithm>
using namespace std;
struct abc{
    long long x, p;
    bool operator < (const abc &a) const{
        return x < a.x;
    }
}c[1010], d[1010], _v[1010];
bool cmp(abc a, abc b){
    return a.x > b.x;
}
struct heap{
    int size;
    void push(abc a){
        _v[size++]=a;
        if(size>1)push_heap(_v,_v+size,cmp);
    }
    void pop(){
        pop_heap(_v,_v+size,cmp);
        --size;
    }
    abc top(){return _v[0];}
    void init(){size=0;}
}hp;

long long n, mod = 1000002013ll;
long long f(long long x){
    return ((n + (n - x + 1)) * x / 2) % mod;
}
int main(){
    int T, ri = 1, m, i, j;
    long long ans;
    freopen("A-small-attempt0(2).in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--){
        ans = 0;
        scanf("%lld%d", &n, &m);
        hp.init();
        for (i = 0; i < m; i++){
            scanf("%lld%lld%lld", &c[i].x, &d[i].x, &c[i].p);
            d[i].p = c[i].p;
            ans += f(d[i].x - c[i].x) * c[i].p;
        }
        ans %= mod;
        sort(c, c + m);
        sort(d, d + m);
        j = m - 1;
        for (i = m - 1; i >= 0; i--){
            while (j >= 0 && d[j].x >= c[i].x){
                hp.push(d[j]);
                j--;
            }
            while (c[i].p){
                int pp = min(c[i].p, _v[0].p);
                c[i].p -= pp;
                _v[0].p -= pp;
                ans += mod - (f(_v[0].x - c[i].x) * pp) % mod;
                ans %= mod;
                if (_v[0].p == 0) hp.pop();
            }
        }
        printf("Case #%d: %lld\n", ri++, ans);
    }
    return 0;
}
