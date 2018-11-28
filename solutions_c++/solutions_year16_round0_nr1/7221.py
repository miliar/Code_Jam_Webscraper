#include <bits/stdc++.h>
using namespace std;

int main() {
	int t,r;
	cin >> t;
	for (r = 1; r <= t; r++) {
		long long int n,a,b,k,g,i,s,f=0;
		map <long long int, long long int > m;
		cin >> n;
		a = n;
		if (a == 0) g = 0;
		else g=log10(a);
		k=a;
		for (i = 0; i <= g; i++) {
			s = k%10;
			if (m[s] == 0) {
				m[s] = 1;
			}
			k = k/10;
		}
		b = 2*n;
		if (b == 0) g = 0;
		else g=log10(b);
		k=b;
		for (i = 0; i <= g; i++) {
			s = k%10;
			if (m[s] == 0) {
				m[s] = 1;
			}
			k = k/10;
		}
		while (a != b) {
			if (m.size() == 10) {
				f = 1;
				break;
			}
			a = a+n;
			b = b+n;
			if (b == 0) g = 0;
			else g=log10(b);
			k=b;
			for (i = 0; i <= g; i++) {
				s = k%10;
				if (m[s] == 0) {
					m[s] = 1;
				}
				k = k/10;
			}
		}
		if (f == 0) 
			cout << "Case #" << r << ": " << "INSOMNIA" << endl;
		else
			cout << "Case #" << r << ": " << b << endl;
	}
	return 0;
}
