#include<bits/stdc++.h>
using namespace std;

bool is_prime(long long x) {
	if (x == 2)
		return 1;
	for (long long i = 2; i * i <= x; i += (i & 1) + 1) {
		if (x % i == 0)
			return 0;
	}
	return 1;
}

long long convert(string s, long long b) {
	long long len = s.length();
	long long res = 0;
	long long tb = 1;
	for (long long i = len - 1; i >= 0; i--) {
		res += (s[i] - '0') * tb;
		tb *= b;
	}
	return res;
}

long long get_div(long long x) {
	for (long long i = 2; i * i <= x; i += (i & 1) + 1) {
		if (x % i == 0)
			return i;
	}
	return -1;
}

int main() {
	freopen("test.txt", "rt", stdin);
	freopen("o.txt","wt",stdout);

	ios::sync_with_stdio(false);

	long long test;
	cin >> test;
	long long n, len;
	cin >> n >> len;
	cout << "Case #1:" << endl;
	for (long long i = (1 << (n - 1)); i < (1 << n); i++) {
		string s = "";
		for (long long j = n-1; j >=0; j--)
			if ((i & (1 << j)))
				s += '1';
			else
				s += '0';
		if(s[n-1] != '1') continue;
//		cout << i << " " << s << endl;
		bool x = 0;
		vector<long long> v;
		for (long long j = 2; j <= 10; j++) {
//			cout<<s<<" "<<j<<" "<<convert(s,j)<<endl;
			v.push_back(convert(s, j));
			x |= is_prime(v.back());
		}
//		cout<<i<<" "<<s<<" "<<x<<endl;
		if (!x) {

			cout<<s;
			for(long long j=0;j<9;j++){
				cout<<" "<<get_div(v[j]);
			}
			cout<<endl;
			len--;
		}
		if (!len)
			break;
	}

	return 0;
}
