#include <fstream>
#include <string>
#include <vector>
#include <utility>

#include "pattern.hpp"

int main(int argc, char**argv){
	if(argc != 3) return 1;
	std::ifstream input{argv[1]};
	std::ofstream output{argv[2]};
	std::string line;
	getline(input, line);
	int number_of_tests = std::stoi(line);
	std::vector<pattern> patterns;
	patterns.reserve(number_of_tests);
	
	for(int i=0; i < number_of_tests; ++i){
		int height, width;
		input >> height >> width;
		std::vector<std::vector<int>> dataset(height, std::vector<int>(width));
		for(int h = 0; h<height; ++h){
			for(int w = 0; w<width; ++w){
				input >> dataset[h][w];
			}
		}
		patterns.emplace_back(height, width, std::move(dataset));
	}
	int test_case = 0;
	for(auto& p: patterns){
		output << "Case #" << ++test_case << ": ";
		if(p.can_be_created()){
			output << "YES\n";
		}
		else{
			output << "NO\n";
		}
	}
}
