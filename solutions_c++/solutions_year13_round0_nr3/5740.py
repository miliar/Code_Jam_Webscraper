#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

bool palindrome(unsigned long long n);
string inttostring(short n);

int main()
{
	string lines;
	ofstream output("output.txt");
	vector<long long> fairandsquare(0,0);
	for (long long p = 0; p < 10000001; p++)
	{
		if (palindrome(p))
		{
			long long q = p*p;
			if (palindrome(q))
			{
				output << q << ',';
				fairandsquare.resize(fairandsquare.size()+1);
				fairandsquare[fairandsquare.size()-1] = q;
			}
		}
	}
	output.close();
	ifstream input("input.txt");
	ofstream output2("output2.txt");
	getline(input, lines);
	int length = atoi (lines.c_str());
	for (short p = 0; p < length; p++)
	{
		getline(input, lines);
		int min = atoi (lines.substr(0, lines.find(' ')).c_str()), max = atoi (lines.substr(lines.find(' ')+1).c_str()), counter = 0;
		for (int q = 0; q < fairandsquare.size(); q++)
		{
			if (fairandsquare[q] >= min)
			{
				if (fairandsquare[q] <= max)
					counter++;
				else
					break;
			}
		}
		output2 << "Case #" << inttostring(p+1) << ": " << counter << endl;
	}
	input.close();
	output2.close();
}

bool palindrome(unsigned long long n)
{
	bool isapalindrome = 1;
	short digits = 0;
	short number[14];
	for (int p = 0; n > 0; p++)
	{
		number[p] = n%10;
		n/=10;
		digits++;
	}
	for (int p = 0; p < digits/2; p++)
	{
		if (number[p] != number[digits-p-1])
		{
			isapalindrome=0;
			break;
		}
	}
	return isapalindrome;
}

string inttostring(short n)
{
	string numberindecform, reversednum;
	do
	{
		reversednum+=char(n%10 + '0');
		n/=10;
	} while (n > 0);
	for (short p = reversednum.size()-1; p >= 0; p--)
		numberindecform += reversednum[p];
	return numberindecform;
}