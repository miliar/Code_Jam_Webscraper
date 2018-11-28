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
#include <queue>
using namespace std;


int main(){
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int t;
	cin >> t;
	for (int c = 1; c <= t; c++){
		bool nums[20];
		memset(nums, false, sizeof(nums));

		int ans;
		cin >> ans;
		int dummy;
		for (int i = 0; i < 16; i++){
			cin >> dummy;
			if (i >= 4 * (ans - 1) && i < 4 * ans){
				nums[dummy] = true;
			}
		}
		vector<int> sol;
		cin >> ans;
		for (int i = 0; i < 16; i++){
			cin >> dummy;
			if (i >= 4 * (ans - 1) && i < 4 * ans){
				if (nums[dummy]){
					sol.push_back(dummy);
				}
			}
		}

		cout << "Case #" << c << ": ";
		if (sol.size() == 1)
			cout << sol[0] << endl;
		else if (sol.size() == 0)
			cout << "Volunteer cheated!" << endl;
		else if (sol.size() > 1)
			cout << "Bad magician!" << endl;

	}
	return 0;
}