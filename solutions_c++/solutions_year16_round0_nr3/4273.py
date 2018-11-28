#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
#define ll long long
#define EPS 1e-7
using namespace std;
int p[10000000];
vector<int>primes;
string binary(int n){
	string s;
	while (n > 0){
		int x = n & 1;
		s += char(x + 48);
		n >>=1;
	}
	reverse(s.begin(), s.end());
	return s;
}
long long fpow(int n, int a){
	long long r = 1, p = a, v = n;
	while (p > 0){
		if (p & 1){
			r *= v;
			r %= 1000000000000000007;
		}
		v *= v;
		v %= 1000000000000000007;
		p /= 2;
	}
	return r;
}
void sieve(){
	p[0] = p[1] = 1;
	for (ll i = 2; i < 10000; ++i){
		if (!p[i]){
			for (ll j = i*i; j>0 && j < 10000000; j += i){
				p[j] = i;
			}
		}
	}
	for (int i = 0; i < 10000000; ++i){
		if (!p[i])
			primes.push_back(i);
	}
}
ll btob(string s, int n){
	ll ans = 0;
	reverse(s.begin(), s.end());
	for (int i = 0; i < s.length(); ++i){
		ans += fpow((s[i] - '0')*n,i);
	}

	return ans;
}
ll check(ll n){
	for (int i = primes.size()-1; i >=0;--i)
	if (n%primes[i] == 0&&n!=primes[i])
		return primes[i];
	return -1;
}
int main(){
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	sieve();
	ll t, n,m,ans=0;
	cin >> t;
	for (int k = 1; k <= t; ++k){
		map<string, vector<int>>v;
		cin >> n>>m;
		ll st = fpow(2, n - 1) + 1;
		for (int i = 0; i < st/2&&m; ++i){
			string s = binary(st + 2 * i);
			int cnt = 0;
			for (int j = 2; j <= 10; ++j)
			{
				ll tmp = btob(s, j);	
				ll x = check(tmp);
				if (x!=-1)
					cnt++;
				else {
					break;
				}
			}
			if (cnt >=9){
				m--;
				for (int j = 2; j <= 10; ++j)
				{
					ll tmp = btob(s, j);
					ll x = check(tmp);
					v[s].push_back(x);
				}
			}
		}

		cout << "Case #" << k << ": " << endl;
		for (map < string, vector<int>>::iterator i = v.begin(); i != v.end(); ++i){
			cout << i->first;
			for (int j = 0; j < i->second.size(); ++j)
			{
				cout << " " << i->second[j];
			}
			cout << endl;
		}
	}

	//system("pause");
}