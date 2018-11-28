// basic file operations
#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

#define MAXTIME 100000
int finalRs;
int data[1001];
int maxP;

int min (int a, int b)
{
		if (a < b)
			return a;
		return b;
}

bool isDone () {
	for (int i = 0; i <= maxP; i++)
		if (data[i] > 0)
			return false;
	return true;
}

void backtrack (int minute) {
	int tempData[1001];
	for (int i = 0; i <= maxP; i++) {
		tempData[i] = data[i];
		//cout << "data[" << i << "] = " << data[i] << " ";
	}
	//cout << "\n";

	for (int i = 0; i < 2; i++) {
		if (i == 1)
		{
			for (int j = 1; j <= maxP; j++)
				data[j] = data[j+1];
			data[maxP] = 0;

			if (minute < finalRs)
			{
				if (isDone())
					finalRs = minute;
				else
					backtrack(minute+1);
			}
			for (int j = 0; j <= maxP; j++)
				data[j] = tempData[j]; 			
		}
		else
		{
			int currentMax = maxP;
			while (data[currentMax] == 0)
				currentMax = currentMax - 1;
			int mid = 1 + currentMax/2;
			for (int j = 1; j <= mid ; j++)
			{
				data[j] ++;
				data[currentMax-j] ++;
				data[currentMax] -= 1;
				if (minute < finalRs)
					backtrack(minute+1);
				data[j] -= 1;
				data[currentMax-j] -= 1;
				data[currentMax]++;

			}
		}
	}
}

int main () {
	int t; // Number of test cases 
	int d;
	int tempP;
	ifstream infile("inputB.txt");
	ofstream outputFile;
	outputFile.open ("outputB.txt");

	infile >> t;

	for (int z = 0; z < t; z++) {
		cout << "Case z = " << z << "\n";
		infile >> d;
	
		for (int i = 0; i < 1001; i++)
			data[i] = 0;

		maxP = 0;
		for (int i = 1; i <= d; i++) 
		{
			infile >> tempP;
			data[tempP] ++;
			if (tempP > maxP)
				maxP = tempP;
		}


		finalRs = maxP;
		backtrack(1);

		outputFile << "Case #" << (z+1) << ": " << finalRs << "\n"; 

	}

	infile.close();
	outputFile.close();
	return 0;
		
}