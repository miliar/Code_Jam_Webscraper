#include <iostream>
#include <string>
#include <fstream>


bool check(bool baseTen[10]);

int main() {
	int N=0;
	int T = 0;
	int placeholder=0;
	std::string name;
	std::string numStringValue;
	std::string output;
	std::string inputPlaceHolder;


	
	bool baseTen[10] = { false };

	std::ofstream myfile;
	myfile.open("output_file.txt");
	
	

	std::ifstream inputFile("A-large.in");
	
	
	std::getline(inputFile, inputPlaceHolder);
	T = std::stoi(inputPlaceHolder);
	//std::cin >> T;
	
	for (int t = 1; t <= T;t++) {
		std::getline(inputFile, inputPlaceHolder);
		N = std::stoi(inputPlaceHolder);
		//std::cin >> N;

		for (int i = 1; !check(baseTen); i++) {

			placeholder = i*N;
			name = std::to_string(placeholder);
			if (N != 0) {
				for (int e = 0; e < 10;e++) {
					numStringValue = std::to_string(e);
					if (name.find(numStringValue) != std::string::npos) {
						baseTen[e] = true;
					}
				}

			}
			else {
				break;
			}


		
		}
		for (int v = 0; v < 10; v++) {
			baseTen[v] = false;
		}
		if (N != 0) {
			
			myfile << "Case #" << t << ": " << name;
			if (T != t) {
				myfile << "\n";
			}
		}
		else {
			myfile << "Case #" << t << ": INSOMNIA";
			if (T != t) {
				myfile << "\n";
			}
		}
		
	}
	myfile.close();
	
	
	


	return 0;
}

bool check(bool baseTen[10]) {

	for (int i = 0; i < 10; i++) {
		if (!baseTen[i]) {
			return false;
		}
	}
	return true;
}
