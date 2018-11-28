#include <iostream>
#include <fstream>
#include <string> 
#include <vector>
#include <algorithm>

bool check_all_smile(std::string stack) {
	for (int i=0; i<stack.length(); ++i) {
		if (stack[i] == '-')
			return false;
	}
	return true;
}

void flip_stack(int pos, std::string &stack) {
	std::string headstr = stack.substr(0,pos);
	std::string tailstr = stack.substr(pos,stack.length());
	for(int i=0; i<headstr.length(); ++i) {
		if (headstr[i] == '+')
			headstr[i] = '-';
		else
			headstr[i] = '+';
	}
	std::reverse(headstr.begin(), headstr.end());
	stack = headstr + tailstr;
}

int main(int argc, char* argv[]) {
	
	if (argc != 2) {
		std::cerr << "Error, provide input file as argument." << std::endl;
		exit(1); 
	}
	std::string infilename = argv[1];
	std::string outfilename = infilename + ".out";
	
	std::ifstream infile(infilename);
	if (!infile.is_open()) {
		std::cerr << "Error opening file" << std::endl;
		exit(1);
	}
	
	std::ofstream outfile(outfilename);
	std::string line;
	getline(infile, line);
	int T = stoi(line);

	for (int case_ = 0; case_ < T; ++case_) {
		
		getline(infile, line);
		std::cout << line << "\t";
		
		int nflips = 0;
		while (!check_all_smile(line)) {
			if (line[0] == '+') {
				int pos = line.find_first_of('-');
				flip_stack(pos, line);	
			}
			else {
				int pos = line.find_last_of('-');
//				std::cout << "Last -: " << pos << std::endl;
				flip_stack(pos+1, line);	
			}
			nflips++;
		}

		
		//std::cout << "Reversed " << stack << "  "<< nflips << std::endl;
		std::cout << "Case #" << case_+1 << ": " << nflips << std::endl;
		outfile << "Case #" << case_+1 << ": " << nflips << std::endl;
	}

	infile.close();
	outfile.close();
	
	return 0;
}