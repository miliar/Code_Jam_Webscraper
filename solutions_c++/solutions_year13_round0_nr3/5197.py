#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string>


using namespace std;

bool isPalindrome(int i)
{
	char digits[256];
	sprintf(digits, "%i", i);
	int numDigits = strlen(digits);

	for(int i=0; i< numDigits/2; i++)
	{
		if( digits[i] != digits[numDigits-1-i]) return false;
		
	}
	return true;
}

int numFairSquares(int lower, int upper)
{
	int num = 0;
	for(int i=lower; i<=upper;i++)
	{
		if(sqrt(i) != (int)sqrt(i)) continue;
		if(!isPalindrome(i)) continue;
		if(!isPalindrome(sqrt(i))) continue;
		num++;
	}
	return num;
}


int main()
{
	int cases;
	cin >> cases;
	for(int i=0; i<cases;i++)
	{
		int low,high;
		cin >> low;
		cin >> high;
		cout << "Case #" << i+1 <<": "<<numFairSquares(low,high)<<endl;
	}
}