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




void run(){
	ll T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		ll N;
		cin >> N;
		if(N == 0){ cout << "Case #" << t << ": " << "INSOMNIA" << endl; continue;}

		ll i = 1;

		vi vis = vi(15, 0);
		while(true){
			ll c = i*N;

			ostringstream ss;
			ss << c;
			string s = ss.str();			
			
			for(int j = 0; j < s.size(); j++){
				vis[s[j]-'0'] = 1;
			}

			int all = 1;
			for(int j = 0; j <= 9; j++){
				if(!vis[j]) all = 0;
			}

			if(all) break;

			i++;
		}
		
		cout << "Case #" << t << ": " << i*N << endl;
		


	}
	

}

int main() {
	cout << fixed << setprecision(16);

	run();

	return 0;
}
