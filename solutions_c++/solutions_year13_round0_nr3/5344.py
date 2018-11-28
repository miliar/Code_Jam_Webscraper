#include<iostream>
#include<fstream>
#include<sstream>
#include<cmath>
#include<string>
using namespace std;

bool isPalindrome(string num){
	if(num.size() == 0 || num.size() == 1){
		return true;
	}
	else if(num[0] == num[num.size()-1]){
		return isPalindrome(num.substr(1, num.size()-2));
	}
	else
		return false;
} 

bool isPerfectSquare(double num){
	int sq = (int)(sqrt(num));
	
	return((sq * sq) == num);
}

bool isFairAndSqaure(string num, double numInt){
	bool palindrome, square, squareIsPalindrome;
	stringstream numStr(stringstream::in | stringstream::out);
	
	palindrome = isPalindrome(num);
	square = isPerfectSquare(numInt);
	
	if(square){
		numStr << sqrt(numInt);
		squareIsPalindrome = isPalindrome(numStr.str());
		
		return (palindrome && square && squareIsPalindrome);
	}
	return false;
}

int main(){
	ifstream inFile("in.txt");
	ofstream outFile("out.txt");
	stringstream num(stringstream::in | stringstream::out);
	int testCases;
	double min, max;
    int	fairAndSquare = 0;
	string digit;
	
	if(inFile.is_open()){
		inFile >> testCases;
		
		for(int i = 1; i <= testCases; i++){
			inFile >> min;
			inFile >> max;
			fairAndSquare = 0;
			for(double j = min; j <= max; j++){
				num.str("");
				num << j;
				if(isFairAndSqaure(num.str(), j)){
					++fairAndSquare;
				}
			}
			outFile << "Case #" << i << ": " << fairAndSquare << endl;
		}
	}

	return 0;
}