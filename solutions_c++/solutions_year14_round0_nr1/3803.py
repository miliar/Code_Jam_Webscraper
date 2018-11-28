#include <stdio.h>
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	int t, n1, n2, array1[4][4], array2[4][4], result1[4], result2[4], n=0, i, j, result;
	ifstream input;
	ofstream output;
	input.open("input.in");
	output.open("output.txt");
	input>>t;
	for (int l = 1; l <= t; l++) {
		input>>n1;
		for (i = 0; i < 4; i++) {
			for (j = 0; j < 4; j++) {
				input>>array1[i][j];
			}
		}
		input>>n2;
		for (i = 0; i < 4; i++) {
			for (j = 0; j < 4; j++) {
				input>>array2[i][j];
			}
		}
		for (i = 0; i < 4; i++) {
			result1[i]=array1[n1-1][i];
		}
		for (i = 0; i < 4; i++) {
			result2[i]=array2[n2-1][i];
		}
		for (i = 0; i < 4; i++) {
			for (j = 0; j < 4; j++) {
				if (result1[i]==result2[j]) {
					n++;
					result=result1[i];
				}
			}
		}
		if (n==0) {
			output<<"Case #"<<l<<": Volunteer cheated!\n";
		}
		else if (n==1) {
			output<<"Case #"<<l<<": "<<result<<"\n";
		}
		else if (n!=1 && n!=0) {
			output<<"Case #"<<l<<": Bad magician!\n";
		}
		n=0;
	}
	input.close();
	output.close();
	return 0;
}

