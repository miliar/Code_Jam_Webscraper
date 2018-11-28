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
		string s;
		cin >> s;

		char res[1100];
		char buffer[1100];
		ll l = sprintf(res, "")	;	
		for(int i = 0; i < s.size(); i++){
			char c = s[i];
			sprintf(buffer, "%s", res);
			if(l == 0 || c >= res[0]){	
				l = sprintf(res, "%c%s", c, buffer);
			} else {
				l = sprintf(res, "%s%c", buffer, c);
			}
			//printf("Case #%d: %s\n", t, res);
		}

		printf("Case #%d: %s\n", t, res);		


	}
	

}

int main() {
	cout << fixed << setprecision(16);

	run();

	return 0;
}
