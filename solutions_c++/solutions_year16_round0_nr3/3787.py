#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<ctime>
#include<cctype>
#include<climits>
#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<list>
#include<queue>
#include<fstream>
#include<deque>
#include<algorithm>
#include<numeric>
#include<utility>
#include<complex>
#include<memory>
#include<functional>

using namespace std;

#define all(g) (g).begin(),(g).end()
#define REP(i, x, n) for(int i = x; i < n; i++)
#define rep(i,n) REP(i,0,n)
#define F(i,j,k) fill(i[0],i[0]+j*j,k)
#define P(p) cout<<(p)<<endl;
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define INF (1<<28)
#define pb push_back

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<long long> vl;
typedef vector<double> vd;
typedef pair<int, int> pii;
typedef pair<long, long> pll;
typedef long long ll;

int gcd(int a, int b) {
	if (b == 0) return a;
	return gcd(b, a % b);
}

int lcm(int a, int b) {
	return a / gcd(a, b) * b;
}

int extgcd(int a, int b, int& x, int& y) {
	int d = a;
	if (b != 0) {
		d = extgcd(b, a % b, y, x);
		y -= (a / b) * x;
	}
	else {
		x = 1; y = 0;
	}
	return d;
}

bool is_prime(ll n) {
	for (ll i = 2; i * i <= n; i++) {
		if (n % i == 0) return false;
	}
	return n != 1;
}

vector<int> divisor(int n) {
	vector<int> res;
	for (int i = 1; i * i <= n; i++) {
		if (n % i == 0) {
			res.pb(i);
			if (i != n / i) res.pb(n / i);
		}
	}
	return res;
}

map<int, int> prime_factor(int n) {
	map<int, int> res;
	for (int i = 2; i * i <= n; i++) {
		while (n % i == 0) {
			++res[i];
			n /= i;
		}
	}
	if (n != 1) res[n] = 1;
	return res;
}

const int MAX_N = 10000000;
int prime[MAX_N];
bool memo[MAX_N + 1];

ll t_pow(ll a, ll b) {
	ll ret = 1;
	rep(i, b) ret *= a;
	return ret;
}
ll mod_pow(ll x, ll n, ll mod) {
	if (n == 0) return 1;
	ll res = mod_pow(x * x % mod, n / 2, mod);
	if (n & 1) res = res * x % mod;
	return res;
}

int binary(int bina) {
	int ans = 0;
	for (int i = 0; bina>0; i++)
	{
		ans = ans + (bina % 2)*t_pow(10, i);
		bina = bina / 2;
	}
	return ans;
}
string to_binString(unsigned int val)
{
	if (!val)
		return std::string("0");
	std::string str;
	while (val != 0) {
		if ((val & 1) == 0)  // val ‚Í‹ô”‚©H
			str.insert(str.begin(), '0');  //  ‹ô”‚Ìê‡
		else
			str.insert(str.begin(), '1');  //  Šï”‚Ìê‡
		val >>= 1;
	}
	return str;
}
ll trans(string a, int num) {
	ll ret = 0;
	int n = a.length();
	for (int i = 0; i < a.length(); i++) {
		ret += ll((int)a[n-1-i]-(int)'0')*t_pow(num, i);
	}
	return ret;
}
ll first_devide(ll n) {
	for (ll i = 2; i * i <= n; i++) {
		if (n % i == 0) return i;
	}
	return n;
}
int main() {
	
	int T, N, J;
	cin >> T >> N >> J;
	set<ll> primes;
	ofstream output("C_small.txt");
	int ans = 0;
	output << "Case #1:" << endl;
	for (int i = 0; i < (1 << (N - 2)); i++){
		bool flag = true;
		string a = to_binString(i);
		while(a.size() < N - 2)a = "0" + a;
		a = "1" + a;
		a += "1";
		REP(j, 2, 11) {
			ll b = trans(a, j);
			if (is_prime(b)) {
				flag = false;
				break;
			}
		}
		if (flag) {
			ans++;
			output << a << " ";
			REP(j, 2, 11) {
				ll b = trans(a, j);
				cout << j << " b is " << b<<endl;
				ll c = first_devide(b);
				if (j == 10) {
					output << c << endl;
				}
				else {
					output << c << " ";
				}
			}
		}
		if (ans == J) break;
	}

	return 0;
}
