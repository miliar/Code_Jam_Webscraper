#include <string>
#include <iostream>
#include <istream>
#include <ostream>
#include <sstream>
#include <functional>
#include <algorithm>
#include <numeric>
#include <vector>

#define INT_LINE_SINGLE(i) int i; { string line; getline(std::cin, line); stringstream stream(line); stream >> i; } 

using namespace std;

void process(int c, string s, int n);
bool isConst(char c);

int main(void) {
	INT_LINE_SINGLE(cases);

	for(int c = 0; c < cases; c++){
		string line; 
		getline(std::cin, line);
		stringstream stream(line);

		string s;
		int n;

		stream >> s;
		stream >> n;

		process(c + 1, s, n);
	}

	return 0;
}

void process(int c, string s, int n)
{
	int r = 0;

	int l = s.length();

	vector<int> matches;

	for(int i = 0; i <= l - n; i++) {
		bool isMatch = true;
		for(int j = i; j < i + n; j++){
			if(!isConst(s.at(j))) {
				isMatch = false;
				break;
			}
		}
		if(!isMatch) continue;
		matches.push_back(i);
	}

	for(int i = n; i <= l; i++){
		for(int j = 0; j <= l - i; j++) {
			r += any_of(matches.begin(), matches.end(), [i, j, n](int k) { return j <= k && (j+i) >= k+n; });
		}
	}

	printf("Case #%i: %i\n", c, r);
}

// PRE: c is an alphabet char
bool isConst(char c){
	return c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u';
}