#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <ctime>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <vector>

using namespace std;

int main() {
#ifdef TESTING
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T, X, R, C;
	cin >> T;
	for (int caso = 1; caso <= T; caso++) {
		cin >> X >> R >> C;
		cout << "Case #" << caso << ": ";
		if (R > C) swap(R, C);
		bool gabriel = false;
		switch (X) {
		case 1: gabriel = true; break;
		case 2:
			if ((C & 1) == 0 || (R & 1) == 0) gabriel = true;
			break;
		case 3:
			if ((C == 3 && R > 1) || (C == 4 && R == 3)) gabriel = true;
			break;
		case 4:
			if (C == 4 && R > 2) gabriel = true;
			break;
		}

		cout << (gabriel ? "GABRIEL" : "RICHARD") << endl;
	}

	return 0;
}
