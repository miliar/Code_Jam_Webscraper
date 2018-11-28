#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm> 

using namespace std;

int main() {

	freopen("B-large.in", "r", stdin);
	int numTestCases;
	int D;
	int e;
	int maxPlate;
	int minMov;
	cin >> numTestCases;
	for(int nCase = 1; nCase <= numTestCases; nCase++) {
		vector<int> plates;
		cin >> D;
		for(int i = 0; i < D; i++) {
			cin >> e;
			plates.push_back(e);
		}
		sort(plates.begin(), plates.end());
		reverse(plates.begin(), plates.end());
		maxPlate = *plates.begin();
		minMov = maxPlate;
		for(int candidate = 1; candidate < maxPlate; candidate++) {
			int cantMoves = 0;
			for(vector<int>::iterator it = plates.begin(); (it != plates.end()) and (*it > candidate); ++it ) {
				cantMoves += *it /candidate - (*it % candidate == 0);
			}
			if(minMov > cantMoves + candidate) {
				minMov = cantMoves + candidate;
			}
		}
		cout << "Case #" << nCase << ": " << minMov << endl;
	}
}