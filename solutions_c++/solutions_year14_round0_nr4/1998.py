#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <streambuf>
#include <cstdint>
#include <assert.h>
#include <set>
#include <iomanip>
#include <map>


int main() {

	int n;
	std::cin >> n;

	for(int _n=0; _n<n; ++_n) {
		std::cout << "Case #" << (_n+1) << ": ";

		std::set<double> naomi, ken, ken2;
		int size;
		std::cin >> size;

		for(int i=0; i<size; ++i) {
			double m;
			std::cin >> m;
			naomi.insert(m);
		}
		for(int i=0; i<size; ++i) {
			double m;
			std::cin >> m;
			ken.insert(m);
			ken2.insert(m);
		}

		int pta = 0, ptb = 0;

		for(auto v: naomi) {
			auto it = ken2.upper_bound(v);
			if(it == ken2.end()) {
				ken2.erase(ken2.begin());
				ptb++;
			}
			else {
				ken2.erase(it);
			}
		}

		for(auto v: naomi) {
			auto maxKen = ken.rbegin();
			auto minKen = ken.begin();

			if(v > *minKen) {
				pta++;
				ken.erase(minKen);
			}
			else {
				ken.erase(*maxKen);
			}
		}

		std::cout << pta << " " << ptb << std::endl;
	}

	return 0;
}