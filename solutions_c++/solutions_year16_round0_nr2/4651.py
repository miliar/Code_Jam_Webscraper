#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int SolveB(string pancakes, char objective) {
	char p, m;
	p = objective == '+' ? '+' : '-';
	m = objective == '+' ? '-' : '+';
	if (find(pancakes.begin(), pancakes.end(), m) == pancakes.end()) {
		return 0;
	} else {
		int n_p_bottom = find(pancakes.rbegin(), pancakes.rend(), m) - pancakes.rbegin();
		int size_top = pancakes.size() - n_p_bottom;
		string upstack(size_top, '.');
		copy_n(pancakes.begin(), size_top, upstack.begin());
		return 1 + SolveB(upstack, m);
	}
}