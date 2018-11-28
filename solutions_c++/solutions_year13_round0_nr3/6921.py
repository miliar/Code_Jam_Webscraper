#include <math.h>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

int numberOfDigits(int a){
	int count = 0;
	while( a > 0){
		a = a/10;
		count++;
	}
	return count;
}

bool isPalindrome(double num){
	if(num - (int)num)
		return false;
	int n = (int) num;
	if(n <= 9)
		return true;

	int digits = numberOfDigits(n);
	while(n >= 10){
		int h = n / (int)pow(10.0, digits-1);
		int l = n % 10;
		if(h != l)
			return false;
		n = (n / 10 ) % (int)pow(10.0, digits-2);
		digits -= 2;
	}
	return true;
}

int main(){
	int a = 1;
	int T;
	int count = 0;
	std::string line;
	std::ifstream input("C-small-attempt0.in");
	std::ofstream output("C-small-attempt0.out");
	getline(input, line);
	std::istringstream iss(line);
	iss>> T;
	for(int i = 1; i <= T; i++){
		output << "Case #" << i << ": ";
		int lowLimit, highLimit;
		getline(input, line);
		std::istringstream iss(line);
		iss >> lowLimit >> highLimit;
		for(int a = lowLimit; a <= highLimit; a++){
			if(isPalindrome(sqrt((double)a)) && isPalindrome(a))
				++count;
		}
		output << count;
		if(i % T)
			output << std::endl;
		count = 0;
	}
	input.close();
	output.close();
}