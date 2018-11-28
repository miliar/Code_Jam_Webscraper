#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<iii> viii;
typedef vector<vii> vvii;
typedef set<int> si;
typedef vector<si> vsi;
typedef pair<double, double> dd;

const int inf = 1e9;

ll sieve_size;
vector<ll> bs(100000010, 1); // 10^7 should be enough for most cases
vi primes;

 // create list of primes in [0..upperbound]
void sieve(ll upperbound) {
    sieve_size = upperbound + 1; // add 1 to include upperbound
    bs[0] = 0; bs[1] = 1; // except index 0 and 1
    for (ll i = 2; i <= sieve_size; i++)
        if (bs[i]) {
            // cross out multiples of i starting from i * i!
            for (ll j = i * i; j <= sieve_size; j += i) bs[j] = i;
            primes.push_back(i);
        }
}

int prime(ll n) {
    if (n <= sieve_size) return bs[n];
    for (int i = 0; i < primes.size(); i++)
        if (n % primes[i] == 0) return primes[i];
    return 1;
} // note: only work for n <= (last prime in vi "primes")^2

ll to_base(const string s, int b) {
	ll p = 1;
	ll ans = 0;
	for (int i = s.length() - 1; i >= 0; i--, p *= b)
		ans += (s[i] - '0') * p;
	return ans;
}

map<string, vi> answer;

void solve(string s, int n, int j) {
    if (answer.size() == j)
		return;
    if (s.size() == n) {
        // // cerr << s << endl;
        // cerr << answer.size() << endl;
		for (int b = 2; b <= 10; b++) {
			ll tmp = to_base(s, b);
            // // cerr << b << ' ' << tmp << endl;
			int div = prime(tmp);
            // // cerr << div << endl;
			if (div == 1) {
				answer.erase(s);
				return;
			}
			answer[s].push_back(div);
		}
		return;
	}
	string tmp = s;
	s.insert(1, "0");
    // // cerr << s << endl;
	solve(s, n, j);
	s = tmp;
	s.insert(1, "1");
    // // cerr << s << endl;
	solve(s, n, j);
}

int main() {
	ios::sync_with_stdio(false);

	sieve(100000000); // can go up to 10^7 (need few seconds)

	int ts; cin >> ts;
	for (int t = 1; t <= ts; t++) {
		int n, j; cin >> n >> j;
		string s = "11";
		solve(s, n, j);
        cout << "Case #" << t << ": " << endl;
        for (map<string, vi>::iterator it = answer.begin(); it != answer.end(); it++) {
            cout << it->first;
            for (int i = 0; i < it->second.size(); i++)
                cout << ' ' << it->second[i];
            cout << endl;
        }
	}

	return 0;
}
