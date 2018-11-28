#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;
typedef long long ll;

void next(string& s)
{
	int index = s.size() - 2;
	while (s[index] == '1') {
		s[index] = '0';
		--index;
	}
	s[index] = '1';
}

ll translate_to_base(const string& s, int base)
{
	ll p  = 1;
	ll num = 0;
	for (int i = s.size() - 1; i >= 0; --i) {
		num += p * (s[i] - '0');
		p *= base;
	}
	return num;
}

ll prime_tester(ll n)
{
	for (ll i = 2; i <= ceil(sqrt(static_cast<long double>(n))); ++i) {
		if (n % i == 0) {
			return i;
		}
	}
	return -1;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	cout << "Case #1:"<< endl;
	int n, k;
	cin >> n >> k;
	string s = "1";
	for (int i = 0; i < n - 2; ++i) {
		s.push_back('0');
	}
	s.push_back('1');
	ll ans[11];
	for (int t = 0; t < k; ++t) {

		int found = 0;
		while (found != 9) {
			for (int j = 2; j <= 10; ++j) {
				ll num = translate_to_base(s,  j);
				ll test = prime_tester(num);
				if (test != -1) {
					++found;
					ans[j] = test;
				} else {
					break;
				}
			}

			
			if (found != 9) {
				found = 0;
			} else {
				cout << s << " ";
				for (int i = 2; i <= 10; ++i) {
					//cout << " >> translate to " << i << "  " << translate_to_base(s, i) << " <<  test is " << prime_tester(translate_to_base(s, i)) << "  " ;
					cout << prime_tester(translate_to_base(s, i)) << " ";
				}
				cout << endl;
			}
			next(s);
		}
	}

	return 0;
}