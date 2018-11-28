#include <iostream>
#include <fstream>
#include <math.h>
#include <string>
using namespace std;

int *expand(int length, string arrString){
	int *arr = new int[length];
	for (int i = 0; i < length; i++){
		arr[i] = arrString.at(i) - '0';
	}
	
	return arr;
}

int parse(int length, int *arr){
	int total = 0, numFriends = 0;
	for (int i = 0; i < length; i++){
		if (total < i){
			int extra = i - total;
			numFriends += extra;
			total += extra;
		}
		total += arr[i];
	}
	delete arr;
	return numFriends;
}

int main(){
	ifstream input("A_large.in");
	ofstream output("output.txt");
	int numberOfCases, maxShyness, i = 0;
	string shynessArray;
	
	input >> numberOfCases;
	while (input >> maxShyness >> shynessArray){
		int length = maxShyness + 1;
		output << "Case #" << ++i << ": " << parse(length, expand(length, shynessArray)) << "\n";
	}
}