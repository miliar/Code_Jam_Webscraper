#include <iostream>
#include <cstdio>
#include <cmath>
#define LL long long
#define LD long double
#define SIZE 18765432

using namespace std;

LL n, T, z, ans, temp, k, q, a, b, i, j, w[SIZE];
LD fa, fb;

int main() {

#if 1
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
#endif

	for (i = 1; i <= 10000000; i++) {
		temp = i;
		q = 0;
		while (temp > 0) {
			q = q * 10 + temp % 10;
			temp /= 10;
		}
		if (q == i) {
			q = 0;
			temp = i * i;
			while (temp > 0) {
				q = q * 10 + temp % 10;
				temp /= 10;
			}
//			cout<<i * i<<" =/= "<<q<<endl;
			if (q == i * i) {
//				cout<<i<<" "<<w[i - 1]<<endl;
				w[i]++;
			}
		}
		w[i] += w[i - 1];
	}
	cin>>T;
	for (z = 1; z <= T; z++) {
		cin>>a>>b;
		fa = sqrt(a);
		fb = sqrt(b);
		b = (int) fb;
		if (1.0 * ((int) fa) == fa) a = (int) fa;
		else a = (int) fa + 1;
		ans = w[b] - w[a - 1];
		cout<<"Case #"<<z<<": "<<ans<<endl;
	}
	return 0;
}
