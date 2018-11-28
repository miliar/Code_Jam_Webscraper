#include <iostream>
#include <string>
#include <fstream>


bool checkString(std::string userInputStr, int starting);

int main() {
	bool inputArray[100] = { false };
	bool plusThenMinus = true;
	int T = 0;
	int starting = 0;
	int finishing = 0;
	int sizeOfInput=0;
	int count = 0;
	

	std::string userInputStr;
	std::string cutUserInput;
	std::string placeHolder;

	
	
	
	std::ifstream inputFile("B-large.in");
	std::ofstream myfile;
	myfile.open("output_file.txt");
	

	std::getline(inputFile, userInputStr);
	T = std::stoi(userInputStr);
	//std::cin >> T;
	for (int t = 1; t <= T; t++) {

		std::getline(inputFile, userInputStr);
		//std::cin >> userInputStr;

		sizeOfInput = userInputStr.length();
		finishing = sizeOfInput - 1;
		cutUserInput = userInputStr.substr(starting);

		while (!checkString(cutUserInput, starting)) {
			if (cutUserInput.find("+-") != std::string::npos) {
				finishing = cutUserInput.find("+-")+1;
				placeHolder = cutUserInput.substr(starting, finishing);
				
				if (placeHolder.rfind("-") != std::string::npos) {
					count = count + 2;
				}
				else {
					count++;
				}
				cutUserInput = cutUserInput.substr(finishing);
				finishing = starting;

			}
			else {
				count++;
				break;
				
			}

		}

		//add count from test case 
		myfile << "Case #" << t << ": " << count<<" \n";
		//reseting count for next case
		count = 0;

	}
	
	myfile.close();

	
	return 0;
}


bool checkString(std:: string userInputStr, int starting) {
	int k = userInputStr.length();
	for (int i = starting; i < k; i++) {
		if (userInputStr.at(i) == '-') {
			return false;
		}
	}


	return true;
}
