#include <cstdio>
#include <algorithm>
#include <iostream>
#include <vector>
#include <tuple>
#include <set>
#include <map>
#include <cassert>
#include <string>

using namespace std;

int test() {
	int n, x;
	vector<int> tab;
	cin >> n >> x;
	tab.resize(n);
	for(auto &x : tab)
		cin >> x;

	sort(tab.begin(), tab.end());

	int counter = 0;
	int j=n-1;
	for(int i=0; i<n; ++i) {
		for(; j>i && tab[i]+tab[j] > x; --j);

		if(i<j && tab[i] + tab[j] <= x) {
			--j;
		} else {
			++counter;
			// i alone
		}
	}

	return counter;
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int T;
	cin >> T;
	for(int i=0; i<T; ++i)
		cout << "Case #" << (i+1) << ": " << test() << "\n";

	return 0;

}
