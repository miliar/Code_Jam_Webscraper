#include <bits/stdc++.h>

typedef long long int lli;

main () {

	lli t, k, z, i, j;

	std::string s;

	for (scanf ("%lld", &t), k = 1; k <= t; ++k) {

		printf ("Case #%lld: ", k);

		std::cin >> s;

		for (i = s.length () - 1, z = 0; i >= 0; --i) {

			if (s[i] == '-') {

				for (j = 0; j < i; ++j) {
					
					if (s[j] == '+')
						s[j] = '-';

					else
						s[j] = '+';
				}

				++z;
			}
		}

		std::cout << z << std::endl;
	}
}