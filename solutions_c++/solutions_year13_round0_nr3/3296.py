#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <array>
#include <math.h>
#include <limits>
#include <cstring>

using namespace std;

bool isPalindrome(long long num){
	char pal[101];
	itoa(num, pal, 10);

	int digits = strlen(pal);

	bool isPal = true;
	for(int i=0;i<digits/2;i++){
		if(pal[i] != pal[digits-i-1]) isPal = false;
	}
	return isPal;
}

vector<long long> printPalins(){
	vector<long long> out;
	for(long long i=1;i<1001;i++){
		if(isPalindrome(i)){
			if(isPalindrome(i*i)){
				out.push_back(i*i);
			}
		}
	}
	return out;
}

int main(){
	
	istream * stream;
	ifstream myfile;
	myfile.open("C-small-attempt1.in");

	ofstream outfile;
	outfile.open("output.txt");
	
	vector<long long> blah = printPalins();

	if(myfile.is_open()){
		stream = &myfile;
	}else{
		stream = &cin;
	}


	int num;
	(*stream) >> num;
	
	int count;

	long long min, max;
	for(int i=0;i<num;i++){
		
		(*stream) >> min >> max;
		count = 0;

		/*
		min = ceil(sqrt(min+0.0));
		max = floor(sqrt(max+0.0));

		for(long long i=min;i<=max;i++){
			if(isPalindrome(i)){
				if(isPalindrome(i*i)){
					count++;
				}
			}
		}*/

		for(vector<long long>::iterator it = blah.begin(); it!=blah.end(); ++it){
			if(min<=*it && *it<=max){
				count++;
			}
		}

		outfile << "Case #" << i+1 << ": " << count << endl;
	}
}