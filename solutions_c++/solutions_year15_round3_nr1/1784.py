//cedar
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <climits>
#include <cmath>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

int main() {
	std::ios::sync_with_stdio(false);
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int R, C, W;
		cin >> R >> C >> W;

		int result = C/W;
		
		if (C%W == 0) {
			result = result + W - 1;
		}
		else
			result += W;

		cout << "Case #" << i + 1 << ": " << result * R << endl;
	}

	return 0;
}