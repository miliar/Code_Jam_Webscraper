#include <iostream>
#include <queue>
#include <climits>

int compute(std::priority_queue<int> &pq) {
	int turn = 0;
	while (!pq.empty()) {
		int max_val = pq.top();
		pq.pop();
		int times = 1;
		while (!pq.empty() && max_val == pq.top()) {
			++times;
			pq.pop();
		}
		int half = max_val/2;
		int big_half = max_val-half;
		int next_max = pq.empty() ? big_half : pq.top();
			// std::cout << max_val <<  ' ' << next_max << std::endl;
		if (next_max < big_half) {
				// Next max element is big_half
			next_max = big_half;
		}
		if (max_val-next_max <= times) {
				// There is no point in splitting
			turn += max_val;
			break;
		} else {
				// We choose to split;
			for (int i = 0; i < times; ++i) {
				pq.push(half);
				pq.push(big_half);
			}
			turn += times;
		}
	}
	return turn;
}

int recur(std::priority_queue<int> pq, int lower, int upper, int times) {
	// std::cout << lower << ' ' << upper << std::endl;
	for (int i = 0; i < times; ++i) {
		pq.push(lower);
		pq.push(upper);
	}
	int turn = pq.top();
	if (turn <= 3)
		return turn;

	int worst = turn;
	pq.pop();
	times = 1;
	while (!pq.empty() && pq.top() == worst) {
		pq.pop();
		++times;
	}
	for (int i = 1; i <= turn/2; ++i) {
		int tmp_min = times+recur(pq, i, turn-i, times);
		worst = tmp_min < worst ? tmp_min : worst;
	}

	return worst;
}

int main() {
	int cases, n = 1;
	std::cin >> cases;
	while (n <= cases) {
		int d, p;
		std::cin >> d;
		std::priority_queue<int> pq;
		while (d--) {
			std::cin >> p;
			pq.push(p);
		}

		int turn = pq.top();
		if (turn > 3) {
			// turn = worst case scenario
			int worst = turn;
			pq.pop();
			int times = 1;
			while (!pq.empty() && pq.top() == worst) {
				pq.pop();
				++times;
			}
			for (int i = 1; i <= turn/2; ++i) {
				int tmp_min = times+recur(pq, i, turn-i, times);
				worst = tmp_min < worst ? tmp_min : worst;
			}
			turn = worst;
		}

		std::cout << "Case #" << n << ": " << turn << std::endl;
		++n;
	}

	return 0;
}