#include <iostream>
#include <vector>
#include <set>
#include <thread>
#include <future>
#include <functional>

#define max(a,b) ((a) > (b) ? (a) : (b))
#define min(a,b) ((a) < (b) ? (a) : (b))

//using nnpair = std::pair<int, int>;
//
//std::vector<nnpair> precalc_optimal()
//{
//	std::vector<nnpair> result(1001);
//	for (int i = 0; i <= 1000; ++i) {
//		result[i].first = 0;
//		result[i].second = i;
//	}
//	for (int i = 2; i <= 1000; ++i) {
//		for (int j = 1; j < i; ++j) {
//			int br = result[j].first + result[i-j].first + 1;
//			int re = max(result[j].second, result[i-j].second);
//			if ((result[i].first + result[i].second > br + re) ||
//				(result[i].first + result[i].second == br + re &&
//				 result[i].first > br)) {
//				result[i].first = br;
//				result[i].second = re;
//			}
//		}
//	}
//	return result;
//}
//
//
//
//int main()
//{
//	std::vector<nnpair> prec = precalc_optimal();
//
//	int T;
//	std::cin >> T;
//	for (int c = 1; c <= T; ++c) {
//		int D, best = 0, calc = 0, bmax = 0;
//		std::cin >> D;
//		std::vector<int> plates(D);
//		for (int i = 0; i < D; ++i) {
//			std::cin >> plates[i];
//			best = max(best, plates[i]);
//			calc += prec[plates[i]].first;
//			bmax = max(bmax, prec[plates[i]].second);
//		}
//		std::cout << "Case #" << c << ": " << min(best, calc + bmax) << '\n';
//	}
//
//	return 0;
//}

// BRUTEFORCE

using mset = std::multiset<int, std::greater<int>>;

int find_optimal(mset _plates)
{
	int front = *_plates.begin();
	_plates.erase(_plates.begin());
	int best = front;
	if (front <= 3) {
		return front;
	}
	for (int j = 2; j <= front / 2; ++j) {
		mset test = _plates;
		test.insert(j);
		test.insert(front - j);
		best = min(best, find_optimal(test) + 1);
	}
	return min(best, front);
}


int main()
{
	int T;
	std::cin >> T;

	std::vector<std::future<int>> res(T);
	std::vector<mset> plates(T);

	for (int c = 1; c <= T; ++c) {
		int D;
		std::cin >> D;
		for (int i = 0; i < D; ++i) {
			int P; std::cin >> P;
			plates[c-1].insert(P);
		}
		res[c-1] = std::async(std::launch::async, find_optimal, plates[c-1]);
	}
	
	for (int c = 1; c <= T; ++c) {
		std::cout << "Case #" << c << ": " << res[c-1].get() << '\n';
	}
	return 0;
}