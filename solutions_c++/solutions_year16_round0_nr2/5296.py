#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>

using namespace std;

long pancakes(string s) {
	
	string s_t = s;
	
	long k = 0;

	char c;

	while (s_t != "") {

		if (s_t == string( s_t.size(), '+')) break;
		
		if (s_t == string(s_t.size(), '-')) {

			++k;

			break;

		}

		c = s_t[0];
		
		for (long i = 1; i < s_t.size(); ++i) {

			if (c != s_t[i]) {
				
				++k;
				
				s_t = s_t.substr(i);

				break;
			
			}

		}

	}

	return k;

}

int main() {
	
	long n;
	
	string s;

	scanf("%ld", &n);

	for (long z = 0; z < n; ++z) {

		cin >> s; 

		printf("Case #%ld: %ld\n", z+1, pancakes(s));

	}

	return 0;

}
