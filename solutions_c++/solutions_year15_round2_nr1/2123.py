#include <iostream>
#include <cstdint>
#include <vector>
#include <queue>
#include <set>
using namespace std;

uint64_t getReverse(uint64_t x) {
	int y = 0;
	while (x) {
		y = 10 * y + x % 10;
		x /= 10;
	}
	return y;
}

int main() {
	uint64_t bound = 2e6;
	vector<uint64_t> memo(bound); 
	for (int i = 0; i < bound; i++) {
		 memo[i] = i;
	}
	queue<uint64_t> q0, q1;
	q0.push(1);
	set<uint64_t> visited;
	set<uint64_t> visitedNext;
	int level = 1;
	while(!q0.empty()) {
		uint64_t front = q0.front();
		// cout << front << endl;
		visited.insert(front);
		memo[front] = level;
		q0.pop();

		uint64_t rfront = getReverse(front);

		if (front + 1 < bound && visited.count(front+1) == 0 && visitedNext.count(front + 1) == 0) {
			q1.push(front + 1);
			visitedNext.insert(front + 1);

			visited.insert(front+1);
		}
		if (rfront < bound && visited.count(rfront) == 0 && visitedNext.count(rfront) == 0) {
			q1.push(rfront);
			visitedNext.insert(rfront);

			visited.insert(rfront);
		}

		if (q0.empty()) {
			q0 = q1;
			q1 = queue<uint64_t>();
			level++;
			visitedNext = set<uint64_t> ();
		}
	}


	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		int N;
		cin >> N;
		cout << "Case #" << t << ": " << memo[N] << endl;
	}
	
	return 0;
}