#include <stdio.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string>
#include <queue>
#include <cstdio>
#include <fstream>

using namespace std;

unsigned GetNumberOfDigits (unsigned i)
{
	return i > 0 ? (int) log10 ((double) i) + 1 : 1;
}

bool isPalindrome(int number){   // make sure that the number can be read from the right and left

	// if the number contains only one digit return true
	if(GetNumberOfDigits(number) == 1) return true;

	string n = itoa(number,new char[33], 10);
	int length = strlen(n.c_str());
	bool flag = true;

	for(int i = 0; i != length / 2; i++)
	{
		if(flag)
		{
			if(n[i] != n[length - i - 1]) // check the characters match
			{
				flag = false;
			}
		}
	}
	return flag;
}

int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	ofstream outputFile("output.txt");
	int input;
	scanf("%d", &input);
	for (int i = 0; i < input; i++)
	{
		int start;
		int end;
		cin >> start;
		cin >> end;
		int palindromeNumber = 0;

		for (int i = start; i < end +1 ; i++)
		{
			// check to see if the number is Palindrome
			bool firstCheck = isPalindrome(i);

			// continue the loop if the first check is false
			if(firstCheck == false) continue;

			// check to see if the number is square
			bool secondCheck;
			float result = sqrt(i);
			result == (int)result ?  secondCheck = true : secondCheck = false;

			// continue the loop if the second check is false
			if(secondCheck == false) continue;

			// check to see if the square root of the number is also a Palindrome
			bool thirdCheck =  isPalindrome((int)result);

			// continue the loop if the third check is false
			if(thirdCheck == false) continue;

			// all conditions apply, increase count by one
			palindromeNumber++;
		}

		outputFile << "Case #" << i + 1 << ": " << palindromeNumber << "\n";
	}

	outputFile.close();
	return 0;
}