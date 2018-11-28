 #include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<ll, ll> ii;
typedef pair<ld, ld> dd;
typedef pair<ll, ll> llll;
typedef vector<ll> vi;
typedef vector<ii> vii;
typedef vector<ll> vll;
typedef vector<llll> vllll;
typedef vector<vi> vvi;
typedef vector<ld> vd;
typedef vector<dd> vdd;
#define INF 1000000000
#define EPS 1e-9
#define rep(i, a, b) for (int i = int(a); i < int(b); i++)
#define contains(x, y) ((x).find(y)!=end(x))
#define mk make_pair
#define pb push_back
#define fst first
#define snd second
#define sz(a) ll((a).size())
#define endl "\n"



ll pow2(ll n, ll e){

	ll r = 1;

	for(int i = 0; i < e; i++){
		r *= n;
	}

	return r;
}

void run(){
	ll T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		ll K, C, S;
		cin >> K >> C >> S;

		ll kc = pow2(K, C);
		ll sl = kc/S;	

		cout << "Case #" << t << ": ";
		for(int i = 0; i < S; i++){
			if(i > 0) cout << " ";
			cout << 1+sl*i;
		}

		 cout << endl;

	}
	

}

int main() {
	cout << fixed << setprecision(16);

	run();

	return 0;
}
