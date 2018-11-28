#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;
typedef vector <ll> VI;

const ll M = 1e15;

VI X;
ll cont;

VI E, P;

ll lol(ll k){
	ll res = 0;
	for (int i = 0; i < (int) X.size(); ++i){
		res += X[i];
		res *= k;
		if (res > M) return M;
	}
	return res;
		
}

void check(){
	ll c = P.size();
	VI sol = VI(0);
	for (ll k = 2; k <= 10; ++k){
		ll f = lol(k);
		for (ll i = 2; i < c && P[i]*P[i] <= f; ++i){
			ll res = 0;
			for (ll j = 0; j < (ll) X.size(); ++j){
				res*=k;
				res += X[j];
				res %= P[i];
			}
			if (res == 0){
				sol.push_back(P[i]);
				//cout << "hh" << endl;
				break;
			}
		}
	}	
	if (sol.size() == 9){
		++cont;
		bool started = false;
		for (ll i = 0; i < (ll) X.size(); ++i){
			cout << X[i];
		}
		cout << " ";
		for (ll i = 0; i < 9; ++i){
			if (started) cout << " ";
			started = true;
			cout << sol[i];
		}
		cout << endl;
	}		
}

void Backtracking(ll z, ll N, ll J){
	if (cont >= J) return;
	if (z == N-1){
		//for (ll i = 0; i < (ll) X.size(); ++i){
			//cout << X[i];
		//}
		//cout << endl;
		check();
		return;
	}
	Backtracking(z+1, N, J); 
	X[z] = 1;
	Backtracking(z+1, N, J);
	X[z] = 0;
}


int main(){
	ll C = 1000000;
	E = VI(C, 1); P = VI(0);
	for (ll i = 2; i < C; ++i){
		if (E[i] == 1){
			for (ll j = i; j*i < C; ++j) E[i*j] = 0;
			P.push_back(i);
		}
	}
	//cout << P.size() << endl;
	//for (int i = 0; i < 10; ++i) cout << P[i] << " ";
	//cout << endl;
	ll T;
	cin >> T;
	for (ll k = 0; k < T; ++k){
		cout << "Case #" << k+1 << ":" << endl;
		ll N, J;
		cin >> N >> J;
		X = VI(N, 0);
		X[0] = X[N-1] = 1;
		cont = 0;
		Backtracking(1,N,J);
	}
}
