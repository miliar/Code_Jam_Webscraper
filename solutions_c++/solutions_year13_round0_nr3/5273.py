#include <iostream>
#include <cmath>
#include <string>
#include <cstdio>
#include <fstream>

using namespace std;

typedef long long int lli;

bool isPalindrome(lli number)
{
	char s[200];
	int length;
	
	length = sprintf(s, "%lld", number);
	
	int j = strlen(s) - 1;
	int i = 0;
	
	while (i < j)
	{
		if (s[i] != s[j])
			return false;
			
		i++;
		j--;
	}
	
	return true;
}

int main()
{
	int test_cases, count;
	lli lowLimit, highLimit;
	lli sqtLow, sqtHigh;
	lli tmpPow;
	
	ifstream fin ("C-small-attempt2.in");
	ofstream fout ("C-small-attempt2.out");
	
	fin>>test_cases;
		
	for (int i = 1; i <= test_cases; i++ )
	{
		fin>>lowLimit>>highLimit;
		
		sqtLow = (lli)sqrt(lowLimit);
		sqtHigh = (lli)sqrt(highLimit);
		count = 0;
		
		for (int j = sqtLow; j <= sqtHigh; j++)
		{
			if (isPalindrome(j))
			{
				tmpPow = j * j;
				
				if (tmpPow >= lowLimit && tmpPow <= highLimit && isPalindrome(tmpPow))
					count++;
			}
		}
		
		fout<<"Case #"<<i<<": "<<count<<endl;
	}
	return 0;
}