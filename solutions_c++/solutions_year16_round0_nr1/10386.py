// bleatrix.cpp
// assignment 1
// by sajenesis

#include <iostream>
#include <iterator>
#include <fstream>
#include <vector>
#include <algorithm> 
#include <string>

std::vector<int> integerSplitter(int number){
	std::vector<int> splitList;
	while (true){
		splitList.push_back(number % 10);
		number=number / 10;
		if(number == 0){
			return splitList;
		}
	}
}

int bleatrix(int N){
	if (N == 0){
		std::cout << "INSOMNIA" << std::endl;
		return 0;
	}
	std::vector<int> digits = {0,1,2,3,4,5,6,7,8,9};
	int multiplier = 1;
	int lastNumber = N;
	while(!digits.empty()){
		int current = N * multiplier;
		std::vector<int> currentString = integerSplitter(current);
		// compare elements of digits with currentString
		for (int i = 0; i < currentString.size(); i++){
			for (int j =0; j < digits.size(); j++){
				if (currentString[i] == digits[j]){
					// remove matched elements
					digits.erase(digits.begin()+j);
				}
			}
		}
		lastNumber = current;
		multiplier++;
		if (digits.empty()){
			return lastNumber;
		}
	}
}

int main()
{
	// set up input file 
	std::ifstream is("A-large.in");
	std::istream_iterator<int> start(is), end;
	std::vector<int> numbers(start, end);
	int T = numbers[0];
	std::ofstream appendfile;
	appendfile.open("output_large.txt", std::ios_base::app);
	for(int i = 1; i < T + 1; i++){
		int lastNumber = bleatrix( numbers[i]);
		if (lastNumber == 0){
			appendfile << "Case #" << i << ": " << "INSOMNIA" << std::endl;
		}else{
		appendfile << "Case #" << i << ": " << lastNumber << std::endl;
		}
	}
}
