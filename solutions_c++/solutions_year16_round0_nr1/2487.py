#include <stdio.h>
#include <iostream>
#include <fstream>

using namespace std;

int main(){
	int sheeps[10];
	int seenCount = 10;

	for(int i = 0; i < 10 ; i++){
		sheeps[i] = i;
	}

	ifstream infile("A-large.in");
	ofstream outfile("A-large.out");

	int number;
	int length;
	int j = 1;
	infile >> length;
	int inputs[length];

	for(int i = 0; i < length; i++){
		infile >> inputs[i];
	}

	for(int i = 0; i < length; i++){
		number = inputs[i];
		if(number != 0){
			seenCount = 10;
			for(int k = 0; k < 10 ; k++){
				sheeps[k] = i;
			}
		    for(j = 1; seenCount > 0 ;j++){
		    	int dividedNumber;
		    	dividedNumber = number * j;

			    for(;dividedNumber != 0;)
			    {
			    	int n1 = dividedNumber%10;
			    	dividedNumber /= 10;

			    	if(sheeps[n1] != -1){
				    	sheeps[n1] = -1;
				    	seenCount--;
			    	}
			    }
		    }

			outfile << "Case #"<< i+1 << ": " << number * (j-1) << endl;
		}
		else{
			outfile << "Case #"<< i+1 << ": INSOMNIA" << endl;
		}

	}
	return 0;
}