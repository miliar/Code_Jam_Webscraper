#include <algorithm>
#include <fstream>
#include <iostream>
#include <iterator>
#include <vector>


void getcase (std::ifstream& in,
	int& firstanswer,
	std::vector<int>& first_map,
	int& secondanswer,
	std::vector<int>& second_map) {

	in >> firstanswer;
	for (int i = 0; i < 16; ++i)
		in >> first_map[i];

	in >> secondanswer;
	for (int i = 0; i < 16; ++i)
		in >> second_map[i];
}

int test_case (int firstanswer,
	std::vector<int>& first_map,
	int secondanswer,
	std::vector<int>& second_map) {

	std::sort(first_map.begin()+4*(firstanswer-1),
		first_map.begin()+4*firstanswer);
	std::sort(second_map.begin()+4*(secondanswer-1),
		second_map.begin()+4*secondanswer);

	std::vector<int> result;
	std::set_intersection(first_map.begin()+4*(firstanswer-1),
		first_map.begin()+4*firstanswer,
		second_map.begin()+4*(secondanswer-1),
		second_map.begin()+4*secondanswer,
		std::back_inserter(result));

	if (result.size() == 1) //good case
		return result[0];

	if (result.size() == 0) //volunteer cheated
		return -1;

	return -2; //bad magician

}

int main (int argc, const char* argv[]) {

	if (argc != 2){
		std::cerr << "You morron!";
		return -1;
	}

	std::ifstream in {argv[1]};
	std::ofstream out {"magic.out"};
	int num_cases;
	in >> num_cases;

	for (int i = 1; i <= num_cases; ++i) {
		std::vector<int> first_map(16);
		std::vector<int> second_map(16);
		int firstanswer;
		int secondanswer;

		getcase(in,firstanswer,first_map,
			secondanswer,second_map);

		switch (int result = test_case(firstanswer,first_map,
			secondanswer,second_map)) {

			case -1: out << "Case #" << i << ": Volunteer cheated!\n";
						break;
			case -2: out << "Case #" << i << ": Bad magician!\n";
						break;
			default: out << "Case #" << i << ": " << result << '\n';
		}
	}
}