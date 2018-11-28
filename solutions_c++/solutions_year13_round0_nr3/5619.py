#include <string>
#include <iostream>
#include <istream>
#include <ostream>
#include <sstream>
#include <functional>
#include <algorithm>
#include <numeric>
#include <vector>

#define INT(i) int i; { string line; getline(std::cin, line); stringstream stream(line); stream >> i; } 
#define LINE { string line; getline(std::cin, line); } 

#define INT_LINE_SINGLE(i) int i; { string line; getline(std::cin, line); stringstream stream(line); stream >> i; } 
#define INT_LINE_LIST(v) vector<int> v; { string line; getline(std::cin, line); stringstream stream(line); int n; while(stream >> n) { v.push_back(n); } }
#define INT_LINE_LIST_N(v, n) vector<int> v; { string line; getline(std::cin, line); stringstream stream(line); int i, x = 0; while(x++ < n && stream >> i) { v.push_back(i); } }

using namespace std;

bool isPali(int x);
void process(int c, int l, int u);

int main(void) {
	INT_LINE_SINGLE(cases);

	for(int c = 0; c < cases; c++){
		INT_LINE_LIST_N(bounds, 2);

		process(c + 1, bounds[0], bounds[1]);
	}

	return 0;
}

void process(int c, int l, int u)
{
	int n = 0;

	int start = ceil(sqrt(l));
	int end = floor(sqrt(u));

	for(int i = start; i <= end; i++) {
		if(isPali(i) && isPali(i * i)) {
			n++;
		}
	}

	printf("Case #%i: %i\n", c, n);
}

bool isPali(int i)
{
	stringstream ss; ss << i;

	string x1 = ss.str();
	string x2 = x1;
	reverse(x2.begin(), x2.end());

	return x1 == x2;
}