#include <iostream>
#include <math.h>
#include <fstream>
#include <string>

using namespace std;

bool IsPalindrome(int number)
{
	int temp;
	if(number<10)
		return true;
	else if(number>10 && number<100)
	{
		temp = number%10;
		number = number/10;
		if(number == temp)
			return true;
	}
	else if(number>100 && number<1000)
	{
		temp = number%10;
		number = number/100;
		if(number == temp)
			return true;
	}
	return false;
}

int main()
{
	int T, lowLimit, upLimit, lowSqrLimit, upSqrLimit, count;
	ifstream inFile;
	ofstream oFile;
	inFile.open("input.txt");
	inFile >> T;
	
	for(int test=0; test<T; test++)
	{
		count = 0;
		inFile >> lowLimit;
		inFile >> upLimit;
		lowSqrLimit = sqrt(lowLimit);
		upSqrLimit = sqrt(upLimit);

		for(int i=lowSqrLimit; i<=upSqrLimit; i++)
		{
			if(IsPalindrome(i) && IsPalindrome(i*i))
				if((i*i) >= lowLimit && (i*i) <= upLimit) 
					count++;
		}
		oFile.open ("output.txt", ios::out | ios::app);
		oFile<<"Case #"<<test+1<<": "<<count<<endl;
		oFile.close();
	}
	inFile.close();
	return 0;
}