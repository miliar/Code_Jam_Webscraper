#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) { 
		cout << "Case #" << i << ": ";
		int X, R, C;
		cin >> X >> R >> C;
		int prod = R * C;
		int Rr;
		int Cr;
		if (C > R) {
			Rr = C;
			Cr = R;
		} else {
			Rr = R;
			Cr = C;
		}
		
		
		if (X == 1) {
			cout << "GABRIEL" << endl;
		}
		
		if (X == 2) {
			if (prod % 2 != 0) {
				cout << "RICHARD" << endl;
			} else {
				cout << "GABRIEL" << endl;
			}
		}
	
		if (X == 3) {
			if (Rr < 3) {
				cout << "RICHARD" <<endl;
				continue;
			}
			if (Rr == 3) {
				if (Cr > 1) {
					cout << "GABRIEL" << endl;
				} else {
					cout << "RICHARD" << endl;
				}
				continue;
			}
			if (prod % 3 != 0) {
				cout << "RICHARD" << endl;
			} else {
				cout << "GABRIEL" << endl;
			}
		}
	
		if (X == 4) {
			if (Rr < 4) {
				cout << "RICHARD" << endl;
				continue;
			}
			if (Cr == 1) {
				cout << "RICHARD" << endl;
			}
			if (Cr == 2) {
				cout << "RICHARD" << endl;
			}
			if (Cr == 3) {
				cout << "GABRIEL" << endl;
			}
			if (Cr == 4) {
				cout << "GABRIEL" << endl;
			}
		}
	}
	return 0;
}

