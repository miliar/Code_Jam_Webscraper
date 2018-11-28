#include <cstdio>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <iomanip>
#include <cstring>

using namespace std;

#define MINX(a, b) ((a) < (b) ? (a) : (b));
#define MAX(a, b) ((a) > (b) ? (a) : (b));

typedef unsigned long long ulng;
typedef signed long long slng;
typedef unsigned int uint;
typedef signed int sint;

void solve()
{
	string line;
	unsigned char buf[1024];
	unsigned char mask = 0;
	int len = 0;
	int flips = 0;

	cin >> line;
	len = line.length();
	assert(len < 1024);
	strncpy((char*)buf, line.c_str(), sizeof(buf));
	buf[sizeof(buf) - 1] = '\0';

	for (int i = 0; i < len; i++) {
		if (buf[i] == '+')
			buf[i] = 0xff;
		else {
			assert(buf[i] == '-');
			buf[i] = 0;
		}
	}

	for (int i = len - 1; i >= 0; i--) {
		if ((buf[i] ^ mask) == 0) {
			flips++;
			mask ^= 0xff;
		}
	}
	cout << flips;
}

int main()
{
	int c;
	cin >> c;
	for (int i = 1; i <= c; i++) {
		cout << "Case #" << i << ": ";
		solve();
		cout << "\n";
	}
}
