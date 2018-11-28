#include <bits/stdc++.h>

#define sc(a) scanf("%d", &a)
#define sc2(a, b) scanf("%d%d", &a, &b)
#define fr(a, b, c) for(int (a) = (b); (a) < (c); ++(a))
#define scs(a) scanf("%s", a);
#define rp(a, b) fr(a, 0, b)
#define cl(a,b) memset((a), (b), sizeof(a))

using namespace std;

typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef unsigned long long ull;
typedef long long ll;

ll num[10];

int main() {
    ll t, n, caso = 1;
    scanf("%lld", &t);
    while(t--) {
        cl(num, 0);
        ll cont = 0;
        scanf("%lld", &n);
        ll aux;
        ll j = 1;
        while(cont < 10 && n != 0) {
            aux = j*n;
            while(aux) {
                if(!num[aux%10]) {
                    cont++;
                    num[aux%10] = 1;
                }
                aux /= 10;
            }
            j++;
            if(j > 100000) break;
        }
        if(j > 100000 || !n) printf("Case #%lld: INSOMNIA\n", caso++);
        else printf("Case #%lld: %d\n", caso++, (j-1)*n);
    }
}

