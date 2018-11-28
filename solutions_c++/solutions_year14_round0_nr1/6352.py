#include <string>
#include <fstream>
#include <iostream>
#include <vector>
#include "ReadIntoVector.h"

std::vector<std::string> ReadIntoVector(std::string input){
	std::ifstream file;
	file.open(input);
	if (!file.is_open()){
		std::cout << "Failed to open\n";
		system("PAUSE");
	}
	std::vector<std::string> answer;
	std::string line;
	int i = 0;
	while (std::getline(file, line)){
		answer.push_back(line + "\n");
		i++;
	}
	return answer;
}