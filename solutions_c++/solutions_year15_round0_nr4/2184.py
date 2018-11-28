#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <stack>
#include <assert.h>
#include <algorithm>
#include <math.h>
#include <ctime>
#include <functional>

#include <Windows.h>

using namespace std;

int main(int argc, char* argv[]) {
	ifstream inf(argv[1]); 

	int TC = 0; 
	inf >> TC; 
	for (int tc = 1; tc <= TC; tc++) {
		int x, r, c; 
		inf >> x >> r >> c; 

		int l = (x - 1) / 2 + 1; 
		bool ok = ((r * c) % x == 0);

		if (ok) {
			if (l < min(r, c)) {
				;
			}
			else if (l > min(r, c)) {
				ok = false;
			}
			else {
				bool good = false;
				for (int i = 0; i <= (x - l); i++) {
					good = false;
					for (int line = 0; line <= (max(r, c) - 1) && !good; line++) {
						int i0 = i, i1 = x - l - i; 
						int l0 = line * min(r, c), l1 = (max(r, c) - 1 - line) * min(r, c);
						if (l0 < i0 || l1 < i1) {
							continue;
						}
						if ((l0 - i0) % x == 0)
							good = true;
					}
					if (!good) break;
				}
				if (!good)
					ok = false;
			}
		}	

		if (ok) {
			cout << "Case #" << tc << ": GABRIEL" << endl;
		}
		else {
			cout << "Case #" << tc << ": RICHARD" << endl; 
		}
	}

	return 0; 
}