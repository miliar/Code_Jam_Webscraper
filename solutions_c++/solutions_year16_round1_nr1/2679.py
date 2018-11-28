#include <bits/stdc++.h>

int t, k, i;

std::string str, s;

main () {
	
	for (std::cin >> t, k = 1; k <= t; ++k) {

		std::cin >> str;

		s = str[0];

		for (i = 1; i < str.length (); ++i) {

			if (str[i] >= s[0])
				s = str[i] + s;

			else
				s += str[i];
		}

		printf ("Case #%d: ", k);
		std::cout << s << std::endl;
	}
}