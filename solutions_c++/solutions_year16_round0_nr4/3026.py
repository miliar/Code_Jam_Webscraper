#include <bits/stdc++.h>
#define lli long long int
#define s(x) scanf("%lld", &x)

using namespace std;

int main()
{
	lli tt,tz,n,m,k,i,j;

	s(tt);
	tz = 1;

	while (tt--) {
		printf("Case #%lld: ", tz);
		++tz;
		s(n);s(m);s(k);
		
		if (m == 1) {
			for (i = 1; i <= n; ++i) cout << i << " ";
			cout << endl;
		} else if (n == 1) {
			cout << 1 << endl;
		} else {
		for (i = 2; i <= n; ++i)
			cout << i << " " ;

		cout << endl;}
	}

	return 0;
}
