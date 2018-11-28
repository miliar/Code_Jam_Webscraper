#include <cstdio>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
	
	int x;

	string  s,res, fh, sh;

	char c;
	
	cin >> x;

	for (int i = 0; i < x; ++i) {
		
		res = "";

		fh = "";
		sh = "";

		cin >> s;

		c = s[0];

		for (int j = 1; j < s.size(); ++j) {

			if (s[j] >= c) {
				
				fh += s[j];

				c = s[j];

			}

			else sh += s[j];

		}

		res = string(fh.rbegin(), fh.rend());

		res += s[0];

		res += sh;

		printf("Case #%d: %s\n", i+1, res.c_str());

	}


	return 0;

}

