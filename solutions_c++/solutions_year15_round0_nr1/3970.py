#include <iostream>
#include <numeric>
#include <algorithm>
#include <functional>
#include <iterator>
#include <vector>

int main() {
	unsigned n;
	std::cin >> n;
	for (unsigned i=0; i<n; ++i) {
		unsigned max;
		std::string ind;
		std::cin >> max;
		std::cin >> ind;
		
		typedef std::vector<unsigned> Triggers;
		Triggers  triggers(ind.size());
		std::transform(ind.begin(), ind.end(), triggers.begin(), std::bind2nd(std::minus<unsigned>(), '0'));

		unsigned standing = 0;
		unsigned threshold = 0;
		unsigned need = 0;
		for (Triggers::iterator it = triggers.begin(); it != triggers.end(); ++it) {
			if (standing >= threshold) {
				standing += *it;
			} else {
				unsigned diff = (threshold - standing);
				need += diff;
				standing += (*it) + diff;
			}
			++threshold;
		}

		std::cout << "Case #" << i+1 << ": " << need << std::endl;
	}
	return 0;
}

