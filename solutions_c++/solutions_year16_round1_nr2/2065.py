#include<iostream>
#include<fstream>
#include<sstream>
#include<vector>
#include<unordered_map>
#include<algorithm>
using namespace std;
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int testCount = 0;
	scanf("%d", &testCount);
	for (int i = 0; i < testCount; i++) {
		int N = 0;
		scanf("%d", &N);
		unordered_map<int, int>countmap;
		for (int j = 0; j < 2 * N - 1; j++) {
			int num = 0;
			for (int k = 0; k < N; k++) {
				scanf("%d", &num);
				if (countmap.find(num) == countmap.end()) {
					countmap[num] = 1;
				}
				else
					countmap[num]++;
			}
		}
		vector<int>res;
		for (auto& countpair : countmap) {
			if (countpair.second & 1) {
				res.push_back(countpair.first);
			}
		}
		sort(res.begin(), res.end());
		cout << "Case #" << i + 1 << ": ";
		for (auto& n : res)cout << n << " ";
		cout << endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}