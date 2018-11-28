#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <numeric>

typedef std::vector<int> vector_t;

int main() {

	int s_max;
	vector_t s;
	vector_t res;
	
	std::ifstream input_file;
	input_file.open("input.txt");
	unsigned int T;
	std::string line;

	if (input_file.is_open()) {
		std::getline(input_file,line);
		T = std::stoi(line);
		for (int i = 0; i < T; ++i) {

			std::getline(input_file,line);
			std::string::size_type pos;
			pos = line.find(' ',0);
			std::string first = line.substr(0,pos);
			std::string last = line.substr(pos+1);
			
			s_max = std::stoi(first);
			s.clear();
			for (int i = 0; i < last.length(); ++i) {
				s.push_back((int)last.at(i) - 48);
			}


			int count(0);
			for (int j = 0; j < s_max; ++j) {
				if (std::accumulate(s.begin(), s.begin() + j+1, count) < j+1) {
					++count;
				}
			}
			res.push_back(count);
		}
	}
	input_file.close();

	int index(0);
	std::ofstream output_file;
  	output_file.open ("output.txt");
  	for (vector_t::iterator it = res.begin(); it < res.end(); ++it) {
			output_file << "Case #" << ++index <<": " << *it << std::endl;
	}
  	output_file.close();

	return 0;
}