// codejam2013_ps3.cpp : main project file.

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace System;
using namespace std;

void calculatePalindrome(unsigned  long long int r1, unsigned  long long int r2,int);
int checkPalindrome(unsigned long long int r);
void writeResult(unsigned long long int count, int caseno);

unsigned long long int nth_power(unsigned long long int a, int n) {
  if(n <= 0)
    return false;
  if(a < 0 && n % 2 == 0)
    return false;
 // a = abs(a);

  unsigned long long int b = pow(a, 1. / n);
 // return pow((double) b, n) == a || pow((double) (b+1), n) == a;
  if(pow((double) b, n) ==a) return b;
  if(pow((double) (b+1), n) == a) return b+1;
  return -1;
}

int main(array<System::String ^> ^args)
{	
	
	ifstream myfile ("C-small-attempt0.in");
	int n = 0;
	if (myfile.is_open())
    {
	  string line1;
	  getline(myfile,line1);
	  std::stringstream ss(line1);
	  ss>>n;
	  int i = 0;
	  while (myfile.good() && i < n)
    {
		string line;
		getline (myfile,line);
		std::stringstream ss1(line);
		unsigned long long int r1 = 0;
		unsigned long long int r2 = 0;
		ss1>>r1;
		ss1 >> r2;		
		i++;
		calculatePalindrome(r1,r2,i);
	}
	myfile.close();
  }
	else cout << "Unable to open file"; 
   system ("pause");
    return 0;
}


int checkPalindrome(unsigned long long int r)
{
	
    unsigned long long int rev = 0;
	unsigned long long int num = r;
	unsigned long long int dig = 0;
	
	while (num > 0)
	{	
		
      dig = num % 10;
      rev = rev * 10 + dig;
      num = num / 10;
	
	}
	
	if(r == rev)
		return 1;
	else return 0;
}
void calculatePalindrome(unsigned long long int r1, unsigned long long int r2, int caseno)
{
	unsigned long long int count = 0;
	for(unsigned long long int i = r1; i <= r2; i++)
	{
		if(checkPalindrome(i) == 1)
		{
			if(checkPalindrome(nth_power(i,2)))
				count++;
		}
	}
	writeResult(count, caseno);
}

void writeResult(unsigned long long int count, int caseno)
{
  fstream filestr;
  filestr.open ("smalloutput.txt", fstream::in | fstream::out | fstream::ate);
  filestr << "Case #"<<caseno << ": "<<count<<"\n";
  filestr.close();
}