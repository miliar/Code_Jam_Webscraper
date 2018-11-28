#include <bits/stdc++.h>
using namespace std;

typedef long long int ll;
typedef long double ld;

#define pb push_back
#define lb lower_bound
#define ub upper_bound
#define mp make_pair

#define trace1(x)							cerr << #x << ": " << x << endl;
#define trace2(x, y)						cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)						cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)       			cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define trace5(a, b, c, d, e)    			cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f) 			cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;

int main(){
	int t;
	cin >> t;
	int cs = 0;
	while (t--) {
		cs++;
		long long n;
		scanf("%lld", &n);
		bool digits[10];
		memset(digits, false, sizeof digits);
		long long curr = n;
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", cs);
			continue;
		}
		while (true) {
			long long temp = curr;
			while (temp > 0) {
				digits[temp % 10] = true;
				temp /= 10;
			}
			bool check = true;
			for (int i = 0; i < 10; i++) {
				check = check && digits[i];
			}
			if (check) break;
			curr += n;
		}
		printf("Case #%d: %lld\n", cs, curr);
	}
}
