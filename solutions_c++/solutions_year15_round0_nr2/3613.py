#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <cstdlib>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <string>
#include <iterator> 

using namespace std;



int main() {
	int T;
	cin >> T;

	for (int i = 0; i < T; i++) {
		int D;
		cin >> D;
		//cout << D << endl;
		vector<int> pancakes(D, 0);

		for (int j = 0; j < D; j++) {
			//int tmp;
			cin >> pancakes[j];
		}

		//sort(pancakes.begin(), pancakes.end(), greater<int>());
		// get steps for each pancake number
		int maxval = pancakes[0];
		for (int j=1; j < pancakes.size(); j++) {
			if (maxval < pancakes[j]) 
				maxval = pancakes[j];
		}

		int z = 2;
		while(z < maxval) {
			int tmp = 0;
			for (int j = 0; j < pancakes.size(); j++) {
				tmp += (pancakes[j]-1) / z;
			}
			maxval = min(maxval, tmp + z);
			z += 1;
		}

		cout << "Case #" << i+1 << ": " << maxval << endl;
	}

	return 0;
}


