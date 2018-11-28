#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <utility>

using namespace std;

void solveSingleCase() {
	map <char, char> flip;
	flip['+'] = '-';
	flip['-'] = '+';

	string pile;
	cin >> pile;

	int flips = 0;
	char want = '+';
	for (int i = pile.length()-1; i >= 0; --i) {
		if (pile[i] != want) {
			++flips;
			want = flip[want];
		}
	}

	cout << " " << flips << endl;
}

int main() {
	int T;
	cin >> T;

	for (int i = 1; i <= T; ++i) {
		cout << "Case #" << i << ":";
		solveSingleCase();
	}
	
	return 0;
}
