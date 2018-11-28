// GCJ13.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <math.h>
using namespace std;

inline char charToInt( char ch ) {
  return (ch - '0');
}

bool isPalindrome(int x)
{
	char buffer[4] = {0};
	itoa (x,buffer,10);
	int size = strlen(buffer);
	for(int i = 0; i<size/2; i++)
	{
		if(buffer[i] != buffer[size -i -1])
		{
			return false;
		}
	}
	return true;
}

int main()
{
	  ifstream in("C-small-attempt0.in" );      // A-tiny-practice.in    // A-small-practice.in    // A-large-practice.in
	  ofstream outfile("C-small-attempt0.out");
	  string line;
	  int tc; 
	  cin >> tc;
	  //tc = 1;
	  for(int tci = 0; tci < tc; tci++)
	  {
		int a = 0;
		int b = 0;
		cin >> a;
		cin >> b;		
		
		int count = 0;
		for(int i = a;i<=b;i++)
		{
			int c = i;
			double sqc = sqrt((double)c);
			int sqci = (int)sqc;
			if(sqc == (sqci))
			{
				if(isPalindrome(sqci) && isPalindrome(c))
				{
					count++;
				}
			}
		}
		
		cout<<"Case #"<<tci+1<<": "<<count<<endl;	
  }
}

