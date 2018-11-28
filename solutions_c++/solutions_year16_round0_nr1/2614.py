#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <unordered_map>
#include <set>
#include <vector>
#include <algorithm>
#include <utility>
#include <iomanip>
#include <stack>

using namespace std;

set<int> seen;
void digitsBreak(long long int x){
	while (x > 0) {
		int remainder = x % 10;
		seen.insert(remainder);
		x = x / 10;
	}
}

int main() {
	FILE * stream1, *stream2;
	freopen_s(&stream1, "Text.txt", "r", stdin);
	freopen_s(&stream2, "OUTPUT.txt", "w", stdout);
	int T, i;
	cin >> T;
	i = 1;
	while (T--) {
		long long int n;
		cin >> n;
		if (n == 0)
			cout << "Case #" << i << ": INSOMNIA" << endl;
		else {
			seen.clear();
			int N = 0;
			while (seen.size() < 10) {
				N++;
				digitsBreak(N * n);
			}
			cout << "Case #" << i << ": " << N*n << endl;
		}
		i++;
	}
	return 0;
}