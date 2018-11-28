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

void solve()
{
	slng i, N;
	int seen = 0;
	int digit[10] = {1,1,1,1,1,1,1,1,1,1};
	cin >> N;

	for (i = 1; i <= 1000000LL; i++) {
		slng cur = i * N;
		while (cur) {
			int rem = cur % 10;
			seen += digit[rem];
			//cout << "rem=" << rem << " seen=" << seen << endl;
			digit[rem] = 0;
			cur = (cur - rem) / 10;
		}
		if (seen == 10)
			break;
	}
	if (i > 1000000LL)
		cout << "INSOMNIA";
	else
		cout << i * N;
}

int main()
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		solve();
		cout << "\n";
	}
}
