#include <bits/stdc++.h>

typedef long long int lli;

main () {

	lli t, k, i, n, x;

	std::set<int> set;
	std::string s;

	for (scanf ("%lld", &t), k = 1; k <= t; ++k) {

		scanf ("%lld", &n);

		printf ("Case #%lld: ", k);

		if (n == 0) {

			printf ("INSOMNIA\n");
			continue;
		}

		set.clear ();

		for (x = n;;) {

			s = std::to_string (n);

			for (i = 0; i < s.length (); ++i)
				set.insert (s[i]);

			if (set.size () < 10)
				n += x;

			else
				break;
		}

		printf ("%lld\n", n);
	}
}