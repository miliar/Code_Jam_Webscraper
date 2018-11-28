#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <algorithm>
#include <ctime>
using namespace std;

int main() {
	int T; cin >> T;
	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";
		
		int R, C, W; cin >> R >> C >> W;
		cout << C/W + W-1 + (C%W != 0) << endl;
	}
	
	return 0;    
}
