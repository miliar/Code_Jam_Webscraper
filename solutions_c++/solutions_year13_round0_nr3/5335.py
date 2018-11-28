#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <sstream>
#include <math.h>

char isPalindrome(int number){
	std::string text;
	std::stringstream convert;

	convert << number;

	text = convert.str();

	for(int ctrChar = 0; ctrChar < text.length()/2; ctrChar++){
		if(text[ctrChar] != text[text.length() - (ctrChar+1)]){
			return 0;
		}
	}

	return 1;
}

int main(){
	int testcases;

	std::cin >> testcases;

	for(int ctrCase = 0; ctrCase < testcases; ctrCase++){

		int found=0;

		int lower;
		int upper;
	
		std::cin >> lower >> upper;

		for(int ctrCheck = lower; ctrCheck <= upper; ctrCheck++){
			if(isPalindrome(ctrCheck)){
				double root = sqrt(ctrCheck) + 0.01;
				if((int)root * (int)root == ctrCheck){
					if(isPalindrome(root)){
						found++;
					}
				}
			}
		}

		std::cout << "Case #" << ctrCase+1 << ": " << found << std::endl;	

	}

	return 0;
}
