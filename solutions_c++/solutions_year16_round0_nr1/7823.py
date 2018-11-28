#include <iostream>
#include <cstring>
using namespace std;

typedef long long ll;

int digits[10];

int main() {
	int soma, t;
	ll n;
	cin >> t;
	for(int i = 0; i < t; i++) {
		memset(digits, 0, sizeof digits);
		cin >> n;
		cout << "Case #" << i + 1 << ": ";
		if(n == 0)
			cout << "INSOMNIA" << endl;
		else {
			ll original = n;
			int j;
			soma = 0;
			for(j = 1; soma < 10; j++) {
				n = original * j;
				while(n > 0) {
					int digito = n % 10;
					n /= 10;
					digits[digito] = 1;
				}
				soma = 0;
				for(int k = 0; k < 10; k++)
					soma += digits[k];
			}
			cout << original * (j - 1) << endl;
		}
	}
	return 0;
}
