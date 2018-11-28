#include <iostream>
#include <list>
#include <cstdio>
#include <cmath>
#include <numeric>
#include <utility>
#include <list>
#include <set>
#include <map>
#include <bitset>
#include <vector>
#include <algorithm>
#include <bitset>
#include <deque>
#include <queue>
#include <limits>
#include <string>
#include <cstring>
#include <cctype>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <stack>
#include <queue>

/* a=target variable, b=bit number to act upon 0-n */
#define BIT_SET(a,b) ((a) |= (1<<(b)))
#define BIT_CLEAR(a,b) ((a) &= ~(1<<(b)))
#define BIT_FLIP(a,b) ((a) ^= (1<<(b)))
#define BIT_CHECK(a,b) ((a) & (1<<(b)))

/* x=target variable, y=mask */
#define BITMASK_SET(x,y) ((x) |= (y))
#define BITMASK_CLEAR(x,y) ((x) &= (~(y)))
#define BITMASK_FLIP(x,y) ((x) ^= (y))
#define BITMASK_CHECK(x,y) ((x) & (y))

using namespace std;

typedef unsigned long long int ull;
typedef unsigned long int ul;
typedef long long int ll;
typedef long int li;
typedef unsigned int ui;

long long int findSheep(long long int n) {
	if (n == 0)
		return 0;

	map <int, bool> m; 
	long long int temp = 1, mult = 1, ans = 0;
	while (m.size() != 10) {
		ans = n * mult;
		temp = ans; 
		while (temp) {
			m[(temp%10)+1]++;
			temp = temp / 10; 
		}
		mult++;
	}
	return ans; 
}

int main(){
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		long long int n;
		cin >> n;

		if (n < 0)
			n = -n; 

		cout << "Case #" << t << ": ";
		long long int sheeps = findSheep(n);
		if (!sheeps)
			cout << "INSOMNIA" << endl;
		else
			cout << sheeps << endl;
	}
	return 0;
}
