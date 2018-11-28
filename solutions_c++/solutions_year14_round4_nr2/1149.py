#include <bits/stdc++.h>
using namespace std;
#define fr(i,a,b) for(int i = a; i < b; ++i)
#define rep(i, n) fr(i,0,n)
#define _(n) rep(i, n)
#define mp make_pair
#define ft first
#define sd second
#define pb push_back
typedef pair<int,int> pii;
typedef long long ll;
typedef unsigned long long hash;
typedef vector<int> VI;

int n;
vector<int> num;

ll toNum(VI& seq){
	ll ans = 0;
	for(int a : seq) ans = ans * n + a;
	return ans;
}

VI fromNum(ll num){
	VI ans(n);
	_(n) ans[n-1-i] = num%n, num /= n;
	return ans;
}

bool eh(VI &aux){
	if(aux.size()==1) return true;

	int j = 1;
	while(aux[j] > aux[j-1]) ++j;

	while(j + 1 < n){
		if(aux[j] < aux[j+1]) return false;
		++j;
	}

	return true;
}


map<ll, int> mapa;

int dij(VI seq){
	mapa.clear();
	queue<ll> fila;
	fila.push(toNum(seq));
	mapa[fila.front()] = 0;

	while(!fila.empty()){
		ll cod = fila.front();
		fila.pop();
		seq = fromNum(cod);

		if(eh(seq)) return mapa[cod];
		int d = mapa[cod];

		fr(i, 0, n-1){
			VI aux = seq;
			swap(aux[i], aux[i+1]);
			ll ncod = toNum(aux);
			auto it = mapa.find(ncod);
			if(it != mapa.end()) continue;
			mapa[ncod] = d+1;
			fila.push(ncod);
		}
	}
}

int main(){
	ios::sync_with_stdio(false);
	int t;
	cin >> t;

	for(int tt = 1; tt <= t; ++tt){
		cin >> n;
		num.clear();
		_(n){
			int tmp;
			cin >> tmp;
			num.pb(tmp);
		}
		{
			VI aux = num;
			sort(aux.begin(), aux.end());
			_(n) num[i] = find(aux.begin(), aux.end(), num[i]) - aux.begin();
		}
		int best = dij(num);

		cout << "Case #" << tt << ": " << best << endl;
	}
}
