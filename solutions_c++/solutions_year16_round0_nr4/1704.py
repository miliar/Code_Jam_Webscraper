#include <iostream>
#include <string>

typedef long long ll;
using namespace std;
int main() {
	ll t, test, i, k, c, s;
	cin >> t;
	for (test=1;test<=t;test++) {
		cin >> k >> c >> s;
		ll p=1;
		for (i=0;i<c-1;i++)
			p*=k;

		cout << "Case #" << test << ": ";
		for (i=0;i<s;i++)
			cout << i*p + 1 << " ";
		cout << endl;
	}
	return 0;
}
