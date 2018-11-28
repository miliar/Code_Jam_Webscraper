
#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

struct party {
	int count, id;
};

class Compare {
public:
	bool operator() (party a, party b) {
		return a.count < b.count;
	}
};

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	std::cin >> T;

	for (int ca = 1; ca <= T; ca++) {
		int N;
		std::cin >> N;

		std::priority_queue<party, std::vector<party>, Compare> arr;
		for (int i = 0; i < N; i++) {
			party p;
			p.id = i;
			std::cin >> p.count;
			arr.push(p);
		}

		printf("Case #%d:", ca);
		while (arr.top().count > 1) {
			party a = arr.top();
			arr.pop();
			a.count--;
			arr.push(a);

			if (arr.top().count > 1) {
				party b = arr.top();
				arr.pop();
				b.count--;
				arr.push(b);

				std::printf(" %c%c", a.id + 'A', b.id + 'A');
			} else {
				std::printf(" %c", a.id + 'A');
			}
		}
		int i = N - 1;
		if (N & 1) {
			std::printf(" %c", i + 'A');
			i--;
		}
		while (i > 0) {
			std::printf(" %c%c", i + 'A', i - 1 + 'A');
			i -= 2;
		}
		printf("\n");
	}
}