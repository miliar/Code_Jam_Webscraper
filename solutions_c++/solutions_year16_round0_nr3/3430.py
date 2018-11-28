#include <bits/stdc++.h>
using namespace std;

#ifdef WIN32
    #define lld "%I64d"
#else
    #define lld "%lld"
#endif

#define mp make_pair
#define pb push_back
#define put(x) { cout << #x << " = "; cout << (x) << endl; }

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef double db;

const int M = 1e6 + 15;
const int Q = 1e9 + 7;

                                                    
ll isprime(ll n) {
	for (ll j = 2; 1LL * j * j <= n; j++)
		if (n % j == 0 && j != 1 && j != n)
			return j;
	return -1;

}
int T = 0;
string nxt() {
	string res = "";
	int tmp = T;
	while (tmp)
		res += tmp % 2, tmp /= 10;
	T++;
	reverse(res.begin(), res.end());
	while ((int)res.size() != 14)
		res = '0' + res;
	return res;
}

pair<string, vector<ll> > solve(int n) {
	while (1) {
		string res;
		res += '1';
		for (int i = 0; i < n - 2; i++)
			res += rand() % 2 + '0';
		res += '1';
		vector<ll> x;
		bool ok = true;
		for (int i = 2; i <= 10; i++) {
			ll ch = 0;
			for (int j = 0; j < n; j++) {
				ch = ch * i + res[j] - '0';
			}
			x.pb(isprime(ch));
			if (x.back() == -1) {
				ok = false;
				break;
			}
		}
		if (ok)
			return mp(res, x);
	}
		
}



int main(){
    srand(time(NULL));
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	int TT;
	cin >> TT;
	map<string, bool> was;
	for (int tq = 1; tq <= TT; tq++) {
		int n, j;
		cin >> n >> j;
		cout << "Case #" << tq << ":\n";
		while (j) {
			pair<string, vector<ll> > res = solve(n);
			if (was[res.first]) continue;
			was[res.first] = true;
			j--;
			cout << res.first;
			for (int i = 2; i <= 10; i++)
				cout << " " << res.second[i - 2];
			cout << endl;
			cerr << j << endl;
		}
	}
		
    return 0;
}   