#include <cstdio>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <iomanip>

using namespace std;

#define MINX(a, b) ((a) < (b) ? (a) : (b));
#define MAX(a, b) ((a) > (b) ? (a) : (b));

typedef unsigned long long ulng;
typedef signed long long slng;
typedef unsigned int uint;
typedef signed int sint;

inline slng pow(slng x, slng y) {
	slng res = 1;
	assert(y >= 0);
	for (slng i = 0; i < y; i++) {
		assert(res * x > res);
		res *= x;
	}
	return res;
}

void solve_small()
{
	slng k, c, s;
	cin >> k >> c >> s;
	slng *pos = new slng[s];

	if (s < k) {
		cout << "IMPOSSIBLE";
		return;
	}
	for (slng i = 1; i <= k; i++) {
		pos[i-1] = i;
	}

	for (slng j = 1; j < c; j++) {
		for (slng i = 1; i < k; i++) {
			pos[i] += i * pow(k, j); 
		}
	}
	for (slng i = 0; i < k; i++)
		cout << pos[i] << " ";

	delete[] pos;
}

int main()
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		solve_small();
		cout << "\n";
	}
}
