#include <iostream>
#include <string>
#include <cstdlib>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>    // std::sort
#include <vector>       // std::vector
#include <map>
using namespace std;

template<typename T1, typename T2>
struct less_second {
	typedef pair<T1, T2> type;
	bool operator ()(type const& a, type const& b) const {
		return a.second > b.second;
	}
};

int main() {
	std::ifstream fin("A-large.in");

	std::ofstream fout("A-large.out");
//	std::ifstream fin("A-small.in");
//	FILE *fout = freopen("A-small.out", "w", stdout);
	int T;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		int parties_num;
		fin >> parties_num;
		map<char, int> array;
		stringstream ss;
		int sum_parties = 0;
		char c = 'A';
		for (int i = 0; i < parties_num; i++) {
			int num;
			fin >> num;
			sum_parties += num;
			array.insert(std::pair<char, int>(c, num));
			std::cout << c << ":" << num << " ";
			c++;
		}
		std::cout << std::endl;
		vector<pair<char, int> > mapcopy(array.begin(), array.end());
		sort(mapcopy.begin(), mapcopy.end(), less_second<char, int>());
		while (sum_parties > 0) {
			char evacuate = mapcopy.begin()->first;
			mapcopy.begin()->second--;
			if (mapcopy.begin()->second == 0) {
				std::cout << "remove1 " << mapcopy.begin()->first << std::endl;
				mapcopy.erase(mapcopy.begin());
			}
			sum_parties--;
			sort(mapcopy.begin(), mapcopy.end(), less_second<char, int>());
			std::cout << mapcopy.begin()->first << mapcopy.begin()->second
					<< " ";
			std::cout << sum_parties << std::endl;
			if (mapcopy.empty()) {
				ss << evacuate;
				break;
			}
			if ((!(mapcopy.begin()->second - 1)) && ((sum_parties - 1) > 0)) {
				ss << evacuate;
				ss << " ";
				sort(mapcopy.begin(), mapcopy.end(), less_second<char, int>());
				continue;
			}
			if (((double) (mapcopy.begin()->second - 1) / (sum_parties - 1)) > 0.5) {
				ss << evacuate;
				ss << " ";
			} else {
				ss << evacuate;
				ss << mapcopy.begin()->first;
				ss << " ";
				mapcopy.begin()->second--;
				if (mapcopy.begin()->second == 0) {
					std::cout << "remove2 " << mapcopy.begin()->first << std::endl;
					mapcopy.erase(mapcopy.begin());
				}
				sum_parties--;
			}
			sort(mapcopy.begin(), mapcopy.end(), less_second<char, int>());
			cout << "already removed: "<<ss.str() << endl;
		}
		std::cout << std::endl;
		fout << "Case #" << t << ": ";
		fout << ss.str() << endl;
	}
	//exit(0);

	return 0;
}

