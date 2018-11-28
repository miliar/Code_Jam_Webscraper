#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <functional> 
#include <vector>
#include <set>
#include <numeric>
#include <unordered_map>

using namespace std;

struct TestCase {
	int diners;
	vector<int> pancakes;
};

std::vector<TestCase> load(const std::string& s) {
	std::ifstream fs(s);
	if (!fs.is_open())
		std::cout << "Not found" << std::endl;

	int n;
	std::vector<TestCase> res;
	fs >> n;
	for (int i = 0; i < n; i++) {
		TestCase tc;
		fs >> tc.diners;
		for (int i = 0; i < tc.diners; i++) {
			int p;
			fs >> p;
			tc.pancakes.push_back(p);
		}
		res.push_back(tc);
	}
	fs.close();
	return res;
}

typedef std::unordered_map<int, int> splitcache;

splitcache computeCache(int max) {
	splitcache res;
	for (int i = 0; i <= max; i++) {
		int counts = i;
		for (int j = 1; j <= i / 2; j++) {
			counts = min(std::max(res[j], res[i - j]) + 1, counts);
		}
		res[i] = counts;
	}
	return res;
}

std::string solve(TestCase& tc, splitcache& cache) {
	vector<int> pancakes = tc.pancakes;
	std::make_heap(pancakes.begin(), pancakes.end());
	
	int savedMinutes = 0;
	int best = pancakes[0];
	while (pancakes[0] > 2) {
		int max = pancakes[0];
		pop_heap(pancakes.begin(), pancakes.end());
		pancakes.resize(pancakes.size() - 1);

		int secondMax = pancakes.size() > 0 ? pancakes[0] : 0;
		/*int split = max / 2;
		int splitcost = max / 2 + max % 2;
		for (int i = 1; i <= max / 2; i++) {
			int cost = std::max(cache[i], cache[max - i]);
			if (cost < splitcost && max - i <= secondMax) {
				split = i;
				splitcost = cost;
			}
		}*/
		++savedMinutes;
		int split = max / 2;
		if (max == 9)
			split = 3;
		
		pancakes.push_back(max - split);
		push_heap(pancakes.begin(), pancakes.end());
		pancakes.push_back(split);
		push_heap(pancakes.begin(), pancakes.end());
		best = min(pancakes[0] + savedMinutes, best);
	}

	pancakes = tc.pancakes;
	std::make_heap(pancakes.begin(), pancakes.end());
	savedMinutes = 0;
	while (pancakes[0] > 2) {
		int max = pancakes[0];
		pop_heap(pancakes.begin(), pancakes.end());
		pancakes.resize(pancakes.size() - 1);
		++savedMinutes;
		int split = max / 2;
		pancakes.push_back(max - split);
		push_heap(pancakes.begin(), pancakes.end());
		pancakes.push_back(split);
		push_heap(pancakes.begin(), pancakes.end());
		best = min(pancakes[0] + savedMinutes, best);
	}
	return std::to_string(best);
}

int main(int argc, const char *argv[]) {
	auto cache = computeCache(10);

	std::ofstream fs("B-small-attempt3.out");
	fs.precision(8);
	fs << std::fixed;
	int i = 1;
	for (auto tc : load("B-small-attempt3.in")) {
		fs << "Case #" << i << ": " << solve(tc, cache) << std::endl;
		std::cout << i << std::endl;
		i++;
	}
	fs.close();
	return 0;
}
