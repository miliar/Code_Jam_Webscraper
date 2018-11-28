#include <algorithm>
#include <iostream>
#include <string>
#include <math.h>
#include <vector>
#include <fstream>

using namespace std;

struct records
{
	string coinCode;
	long* divisors = new long[11];
};

long convertFromBase(string input, long number){
	long count = 1;
	long myNumber = 0;
	for (int i = 0; i < input.length(); ++i)
	{
		int digit = (int)input[input.length() - count] - '0';
		myNumber += pow(number,count-1)*digit;
		count++;
	}
	return myNumber;
}

void resetArray(long* arr) {
	for (int i = 0; i < 11; ++i)
	{
		arr[i] = -1;
	}
	arr[0] = 0;
	arr[1] = 0;
}


std::vector<string> generateAllStrings(long len){
	string temp = "";
	std::vector<string> result;
	for (int i = 0; i < len; ++i)
		temp = temp + '0';
	

	for (int i = 0; i < len; ++i)
	{
		string another = temp;
		for (int j = 1; j <= i; ++j)
		{
			another[another.length()-j] = '1';
		}
		do
    	{	
       		result.push_back(another);
    	}
    	while (std::next_permutation(another.begin(), another.end()));
	}
	temp = "";
	for (int i = 0; i < len; ++i)
		temp = temp + '1';
	result.push_back(temp);	
	return result;
}

std::vector<struct records> produceCoins(long lengthCoinCode){
	
	long SIZE = (long)pow(2,lengthCoinCode);
	std::vector<struct records> myResult;
	std::vector<string> allStrings = generateAllStrings(lengthCoinCode);
	for (int i = 0; i < allStrings.size(); ++i)
	{	struct records res;
		string tempo = allStrings[i];
		if(tempo[tempo.length()-1] == '1' && tempo[0] == '1'){
			res.coinCode = tempo;
			resetArray(res.divisors);
			myResult.push_back(res);
		}
	}
	return myResult;
}

bool checkPrime(long number) {
	if(number == 2) return true;
	else if(number <= 0 || number % 2 == 0) return false;
	else {
		long divisor = 3;
		for (int i = divisor; i <= ((int)(sqrt((double)number))) +1; i+=2)
		{
			if(number%i == 0){
				return false;
			}
		}
	}
	return true;
}

long findANonPrime(long number) {
	//cout << "In findANonPrime " << number << endl;
	if(number%2 == 0) return 2;
	for (int i = 3; i < ((int)(sqrt((double)number))) + 1; i+=2)
		{
			//cout << i << endl;
			if(number%i == 0) return i;
		}	
	return -1;	
}

struct records fillInOneRecord(struct records input)
{
	for (int i = 0; i < 9; ++i)
	{
		//cout << "Point 1" << endl;
		long number = convertFromBase(input.coinCode,i+2);
		//cout << "Point 2" << endl;
		input.divisors[i+2] = findANonPrime(number);
		//cout << "Point 3" << endl;
		if(input.divisors[i+2] == -1) return input;
		//cout << "Point 4" << endl;

	}
	return input;
}

std::vector<struct records> fillInDivisors(std::vector<struct records> list){
	for (int i = 0; i < list.size(); ++i)
	{
		list[i] = fillInOneRecord(list[i]);
		cout << "In fillInDivisors " << i << endl;
	}
	return list;
}

bool checkMyArray(long* arr){
	for (int i = 0; i < 9; ++i)
	{
		if(arr[i+2] == -1) return false;
	}
	return true;
}

std::vector<struct records> refineResults(std::vector<struct records> list){
	std::vector<struct records> result;
	for (int i = 0; i < list.size(); ++i)
	{
		

		if(checkMyArray(list[i].divisors)) result.push_back(list[i]);
	}
	return result;
}

std::vector<struct records> refine(std::vector<struct records> list){
	std::vector<struct records> result;
	for (int i = 0; i < list.size(); ++i)
	{
		

		if(list[i].coinCode != "") result.push_back(list[i]);
	}
	cout << "returning from refine " << result.size() << endl;
	return result;
}


int main(){
	ifstream input("inputs.txt");
	ofstream output("output.txt");
	long numberOfInputs;
	input >> numberOfInputs; 
	int counter = 0;
	while (numberOfInputs > 0){
		counter++;
		long lengthCoinCode,requiredCoins;
		input >> lengthCoinCode >> requiredCoins;
		output << "Case #" << counter << ":" << endl;
		std::vector<struct records> result = refineResults(fillInDivisors(refine(produceCoins(lengthCoinCode))));
		int counter2 = 0;
		for (int i = 0; i < result.size(); ++i)
		{	if(counter2 >= requiredCoins) break;
			output <<result[i].coinCode << " ";
			for (int j = 0; j < 9; ++j)
			{
				output << result[i].divisors[j+2] << " ";
			}
			output << endl;
			counter2++;
		}
		numberOfInputs--;
	}
	input.close();
	output.close();

	return 0;
}
