#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

ifstream input;
ofstream output;

bool FairNSquare(unsigned long long);
bool Panindrom(unsigned long long);
int Range(unsigned long long, unsigned long long);

std::string to_string(double x);

int main(){
	input.open ("input.txt");
	output.open ("output.txt");
	int cases=0;
	input >> cases;

	cout << "START"<<endl;
	cout << "Cases #"<<cases<<endl<<endl;
	string line;
	std::getline(input, line);
	for(int i=0; i<cases; i++){
		/*
		unsigned long long value=0;
		int sucesses=0;		
		std::getline(input, line);
		std::stringstream ss(line);
		while(ss>>value){
			if (FairNSquare(value))	sucesses+=1;
		}*/

		unsigned long long low=0, high=0;
		std::getline(input, line);
		std::stringstream ss(line);
		ss>>low;
		ss>>high;
		int sucesses = Range(low,high);

		cout << "Case #"<<(i+1)<<": "<< sucesses<<endl;
		output << "Case #"<<(i+1)<<": "<< sucesses<<endl;
	}
	input.close();
	output.close();
	cout << "DONE";

	while(1);
	return 0;
}

int Range(unsigned long long low, unsigned long long high){
	int number = 0;
	for(unsigned long long i=low; i<high+1; i++){
		if (FairNSquare(i)){
			number++;
			cout << i << " ";
		}
	}
	cout << endl;
	return number;
}

bool FairNSquare(unsigned long long value){
	if (Panindrom(value)){
		int h = int(sqrt(double(value)));
		if ((h-sqrt(double(value)))==0){
			if (Panindrom(h))	return true;
		}
	}

	return false;
}

bool Panindrom(unsigned long long value){
	if (value<10)	return true;
	
	unsigned long long temp = value;
	int size=1;
	while(temp>10){
		temp/=10;
		size+=1;
	}

	char digits [50];
	std::string str = to_string(value);
	std::strcpy( digits, str.c_str() );

	for(int i=0; i<size/2; i++){
		if (digits[i]!=digits[size-i-1]){
			return false;
		}
	}
	return true;
}

std::string to_string(double x)
{
  std::ostringstream ss;
  ss << x;
  return ss.str();
}