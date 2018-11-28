#include <algorithm>
#include <deque>
#include <iostream>
#include <iterator>

int play_war(std::deque<double> xs, std::deque<double> ys) {
	while(!xs.empty() && !ys.empty()) {
		if(xs.front() < ys.front())
			xs.pop_front();

		ys.pop_front();
	}

	return xs.size();
}

int play_deceit(std::deque<double> xs, std::deque<double> ys) {
	int res = 0;

	while(!xs.empty()) {
		if(xs.front() < ys.front())
			ys.pop_back();
		else {
			++res;
			ys.pop_front();
		}

		xs.pop_front();
	}

	return res;
}

void process(int tc) {
	int n;
	std::deque<double> xs, ys;

	std::cin >> n;
	std::copy_n(std::istream_iterator<double>(std::cin), n, std::back_inserter(xs));
	std::copy_n(std::istream_iterator<double>(std::cin), n, std::back_inserter(ys));
	std::sort(std::begin(xs), std::end(xs));
	std::sort(std::begin(ys), std::end(ys));

	int war = play_war(xs, ys), deceit = play_deceit(xs, ys);
	std::cout << "Case #" << tc << ": " << deceit << " " << war << std::endl;
}

int main() {
	int n;
	std::cin >> n;
	
	for(int i = 1; i <= n; ++i)
		process(i);
}
