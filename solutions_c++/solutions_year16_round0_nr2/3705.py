#include <bits/stdc++.h>
#define lli long long int
#define s(x) scanf("%lld", &x)

using namespace std;

string a;

int main()
{
	lli i,j,k,cnt,ans,tcase,tt;

	s(tcase);
	tt = 1;

	while (tcase--) {
		printf("Case #%lld: ", tt);
		++tt;

		cin >> a;

		if (a[0] == '-') {
			cnt = 1;
			
			for (i = 1; i < a.length(); ++i) {
				if (a[i] == '+')
					break;
			}
		} else {
			cnt = 0;
			i = 1;
		}

		for (; i < a.length(); ) {
			if (a[i] == '-') {
				cnt += 2;

				for (j = i; j < a.length(); ++j) {
					if (a[j] == '+')
						break;
				}
				i = j;				
			} else {
				++i;
			}
		}

		printf("%lld\n", cnt);
	}

	return 0;
}
