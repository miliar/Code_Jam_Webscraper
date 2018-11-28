#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <cmath>
#include <string>

using namespace std;

#define FORI(i,n) for(int i = 0; i < n; i++)
#define FORD(i,n) for(int i = n; i >= 0; i--)

bool isPalindrome(int newNumber)
{
	// reverse the integer
	int newNumber1 = newNumber;
	int reversedNo = 0;
	while ( newNumber1 > 0)
	{
		// remove digit from newNumber
		int digit = newNumber1 % 10;
		newNumber1 /= 10;
		
		// add digit to new reversed number
		reversedNo = (reversedNo*10)+digit; 
	}
	// check if it is a palindrome
	if(reversedNo == newNumber)
	{
		return true;
	}
	return false;
}



bool isNice(int a)
{
	if(isPalindrome(a))
	{
		double t = sqrt(a);
		if(fmod(t, 1.0) == 0.0)
		{
			if(isPalindrome((int)t))
			{
				return true;
			}
		}
	}
	return false;
}

int main(int argc, char** argv)
{
	int N = 0;
	int start, end;
	
	cin  >> N;
	int cas = 0;
	FORI(cas, N)
	{
		cin >> start >> end;
		int verdict = 0;
		for(int i = start; i <= end; i++)
		{
			if(isNice(i))
			{
				verdict++;
			}
		}
		cout << "Case #" << (cas + 1)<< ": " << verdict << endl;
	}
	return EXIT_SUCCESS;
}
