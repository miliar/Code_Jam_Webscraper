#include<iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <math.h>
using namespace std;

int main() {

int curnumb, finnumb, ii, jj, dig, kk, numbers[10], cases;
string line;
ofstream result;
ifstream infile;

infile.open ("A-large.in");
if (infile.good()) 
{
	infile >> cases;
	cout << "The number of cases are:" << endl;
	cout << cases << endl;
}

int orgnumb[cases];
cout << "The numbers are:" << endl;

if (infile.is_open()) 
	{
	for (jj = 0; jj < cases; ++jj)
	{
		infile >> orgnumb[jj];
		cout << orgnumb[jj] << endl;
	}
}
infile.close();

result.open("output");

for (jj = 0; jj < cases; ++jj) 
	{
	cout << "The original number is: " << orgnumb[jj] << endl;
	if (orgnumb[jj] == 0)
	{
		result << "Case #" << jj+1 << ": INSOMNIA" << endl;
		continue;
	}
	
	kk = 0;
	for (ii = 0; ii < 10; ++ii) 
	{
		numbers[ii] = 0;
	};
	for ( ii = 1; ii < 1000001 ; ++ii) 
	{
		curnumb = orgnumb[jj] * ii;
		do 
		{
			dig = curnumb % 10;
			curnumb = curnumb / 10;
				if (numbers[dig] == 0) 
				{
					cout << "So far there have been " << kk << " numbers." << endl;
					numbers[dig]=1;
					kk = kk+1;
				}
		} while(curnumb > 0);
		if (kk >= 10) 
		{
			cout << "All numbers have been there..." << endl;
			cout << "We went to i= " << ii << endl;
			finnumb = ii * orgnumb[jj];
			result << "Case #" << jj+1 << ": " << finnumb << endl;
			break;
		};
	};
	if (kk < 10) 
	{
		cout << "Not all numbers have been there..." << endl;
		result << "Case #" << jj+1 << ": INSOMNIA" << endl;
	};
}
result.close();










return 0;
}

