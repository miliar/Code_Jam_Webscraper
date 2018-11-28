#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <utility>

using namespace std;

#define MAXN 100000LL

typedef pair<long long int, long long int> ii;

long int gcd(long long int a, long long int b) { return b == 0 ? a : gcd(b,a%b); }

int main() {
    int T, p, q;
    scanf("%d", &T);
    //printf("%d cases\n", T);
    queue<ii> anc;
    anc.push(ii(1,1));
    anc.push(ii(1,2));
    map<ii,int> dist;
    dist[ii(1,1)] = 0;
    //int generation = 0;
    while(!anc.empty()) {
        //generation++;
        //if(generation > 100) break;
        ii v = anc.front(); anc.pop();
        if(dist[v] > 40) break;
        long long int a, b;
        a = v.first; b = v.second;
        //printf("=====GENERACION %d=====\n", generation);
        //printf("Padre: %d, %d\n", a, b);
        long long int x, y;
        // ancestro v y 0/1
        x = a; y = 2*b;
        long long int factor = gcd(x,y);
        x = x/factor; y = y/factor;
        ii child1 = ii(x,y);
        if(dist.count(child1) == 0) {
            //printf("Genere %d, %d, gcd = %d\n", x, y, gcd(x,y));
            dist[child1] = dist[v] + 1;
            if(x <= MAXN && y <= MAXN)
                anc.push(child1);
        }
        // ancestro v y 1/1
        x = a+b; y = 2*b;
        factor = gcd(x,y);
        x = x/factor; y = y/factor;
        ii child2 = ii(x,y);
        if(dist.count(child2) == 0) {
            //printf("Genere %d, %d, gcd = %d\n", x, y, gcd(x,y));
            dist[child2] = 1;
            if(x <= MAXN && y <= MAXN)
                anc.push(child2);
        }
    }
for(int kase = 1; kase <= T; kase++) {
    scanf("%d/%d", &p, &q);
    long long int factor = gcd(p,q);
    p = p/factor; q = q/factor;
    //printf("p: %d q: %d, gcd(p,q) = %d\n",p,q, factor);
    ii vida = ii(p,q);
    if(dist.count(vida) != 0)
        printf("Case #%d: %d\n", kase, dist[vida]);
    else
        printf("Case #%d: impossible\n", kase);
}
    return 0;
}
