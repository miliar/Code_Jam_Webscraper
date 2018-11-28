#include <bits/stdc++.h>

using namespace std;

#define FOR(i,a,b) for(int i = a; i < b; i++)
#define FORR(i,b) FOR(i, 0, b)
#define sz(e) (int)e.size()
#define CLR(x,v) memset (x, v, sizeof x)
#define pb push_back
#define all(e) e.begin(), e.end()

typedef long long ll;
typedef pair<int, int> ii;

const int MAXN = 100005;
const int INF = 1000000000;

vector<double> bag;
double PD[250][250];

double calc (int x, int yes) {
	if (x==sz(bag)) return (yes==(sz(bag)/2) ? 1. : 0.);
	if (PD[x][yes]<0) {
		PD[x][yes] =  bag[x] * calc (x+1, yes+1) + (1. - bag[x]) * calc (x+1, yes); 
	}
	return PD[x][yes];
}	

double vet[MAXN];

int main () {
	int T;
	cin>>T;
	FORR (c, T) {
		cout << "Case #" << c+1 << ": ";
		int N, K;
		cin>>N>>K;
		FORR (i, N) {
			cin>>vet[i];
		}
		sort (vet, vet+N);
		double ans = 0.;
		int melhor = 0;
		FORR (i, K+1) {
			/*bag.clear();
			FORR (j, N) {
				if ((1<<j) & i) bag.pb (vet[j]);
			}
			if (sz(bag)!=K) continue;*/
			
			FORR (j, N+1) FORR (k, N+1) PD[j][k] = -1.;
			
			bag.clear();
			int aux = 0;
			FORR (j, i) {
				bag.pb (vet[j]), aux |= 1<<j;
			}
			FOR (j, i, K) {
				bag.pb (vet[N-j-1+i]), aux |= 1<<(N-j-1+i);
			}
			sort (all(bag));
			/*while (aux) {
				cout << (aux&1);
				aux>>=1;
			} cout << endl;*/
			if (calc(0,0) > ans) melhor = aux; 
			//cout << sz(bag) << endl;
			
			//if (calc(0,0) > ans) melhor = i; 
			ans = max (ans, calc(0,0));
		}
		
		/*while (melhor) {
			//cout << "aqui" << endl;
			cout << (melhor&1);
			melhor>>=1;
		} cout << endl;*/
		//FORR (i, sz(bag)) cout << i << " " << bag[i] << endl;
		//cout << calc (1, 0) << endl;
		cout << setprecision(12) << fixed << ans << endl;
	}
}
