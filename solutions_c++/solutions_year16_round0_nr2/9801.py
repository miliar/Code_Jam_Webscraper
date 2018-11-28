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

bool isHappy(string s) {
	for (int i = 0; i < s.size(); i++) {
		if (s[i] == '-')
			return false;
	}
	return true; 
}

void flip(string &input, int pos) {
	for (int i = 0; i <= pos; i++)
		input[i] = (input[i] == '+') ? '-' : '+';
	return;
}

int main(){
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		string input;
		cin >> input;

		int n = input.size(); 
		int count = 0;
		while (!isHappy(input)) {
			for (int i = n-1; i >= 0; i--) 
				if (input[i] == '-') {
					flip(input, i);
					count++;
				}

		}

		cout << "Case #" << t << ": " << count << endl;
	}
	return 0;
}
