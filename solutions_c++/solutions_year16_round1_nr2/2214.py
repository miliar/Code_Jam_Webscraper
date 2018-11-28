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

typedef vector<int> VI;
typedef vector<vector<int> > VVI;

bool cprVectorUntilk(VVI a, VI b, int k) {
	for (int i = 0; i < k; i++) {
		if ( (a[i][k] != b[i]) && (a[i][k] != -1) )
			return false;
	}
	return true;
}

int main() {
	FILE * stream1, *stream2;
	freopen_s(&stream1, "Text.txt", "r", stdin);
	freopen_s(&stream2, "OUTPUT.txt", "w", stdout);
	int T, times;
	cin >> T;
	times = 1;
	while (T--) {
		int N,cat;
		cin >> N;
		VI v,result;
		for (int i = 0; i < (2 * N - 1) * N; i++) {
			cin >> cat;
			v.push_back(cat);
		}
		sort(v.begin(), v.end());
		while (!v.empty()) {
			if (v.size() == 1) {
				result.push_back(v[0]);
				v.erase(v.begin());
			}
			else if (v[0] == v[1]) {
				v.erase(v.begin());
				v.erase(v.begin());
			}
			else if (v[0] != v[1]) {
				result.push_back(v[0]);
				v.erase(v.begin());
			}
		}
		cout << "Case #" << times << ": ";
		for (int i = 0; i < result.size(); i++)
			cout << result[i] << " ";
		cout << endl;
		times++;
	}

	return 0;
}