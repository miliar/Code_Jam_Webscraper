/*mohitmangnani*/
#include<bits/stdc++.h>

#define ll long long int
#define pb push_back
#define mp make_pair
#define s(x) scanf("%lld", &x)
#define SET(x, a) memset(x, a, sizeof(x));
#define trace(x) cerr << #x << ": " << x << endl;
#define trace2(x, y) cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z) cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;

using namespace std;

int main()
{
	ll test,max_shy;
	s(test);

	for (int t = 1; t <= test; t++) {
		string s;
		s(max_shy);
		cin >> s;

		ll friends,standing,res;

		standing = s[0] - '0';
		res = 0;
		
		for (int i = 1; i < max_shy + 1; i++) {
			if (s[i] != '0') {
				if (standing >= i) {
					standing += (s[i] - '0');
				} else {
					friends = i - standing;
					res += friends;
					standing += (s[i] - '0');
					standing += friends;
				}
			}
		}

		printf("Case #%d: %lld\n", t,res);
	}
	return 0;
}

