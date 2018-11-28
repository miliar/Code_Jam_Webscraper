#include <iostream>
#include <string>
#include <fstream>

int main(){
	std::string first;
	char current;
	int count(0), N(0);
	std::ifstream input;
	input.open("B-large.in");
	std::ofstream output;
	output.open("Problem2Solutions.txt");
	input >> N;

	for(int j(0); j < N; ++j){
		input >> first;
		current = first[0];
		for(int i(1); i < first.size(); ++i){
			if(first[i] != current){
				count++;
				current = first[i];
			}
		}
		if(first[first.size()-1] == '-')
			count++;
	
		output << "Case #" << j+1 << ": " << count << std::endl;
		count = 0;
	}
	return 0;
}
