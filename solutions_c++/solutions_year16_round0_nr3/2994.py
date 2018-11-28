#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <numeric>
#include <bitset>

using namespace std;

#define FOR(i, n) for(int i = 0; i < (n); ++i)
#define SIZEOF(a) (sizeof(a)/sizeof((a)[0]))

typedef long long ll;

const int MAX_N = 1e6+10;
int a[MAX_N];

const ll SQRT_MAXN = 1e8; // корень из максимального значения N
const ll S = 1e7;
bool nprime[SQRT_MAXN], bl[S];
ll primes[SQRT_MAXN], cnt;
set<ll> pr;

int precalc_primes(ll n) {
	ll nsqrt = (ll) sqrt (n + .0);
	for (ll i=2; i<=nsqrt; ++i)
		if (!nprime[i]) {
			primes[cnt++] = i;
			if (i * 1ll * i <= nsqrt)
				for (int j=i*i; j<=nsqrt; j+=i)
					nprime[j] = true;
		}
 
	for (ll k=0, maxk=n/S; k<=maxk; ++k) {
		memset (bl, 0, sizeof bl);
		ll start = k * S;
		for (ll i=0; i<cnt; ++i) {
			ll start_idx = (start + primes[i] - 1) / primes[i];
			ll j = max(start_idx, 2LL) * primes[i] - start;
			for (; j<S; j+=primes[i])
				bl[j] = true;
		}
		if (k == 0)
			bl[0] = bl[1] = true;
		for (ll i=0; i<S && start+i<=n; ++i)
			if (!bl[i])
				pr.insert(i);
	} 
}

int N, J;

vector<int> GetBin(int x){
	vector<int> v;
	while(x){
		v.push_back(x&1 ? 1 : 0);
		x /= 2;
	}
	return v;
}

ll GetBase(const vector<int>& v, int base){
	ll res = 0;
	ll b = 1;
	for (int i = 0; i < v.size(); ++i)
	{
		res += v[i] * b;
		b *= base;
	}
	return res;
}

vector<int> v;
ll bases[20];
ll divisors[20];

bool printBin(const vector<int>& v){
	const size_t n = v.size();
	FOR(i,n) cout << v[n-1-i];
}

bool is_jc(const vector<int>& v){
	for(int b=2; b<=10; b++){
		const ll x = GetBase(v, b);
		bases[b] = x;
		//if(pr.count(x))	return false;
	}
	return true;
}

int divisor(const ll n){
	for(ll i = 2LL; i*i <= n; ++i){
		if(n % i == 0)
			return i;
	}
	return -1;
}

bool has_div(const vector<int>& v)
{
	for(int b=2; b<=10; b++){
		const int d = divisor(bases[b]);
		if(d <= 0) return false;
		divisors[b] = d;
	}
	return true;
}

int SolveCase()
{
	cout << endl;
	const int n = 1<<(N-2);
	const int mask = (1<<(N-1)) | 1;
	//cout << bitset<32>(n) << endl;
	//cout << bitset<32>(mask) << endl;
	//cout << endl;
	int cnt = 0;
	for(int i=0; i < n && cnt < J; ++i){
		const int curr = (i<<1) | mask;
		//cout << curr << endl;
		v = GetBin(curr);
		if(!is_jc(v)) continue;
		if(!has_div(v)) continue;
		++cnt;
		printBin(v);
		for(int b=2; b<=10; b++){
			cout << " " << divisors[b];
			//cout << "(" << bases[b] << ")";
		}
		cout << endl;
	}//*/
}

int main()
{
	//test();return 0;
	//precalc_primes(1e7);
	int t; cin >> t;
	FOR(i,t){
		cin >> N >> J;
		cout << "Case #" << i+1 << ": ";
		SolveCase();
		cout << endl;
	}
	return 0;
}
