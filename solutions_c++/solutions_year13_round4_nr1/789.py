#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <sstream>
using namespace std;
typedef vector<string> vs;
typedef vector<int> vi;
typedef long long ll;
typedef pair<int,int> pii;
#define sz(A) (int)(A).size()
#define FOR(A,B) for(long long A=0; A < (long long) (B);A++)
#define FOREACH(I,C) for(__typeof(C.begin()) I = (C).begin(); I != (C).end(); I++)
#define pb push_back
#define all(x) x.begin() , x.end()
#define mp make_pair

#define MAX 128

long long mod = 1000002013;
long long N, M;
map<long long, long long> entra, sai;
set<ll> ind;

long long PA(long long x) {
	return ((1 + x) * x / 2) % mod;
}

long long opt_cost() {
	long long cost = 0;
	map< ll,ll > in;
	FOREACH(k, ind) {
		long long i = *k;
		in[-i] += entra[i];
		while(sai[i]) {
			long long entrou = -(*in.begin()).first;
			long long qtd = (*in.begin()).second;
			long long dist = i - entrou;

			long long pessoas = min(qtd, sai[i]);
			sai[i] -= pessoas;
			in[-entrou] -= pessoas;
			if (in[-entrou] == 0) in.erase(in.begin());

			long long paga = ((dist * N - PA(dist))) % mod * pessoas;
			cost += paga;
			cost %= mod;
		}
	}
	return cost;
}

void solve() {
	cin >> N >> M;
	entra.clear(); sai.clear(); ind.clear();
	long long ini, fim, p;
	long long normal = 0;
	FOR(i, M) {
		cin >> ini >> fim >> p;
		entra[ini] += p;
		sai[fim] += p;
		ind.insert(ini); ind.insert(fim);
		long long dist = fim - ini;
		if (dist != 0) {
			normal += ((((ll) dist * N - PA(dist))) % mod) * p;
			normal %= mod;
		}
	}
	// cerr << "NORM = " << normal << endl;
	long long opt = opt_cost();
	// cerr << "OPT = " << opt << endl;

	long long res = ((normal - opt) + mod) % mod;
	cout << res << endl;
}

int main() {
  int num_testes;
  scanf("%d", &num_testes);
  for(int t = 1; t <= num_testes; t++) {
    printf("Case #%d: ", t);
    solve();
  }
  return 0;
}
