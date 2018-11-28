#include <bits/stdc++.h>
#define sc1(a) scanf("%d", &a)
#define sc2(a, b) scanf("%d%d", &a, &b)
#define sc3(a, b, c) scanf("%d%d%d", &a, &b, &c)
#define sc4(a, b, c, d) scanf("%d%d%d%d", &a, &b, &c, &d)
#define pb(a) push_back(a)
#define inf 0x3f3f3f3f
#define linf 0x3f3f3f3f3f3f3f3fLL
#define fr(i, a, n) for(int i = (a); (i) < (n); ++(i))
#define rp(a, b) fr(a, 0, b)
#define mp(a, b) make_pair(a, b)
#define st first
#define nd second
#define EPS 1e-8
#define clr(a, b) memset(a, b, sizeof(a))
#define addEdge(a, b) to[z] = b; ant[z] = adj[a]; adj[a] = z; z++

using namespace std;
typedef vector<int> vi;
typedef long long int ll;
typedef pair<int, int> pii;
const double PI = acos(-1);

ll v[50];
int qtd;

int main() {
	int t, n, caso = 0;
	
	sc1(t);
	
	while(t--) {
		caso++;
		sc1(n);
		printf("Case #%d: ", caso);
		
		if(!n) {
			printf("INSOMNIA\n");
			continue;
		}
		fr(i, 0, 11) v[i] = 0;
		qtd = 0;
		ll idx = 1, ans;
		while(true) {
			ll aux = n*idx, aux2;
			
			while(aux > 0) {
				aux2 = aux%10;
				aux/=10;
				if(!v[aux2]) qtd++;
				v[aux2]++;
			}
			
			if(qtd == 10) {
				ans = n*idx;
				break;
			}
			
			idx++;
		}
		
		printf("%lld\n", ans);
	}

	return 0;
}




















