#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

bool isprime(ll n) {
	if(n == 1) return false;
	for(ll i = 2; i*i <= n; i++)
		if(n % i == 0) return false;
	return true;
}

bool check(string str) {
	for(int i = 2; i <= 10; i++)
		if(isprime(strtol(str.c_str(), NULL, i)))
			return false;
	return true;
}

ll find_div(ll n) {
	for(ll i = 2; i*i <= n; i++)
		if(n % i == 0) return i;
}

vector<ll> div(string str) {
	vector<ll> divisors;
	for(int i = 2; i <= 10; i++) {
		ll temp = strtol(str.c_str(), NULL, i);
		divisors.push_back(find_div(temp));
	}
	return divisors;
}

int main() {
	cout << "Case #1:" << endl;
	string str;
	int MAXN = (1 << 14) - 1;
	int cnt = 0;
	for(int i = 0; i <= MAXN; i++) {
		bitset<14> bs(i);
		str = '1' + (bitset<14>(i).to_string()) + '1';
		if(check(str)) {
			vector<ll> divisors = div(str);
			cout << str << " ";
			for(int i = 0; i < divisors.size(); i++)
				cout << divisors[i] << " ";
			cout << endl;
			cnt++;
		}
		if(cnt == 50) break;
	}
	return 0;
}