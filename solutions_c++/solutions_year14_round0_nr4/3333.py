#include <iostream>
#include <deque>
#include <algorithm>

unsigned int w(std::deque<double> n, std::deque<double> k) {
	unsigned int s = 0;
	while(!n.empty()) {
		if( n.back() > k.back() ) {
			n.pop_back(); k.pop_front(); s++;
		} else {
			n.pop_back(); k.pop_back();
		}
	}
	return s;
}

unsigned int d(std::deque<double> n, std::deque<double> k) {
	unsigned int s = 0;
	while(!n.empty()) {
		if( n.front() < k.front() ) {
			n.pop_front(); k.pop_back();
		} else {
			n.pop_front(); k.pop_front(); s++;
		}
	}
	return s;
}

int main(int argc, char* argv[]) {
	unsigned int T, N;
	double v;

	std::deque<double> n, k;

	std::cin >> T;

	for( unsigned int t = 1; t <= T; t++ ) {
		
		std::cin >> N;
		n.clear(); k.clear();

		for( unsigned int i = 0; i < N; i++ ) {
			std::cin >> v; n.push_back(v);
		}
		for( unsigned int i = 0; i < N; i++ ) {
			std::cin >> v; k.push_back(v);
		}

		std::sort(n.begin(), n.end());
		std::sort(k.begin(), k.end());

		std::cout << "Case #" << t << ": " << d(n,k) << " " << w(n,k) << std::endl;

	}

	return 0;
}