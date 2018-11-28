#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string.h>

using namespace std;

int main(){
	ifstream input("B-small-attempt0.in");
	FILE *out;
	out = fopen("out", "w");
	int nCase	= 0;
	input >> nCase;
	double tempSums, result, c, f, x ;
	for(int t = 1; t <= nCase; t++){
		input >> c;
		input >> f;
		input >> x;
		result = 10000000;
		tempSums = 0;
		for(int i = 0; ; i++){
			double tempResult = x / (f * i + 2);
			if(i > 0)
				tempSums += c / (f * ( i - 1) + 2);										
			if(tempResult + tempSums < result)
				result = tempResult + tempSums;
			else
				break;
		}
		fprintf(out, "Case #%d: %.7f\n", t, result);
		if(input.eof())
			break;
	} 		
	return 0;
}
