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
#define sc scanf



void run(){
	ll T;
	sc("%lld", &T);
	for(int t = 1; t <= T; t++){
		char s[110];
		sc("%s", s);
		ll l = sprintf(s, "%s", s);

		char c = s[0];
		
		ll sum = 0;
		for(int i = 1; i < l; i++){
			if(s[i] != c){
				c = s[i];
				sum++;
			}
		}

		if(c == '-') sum++;

		cout << "Case #" << t << ": " << sum << endl;

	}
	

}

int main() {
	cout << fixed << setprecision(16);

	run();

	return 0;
}
