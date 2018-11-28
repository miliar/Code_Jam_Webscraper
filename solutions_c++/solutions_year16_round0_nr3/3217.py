#include <iostream>
#include <string>
#include <math.h>
#include <cstdlib>
#include <map>
#include <sstream>
#include <fstream>
using namespace std;
bool isPrime(long long int num);
string reverse(string input);
string trim(string input);
string incrementOne(string input);
int findDivisor(long long int num);
long long int interpretBin(string input, int inputnumber);
int stringtoInt(string input);
string IntToString(long int input);
string generate(int number);
string generateOne(int number);
bool hasPrime(string input);
bool readfile(string input);
int main(){

	int numberOfInput;
	cin >> numberOfInput;
	string test = "155423";

	
	for (int m = 0; m < numberOfInput; m++){
		int j,n;
		cin >> n >> j;
		int counter = 0;
		string input;
		input = "";

		input = generate(n);
		cout << "Case #"<<m+1<<":" << endl;
		//input = "1000000000000101";
		while (counter < j){
			if (!hasPrime(input)){
				cout << input;
				for (int i = 2; i < 11; i++){
					cout << " " << findDivisor(interpretBin(input, i));
				}
				cout << endl;
				counter++;
			}
			input = incrementOne(incrementOne(input));
			//cout << " getting while " << endl;
		}
	}
	
	string stop;
	cin >> stop;

}


bool hasPrime(string input){
	bool two = isPrime(interpretBin(input, 2));
	//cout << interpretBin(input, 2)<<endl;
	bool three = isPrime(interpretBin(input, 3));
	bool four = isPrime(interpretBin(input, 4));
	bool five = isPrime(interpretBin(input, 5));
	bool six = isPrime(interpretBin(input, 6));
	bool seven = isPrime(interpretBin(input, 7));
	bool eight = isPrime(interpretBin(input, 8));
	bool nine = isPrime(interpretBin(input, 9));
	bool ten = isPrime(interpretBin(input, 10));
	
	return (two || three || four || five || six || seven || eight || nine || ten);
}

string incrementOne(string input){
	string output = reverse(trim(input));
	if (output == ""){ return "1"; }
	
	int length = input.length();
	for (int i = 0; i < length; i++){
		if (output[i] == '0'){
			output[i] = '1';
			return reverse(output);
		}
		output[i] = '0';
	}
	if (trim(input) == generateOne(input.length())){
		return "1" + output;
	}
	return output;
}
string trim(string input){
	string output = "";
	int length = input.length();
	bool one = false;
	for (int i = 0; i < length; i++){
		if (input[i] == '0' && !one){
			
		}
		else{
			output += input[i];
			one = true;
		}
	}
	return output;
	
}

string reverse(string input){
	string output = "";
	int length= input.length();
	for (int i = 0; i < length; i++){
		output += input[length-1 - i];
	}
	return output;
}

long long int interpretBin(string input,int inputnumber){
	const string s = input;
	unsigned long value = strtoul(s.c_str(), NULL, inputnumber);
	
	return value;
	
}

string generateOne(int number){
	string output = "";
	for (int i = 0; i < number; i++){
		output += '1';
	}
	return (output);
}

string generate(int number){
	string output = "1";
	for (int i = 0; i < number-2; i++){
		output += '0';
	}
	return (output+'1');
}

int findDivisor(long long int num){
	
	if (num % 2 == 0)
		return 2;
	else
	{
		bool prime = true;
		int divisor = 3;
		long long int num_d = static_cast<long long int>(num);
		long long int upperLimit = static_cast<int>(sqrt(num_d) + 1);
		while (divisor <= upperLimit)
		{
			if (num % divisor == 0)
				return divisor;
			divisor += 2;
		}
	}
}


int stringtoInt(string input){
	stringstream ss(input);
	int x;
	ss >> x;
	return x;
}


string IntToString(long int input){
	stringstream ss;
	ss << input;
	return ss.str();
}

bool isPrime(long long int num)
{
	if (num <= 1)
		return false;
	else if (num == 2)
		return true;
	else if (num % 2 == 0)
		return false;
	else
	{
		bool prime = true;
		long long int divisor = 3;
		long long int num_d = static_cast<long long int>(num);
		int upperLimit = static_cast<long long int>(sqrt(num_d) + 1);

		while (divisor <= upperLimit)
		{
			if (num % divisor == 0)
				prime = false;
			divisor += 2;
		}
		return prime;
	}
}

bool readfile(string input){
	ifstream fin("sprimes.txt");
	fin.seekg(0, ios::end);
	int last = fin.tellg();

	fin.seekg(0, ios::beg);
	int first = fin.tellg();

	string word = input;
	int middle = 0;
	string search;
	bool found = false;
	
	while (!fin.eof())
	{
		middle = (first + last) / 2;
		cout << first << " " << last << " " << " " << middle;  //**
		fin.seekg(middle);
		fin >> search;

		cout << search << endl;  //**
		if (search < word)
		{
			first = middle + 1;
			cout << "a";  //**
		}
		else if (search > word)
		{
			last = middle - 1;
			cout << "b";  //**
		}
		else
		{
			return true;
			
		}
		cout << first << " " << last << " " << " " << middle << endl;  //**

	}
	return false;
}