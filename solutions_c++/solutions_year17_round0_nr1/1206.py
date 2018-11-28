#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <vector>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

#define endl '\n'

void main() {
	std::ios::sync_with_stdio(false);


	int t, n, m;
	string s;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.



	for (int i = 1; i <= t; ++i) {
	 
		cin >> s >> n;

		bool jde = true;
		int number = 0;

		for (size_t j = 0; j < s.size(); j++)
		{
			if (s[j] == '-') {
				number++;

				if (j + n > s.size()) {
					jde = false;
					break;
				}

				for (size_t k = 0; k < n; k++)
				{
					if (s[k + j] == '+')
						s[k + j] = '-';
					else
						s[k + j] = '+';

				}

			}
		}

		if(jde)
			cout << "Case #" << i << ": " << number << endl;
		else
			cout << "Case #" << i << ": IMPOSSIBLE" << endl;
		

	}
}