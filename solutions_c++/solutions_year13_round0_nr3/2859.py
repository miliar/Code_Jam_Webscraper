/*

 *
 */


#include <iostream>
#include <fstream>
#include <algorithm>
#include <stack>
#include <cmath>
#include <sstream>

using namespace std;

template <typename T>
string numToStr(T number)
{
	return dynamic_cast<stringstream *> (&(stringstream() << std::uppercase << number))->str();
}

bool isSquare(int n)
{
	float srt = sqrt(n);
	int x = (int) srt;
	x = x * x;
	return (x == n);
}

bool isPalindrom(int n)
{
	string num = numToStr(n);
	if(num.length() == 1)	return true;
	
	int i,j;
	for(i = 0, j = num.length()-1; (i < num.length()/2) && (j >= ceil(num.length()/2)); i++, j--) {
		if(num[i] != num[j])		return false;
	}
	
	return true;
}


int main()
{
	ifstream inf;
	ofstream outf;
	inf.open("C-small-attempt0.in", ios::in);
	outf.open("output.txt");


	int T;
	int begin, end;
	
	inf >> T;
	for(int k = 0; k < T; k++)
	{
		int count = 0;
		
		inf >> begin;
		inf >> end;
		
		
		for(int i = begin; i <= end; i++)
		{
			if(isSquare(i) && isPalindrom(i) && isPalindrom((int)sqrt(i)))	count++;
		}
		// finish getting one test case
		
		outf << "Case #" << (k+1) << ": " << count;
	
		outf << endl;
		
		
	}


	inf.close();
	outf.close();
	return 0;
}
