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

int charToInt (char c)
{
	if (c == 'i')
		return 2;
	if (c == 'j')
		return 3;
	return 4;
}

int abs(int a) {
	if (a < 0)
		return -a;
	return a;
}

int main () {
	// 1 ~ 1
	// i ~ 2
	// j ~ 3
	// k ~ 4
	int product[5][5];
	product[1][1] = 1; product[1][2] =  2;  product[1][3] = 3;  product[1][4] =  4;
	product[2][1] = 2; product[2][2] = -1;  product[2][3] = 4;  product[2][4] = -3;
	product[3][1] = 3; product[3][2] = -4;  product[3][3] = -1;  product[3][4] = 2;
	product[4][1] = 4; product[4][2] =  3;  product[4][3] = -2; product[4][4] = -1;


	int t; // Number of test cases 
	int l,x;
	int temp;
	string inputString;
	short dp[10001];
	short dp2[10001];

	ifstream infile("inputC.txt");
	ofstream outputFile;
	outputFile.open ("outputC.txt");

	infile >> t;

	for (int z = 0; z < t; z++) {
		cout << "test case : " << (z + 1) << "\n";
		infile >> l >> x;
		infile >> inputString;



		dp[0] = charToInt(inputString[0]);

		for (int i = 1; i < l*x; i++)
		{
			if (dp[i-1] > 0)
				dp[i] = product[dp[i-1]][charToInt(inputString[i % l])];
			else
				dp[i] = -product[-dp[i-1]][charToInt(inputString[i % l])];
		}


		dp2[l*x-1] = charToInt(inputString[l-1]);

		for (int i = l*x-2; i >= 0; i--)
		{
			if (dp2[i+1] > 0)
				dp2[i] = product[charToInt(inputString[i % l])][dp2[i+1]];
			else
				dp2[i] = -product[charToInt(inputString[i % l])][-dp2[i+1]];
		}

		bool achievable = false;
		int temp;
		int tempSign;
		int midProduct;
		for (int pos1 = 0; pos1 < l*x; pos1 ++)
			if (dp[pos1] == charToInt('i') && !achievable)
			{
				midProduct = 1;
				for (int pos2 = pos1 + 2; pos2 < l*x; pos2++) {
					if (midProduct > 0)
						midProduct = product[midProduct][charToInt(inputString[(pos2-1) % l])];
					else
						midProduct = -product[-midProduct][charToInt(inputString[(pos2-1) % l])];
					
					if (!achievable)
					{	
						if (dp2[pos2] == charToInt('k') && midProduct == charToInt('j'))
							{
								achievable = true;
								break;
							}
					}
					else
						break;
				}
			}
	
		string finalRs;

		if (achievable)
			finalRs = "YES";
		else
			finalRs = "NO";

		outputFile << "Case #" << (z+1) << ": " << finalRs;
		if (z + 1 < t)
			outputFile << "\n"; 

	}

	infile.close();
	outputFile.close();
	return 0;
		
}
