#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
using namespace std;

void DoSwap(int i, int j, string& s) {
	reverse(s.begin() + i, s.begin() + j + 1);
	for (int k = i; k <=j; k++) {
		if (s[k] == '+') {
			s[k] = '-';
		} else {
			s[k] = '+';
		}
	}
}
void PrintAnswer(string s) {
	int stp = 0;
	while (true) {
		int idx = -1;
		for (int i = s.size() - 1; i>=0; i--) {
			if (s[i] == '-') {
				idx = i;
				break;
			}
		}
		if (idx == -1) {
			break;
		}
		stp++;
		if (idx == 0) {
			break;
		}
		if (s[0] == '-') {
			DoSwap(0, idx, s);
		} else {
			int idx2 = 0;
			for (int i = 1; i < s.size() ; i++) {
				if (s[i] == '-') {
					idx2 = i - 1;
					break;
				}
			}
			DoSwap(0, idx2, s);
			stp++;
			DoSwap(0, idx, s);
		}
	}
	cout << stp;
}
int main() {
	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);
	int t;
	string s;
	cin >> t;
	for (int tt = 1; tt <= t; tt++) {
		cin >> s;
		cout << "Case #" << tt <<": ";
		PrintAnswer(s);
		cout << endl;
	}
	return 0;
}
