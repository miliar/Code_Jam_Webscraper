#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

bool isPalindromeNumber (long long);
bool isFairAndSquare (long long);

int main ()
{
	ifstream infile;
	ofstream outfile;
	long long lowerBound, upperBound, count, testCases;
	
	infile.open("C-small-attempt0.in");
	outfile.open("output.txt");
	infile >> testCases;
	
	for (long long t=0; t<testCases; t++)
	{
		count = 0;;
		infile >> lowerBound;
		infile >> upperBound;
		for (long long i=lowerBound; i<=upperBound; i++)
		{
			if (isFairAndSquare(i))
				count++;
		}
		
		outfile << "Case #" << t+1 << ": " << count << endl;
	}
	infile.close();
	outfile.close();
	return 0;
}

bool isFairAndSquare (long long input)
{
	if ((pow(floor(sqrt(input)),2)) == input)
	{
		if ((isPalindromeNumber(input)) && isPalindromeNumber(sqrt(input)))
			return true;
	}
	return false;
}

bool isPalindromeNumber (long long input)
{
	int digitArray [20]; 
	long long tempInput;
	int index = 0;
	tempInput = input;
	
	if (tempInput < 10) return true;
	while (tempInput != 0)
	{
		digitArray[index] = tempInput % 10;
		tempInput /= 10;
		index++;
	}
	
	for (int i=0; i<index-1; i++)
	{
		if (digitArray[i] != digitArray[index-1-i])
			return false;
	}
	return true;
}
