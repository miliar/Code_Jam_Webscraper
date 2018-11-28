#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <set>
#include <memory>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <memory>
#include <iostream>
#include <sstream>


void solve(int num, std::ifstream& input, std::ofstream& output){

	int max_S = 0;
	std::string str;
	
	std::string line;
	std::getline(input,line);
	
	std::stringstream          lineStream(line);
	std::string                cell;
		
	std::getline(lineStream,cell,' ');
	max_S = atoi(cell.c_str());
	std::getline(lineStream,cell,' ');

	std::vector<int> persons(max_S+1,0);
	for(int i = 0; i <= max_S; ++i){
		char c = cell[i];
		persons[i] = atoi(&c);
	}

	int to_invite = 0;
	int total = 0;
	for(int i = 1; i < persons.size(); ++i){
		total += persons[i-1];

		if(total < i){
			to_invite += (i-total);
			total += (i-total);
		}
		//std::cout << i << " - " << total << " - " << to_invite << std::endl;
	}


	
	//std::cout	<< "Case #" << num << ": ";
	output		<< "Case #" << num << ": ";

	
	//std::cout	<< to_invite << std::endl;
	output		<< to_invite << std::endl;

}


int main(int argc, char *argv[]){
	if(argc!=3){
		std::cout << "wrong number of arguments";
		return 1;
	}

	std::ifstream file_input (argv[1]);
	if (!file_input.is_open()){
		std::cout << "unable to open the input file";
		return 1;
	}

	std::ofstream file_output (argv[2]);
	if (!file_output.is_open()){
		std::cout << "unable to open the input file";
		return 1;
	}

	int n_tests = 0;
	file_input >> n_tests;

	std::cout << "#tests: " << n_tests << std::endl;


	std::string line;
	std::getline(file_input,line);

	for(int i = 0; i < n_tests; ++i){
		solve(i+1,file_input,file_output);
	}

}