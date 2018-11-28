#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <cstring>
#include <array>
#include <cassert>
#include <bitset>

using namespace std;

int main()
{
	int t; cin >> t;
	for (int i = 1; i <= t; ++i) {
		int K, C, S;
		cin >> K >> C >> S;

		std::cout << "Case #" << i << ": ";
		for (int i = 1; i <= S; ++i) cout << i << " ";
		cout << "\n";
	}

	return 0;
}