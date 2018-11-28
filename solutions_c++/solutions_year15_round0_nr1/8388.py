#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main()
{
	int T;
	std::cin >> T;
	for (auto i = 1; i <= T; ++i) {
		int n;
		std::string people;
		std::cin >> n >> people;
		int stand = 0;
		int add = 0;
		for (auto shyness = 0u; shyness < people.size(); ++shyness) {
			if (stand < shyness) {
				add += shyness - stand;
				stand += shyness - stand;
			}
			stand += people[shyness] - '0';
		}
		std::cout << "Case #" << i << ": " << add << std::endl;
	}
}
