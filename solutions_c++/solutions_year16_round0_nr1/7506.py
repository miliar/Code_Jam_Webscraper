#include <iostream>
#include <fstream>
#include <string> 
#include <vector>

int get_digits(int number, std::vector<bool> &mask) {
	std::string numberstr = std::to_string(number);
	for (int i=0; i< numberstr.length(); ++i) {
		mask.at((int)(numberstr[i]-'0')) = true;
	}
}
bool check_all_true(std::vector<bool> mask) {
	bool R = true;
	for (int i=0; i<mask.size(); ++i) {
		if (mask.at(i) == false)
			return false;
	}
	return true;
}

void show_mask(std::vector<bool> mask) {
	std::cout << "Mask: "; 
	for(int i=0; i<mask.size(); ++i) {
		std::cout << mask.at(i);	
	}
	std::cout << std::endl;
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
		int number = stoi(line);
		std::cout << "Number: " << number << "\t";
		if (number == 0) {
			std::cout << "Case #" << case_+1 << ": INSOMNIA" << std::endl;
			outfile << "Case #" << case_+1 << ": INSOMNIA" << std::endl;
			continue;
		}		
	
		std::vector<bool> mask(10, false);
	
		int factor = 1;
		int lastnumber;
		while (!check_all_true(mask)) {
			lastnumber = number * factor;
			//std::cout << "NewNumber: " << newnumber << std::endl;
			get_digits(lastnumber, mask);
			//show_mask(mask);
			
			factor++;
		}
		std::cout << "Case #" << case_+1 << ": " << lastnumber << std::endl;
		outfile << "Case #" << case_+1 << ": " << lastnumber << std::endl;
	}

	infile.close();
	outfile.close();
	
	return 0;
}