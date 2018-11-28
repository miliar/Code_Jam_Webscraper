#include <iostream>
#include <numeric>
#include <algorithm>
#include <functional>
#include <iterator>
#include <set>

typedef std::multiset<unsigned> Eating;

std::ostream& operator<<(std::ostream& out, const Eating& e) {
	std::copy(e.begin(), e.end(), std::ostream_iterator<unsigned>(out, " "));
	return out;
}

unsigned minTime(const Eating& e) {
	Eating noMax = e;
	Eating::iterator itEnd = noMax.end();
	--itEnd;
	unsigned last = *itEnd;
	if (last <=3) {
		return last;
	}
	
	noMax.erase(itEnd);

	unsigned ret = last;
	for (unsigned half = last/2; half < last-1; ++half) {
		Eating split = noMax;
		split.insert(half);
		split.insert(last-half);
		unsigned tmp = 1 + minTime(split);
		if (tmp < ret)
			ret = tmp;
	}

	return ret;
}

int main() {
	unsigned n;
	std::cin >> n;
	for (unsigned i=0; i<n; ++i) {
		unsigned plates;
		std::cin >> plates;
		
		Eating eating;
		for (unsigned e=0; e<plates; ++e) {
			unsigned c;
			std::cin >> c;
			eating.insert(c);
		}

		std::cout << "Case #" << i+1 << ": " << minTime(eating) << std::endl;
	}
	return 0;
}

