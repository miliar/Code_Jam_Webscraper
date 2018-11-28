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

int isPrime(ll n){

	for(int i = 2; i < sqrt(n)+5; i++){
		if(n % i == 0) return 0;
	}

	return 1;
}

ll toBase(string s, ll base){
	ll cb = 1;
	ll n = 0;
	for(int i = s.size()-1; i >= 0; i--){
		n += (s[i]-'0')*cb;
		cb *= base;
	}
	return n;
}

int checkSingle(string s, ll base){
	ll n = toBase(s, base);

	return isPrime(n);
}

int check(string s){

	int possible = 1;
	for(int i = 2; i <= 10; i++) {
		if(checkSingle(s, i))
		{
			possible = 0;
			//cout << "wr: " << i << " " << toBase(s, i) << endl;
		}
	}

	return possible;
}


ll findD(ll n){
	for(int i = 2; i < sqrt(n)+5; i++){
		if(n % i == 0) return i;
	}

	return 0;

}

void findDivisorsSingle(string s, ll base){
	ll n = toBase(s, base);
	ll d = findD(n);

	cout << d;
}
void findDivisors(string s){
	for(int i= 2; i <= 10; i++){
		findDivisorsSingle(s, i);
		if(i < 10) cout << " ";
			
	}
}

ll pow2(ll b, ll k){
	ll n = 1;

	for(int i = 0; i < k; i++){
		n*= b;
	}
	return n;
}

string transform(ll n, ll l){

	l-= 3;
	
	l = pow2(2, l);
	ostringstream ss1;
	for(int i = l; i >= 1; i/=2){
		if(n >= i){
			n-= i;
			ss1 << "1";
		} else ss1 << "0";
	}

	string s = ss1.str();

	return s;

}

void run(){
	ll T;
	sc("%lld", &T);
	for(int t = 1; t <= T; t++){
				
		ll N, J;
		cin >> N >> J;

		ll found = 0;

		


		cout << "Case #" << t << ":" << endl;

		ll current = 0;
		while(found < J){
			ostringstream ss;
			ss << "1" << transform(current, N) << "1";

			

			string s = ss.str();

			//cout << current<< endl;
			//cout << s << endl;

			if(check(s)){
				cout << s << " ";

				findDivisors(s);
				cout << endl;
				found++;
			}
			current++;

		}

	}
}

int main() {
	cout << fixed << setprecision(16);

	run();

	return 0;
}
