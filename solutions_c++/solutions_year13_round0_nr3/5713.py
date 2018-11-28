/***********************************************************************************************************************
Author: Sagar Rakshe
Date: 12/04/2013
Problem Statement: 



Little John likes palindromes, and thinks them to be fair (which is a fancy word for nice). A palindrome is just an integer that reads the same backwards and forwards - so 6, 11 and 121 are all palindromes, while 10, 12, 223 and 2244 are not (even though 010=10, we don't consider leading zeroes when determining whether a number is a palindrome).

He recently became interested in squares as well, and formed the definition of a fair and square number - it is a number that is a palindrome and the square of a palindrome at the same time. For instance, 1, 9 and 121 are fair and square (being palindromes and squares, respectively, of 1, 3 and 11), while 16, 22 and 676 are not fair and square: 16 is not a palindrome, 22 is not a square, and while 676 is a palindrome and a square number, it is the square of 26, which is not a palindrome.

Now he wants to search for bigger fair and square numbers. Your task is, given an interval Little John is searching through, to tell him how many fair and square numbers are there in the interval, so he knows when he has found them all.
Solving this problem

Usually, Google Code Jam problems have 1 Small input and 1 Large input. This problem has 1 Small input and 2 Large inputs. Once you have solved the Small input, you will be able to download any of the two Large inputs. As usual, you will be able to retry the Small input (with a time penalty), while you will get only one chance at each of the Large inputs.
Input

The first line of the input gives the number of test cases, T. T lines follow. Each line contains two integers, A and B - the endpoints of the interval Little John is looking at.
Output

For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is the number of fair and square numbers greater than or equal to A and smaller than or equal to B. 
***********************************************************************************************************************/
 
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

int square[1001] ={0};

void initialize()
{
	for (long long int i = 1; i < 33; ++i)
		square[i*i]=1;
}

bool isPalindrome(unsigned int num)
{
	unsigned int rev=0,n;
	int dig;
	
	n = num;
	rev = 0;
	while (num > 0)
	{
	    dig = num % 10;
	    rev = rev * 10 + dig;
	    num = num / 10;
	}

	if(rev==n)
		return true;
	return false;
}

int main(void)
{
	unsigned int number;
	int test,count=0,a,b;

	cin>>test;

	initialize();
	for (int i = 1; i <= test; ++i)
	{
		cin>>a>>b;
		count=0;
		for(int j=a;j<=b;++j)
			if(square[j] && isPalindrome(j) && isPalindrome(sqrt(j)))
			{
				count++;
			}	
			cout<<"Case #"<<i<<": "<<count<<endl;
	}

	return 0;
}
