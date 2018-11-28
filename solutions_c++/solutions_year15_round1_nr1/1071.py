#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <array>
#include <string>
#include <deque>
#include <list>
#include <numeric>
#include <limits>
#include <utility>
#include <cmath>
#include <cstdlib>

using namespace std;

void comp(int tc){
	int N;
	cin >> N;
	vector<int> v(N);
	for (int &val : v)
		cin >> val;

	int ans1 = 0, ans2 = 0, md = 0;
	for (int i = 0; i < N-1; ++i){
		int diff = v[i] - v[i + 1];
		ans1 += max(0, diff);
		md = max(md, diff);
	}

	for (int i = 0; i < N - 1; ++i){
		ans2 += min(md, v[i]);
	}

	cout << "Case #" << tc << ": " << ans1 << " " << ans2 << endl;
}

int main(){
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i){
		comp(i);
	}
}