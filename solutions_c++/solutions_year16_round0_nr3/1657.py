/*
        By: facug91
        From: 
        Name: 
        Date: 09/04/2016
*/

#include <bits/stdc++.h>
#define endl "\n"
#define EPS 1e-9
#define MP make_pair
#define F first
#define S second
#define DB(x) cerr << " #" << (#x) << ": " << (x)
#define DBL(x) cerr << " #" << (#x) << ": " << (x) << endl
const double PI = acos(-1.0);

#define INF 1000000000
//#define MOD 1000000007ll
#define MAXN 100000005

using namespace std;
typedef long long ll;
typedef unsigned long long llu;
typedef pair<int, int> ii; typedef pair<ii, ii> iiii;
typedef vector<int> vi; typedef vector<ii> vii; typedef vector<iiii> viiii;

ll n, j;
string s;
vector<ll> primes;
bool sieve[200000005];

bool isProbablyPrime (ll base) {
	ll ip = 0, p = primes[ip], val;
	while (ip < 1000) {
		val = 0;
		for (int i=0; i<n; i++) val = (val * base + ((s[i] == '0') ? 0ll : 1ll)) % p;
		if (val == 0ll) return false;
		p = primes[++ip];
	}
	return true;
}

ll firstDivisor (ll base) {
	ll ip = 0, p = primes[ip], val;
	while (ip < 1000) {
		val = 0;
		for (int i=0; i<n; i++) val = (val * base + ((s[i] == '0') ? 0ll : 1ll)) % p;
		if (val == 0ll) return p;
		p = primes[++ip];
	}
	return -1;
}

int main () {
	#ifdef ONLINE_JUDGE
		ios_base::sync_with_stdio(0); cin.tie(0);
	#endif
	//cout<<fixed<<setprecision(3); //cerr<<fixed<<setprecision(3); //cin.ignore(INT_MAX, ' '); //cout << setfill('0') << setw(5)
	
	for (int i=1; i<MAXN; i+=2) sieve[i] = true;
	for (int i=3; i<10005; i+=2)
		if (sieve[i])
			for (int k=i*i; k<MAXN; k+=i+i)
				sieve[k] = false;
	primes.push_back(2);
	for (int i=3; i<MAXN; i+=2)
		if (sieve[i])
			primes.push_back(i);
	n = 32ll;
	j = 500ll;
	s = "10000000000000000000000000000000"; // 16 digits
	cout<<"Case #1:"<<endl;
	while (j) {
		if (s[n-1] == '1') {
			bool jamcoin = true;
			for (int i=2; i<=10; i++)
				if (isProbablyPrime(i)) jamcoin = false;
			if (jamcoin) {
				cout<<s;
				for (int i=2; i<=10; i++)
					cout<<" "<<firstDivisor(i);
				cout<<endl;
				j--;
			}
		}
		int carry = 1;
		for (int i=n-1; i>=0; i--) {
			if (s[i] == '0') {
				if (carry == 1) {
					s[i] = '1';
					carry = 0;
				}
			} else {
				if (carry == 1) s[i] = '0';
			}
		}
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	return 0;
}
