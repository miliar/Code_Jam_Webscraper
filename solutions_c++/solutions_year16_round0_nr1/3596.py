#include <bits/stdc++.h>
using namespace std;

int get_digits(long long  n, vector<int>& v) {
	stringstream ss;
	ss << n;
	string s = ss.str();
	for(char c: s) {
		int i = c - '0';
		v[i] = 1;
	}
	return accumulate(v.begin(), v.end(), 0);
}

long long single_test() {
	long long n;
	cin >> n;
	if(n==0) return -1;
	long long  res = n;
	vector<int> v(10, 0);
	while(get_digits(res, v)<10) {
		res +=n;
	}
	return res;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.precision(10);
	cout << fixed;
	int t;
	cin >> t;
	for(int i=1; i<=t; ++i) {
		long long res = single_test();
		if(res>=0) {
			cout << "Case #" << i << ": " << res << endl;
		} else {
			cout << "Case #" << i << ": INSOMNIA" << endl;
		}
	}
	return 0;
}
