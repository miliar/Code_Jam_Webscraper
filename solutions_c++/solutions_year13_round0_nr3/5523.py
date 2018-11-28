#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <math.h>

using namespace std;

void checkPossible (int numCase);
bool isPalindrome (int i);
string convertInt(int number);
string reverse_str(string str);

double a = 1;
double sqrta = 0;
int roundSqrta = 0;
double b = 1;
double sqrtb = 0;
int roundSqrtb = 0;
int total = 0;

int main (int argc, char *argv[])
{
	int numCase;
	cin >> numCase;
	for (int i = 0; i < numCase; ++i){
		cin >> a;
		cin >> b;
		sqrta = sqrt(a);
		roundSqrta = (int) sqrta;
		sqrtb = sqrt(b);
		roundSqrtb = (int) sqrtb;
		checkPossible(i);
		total = 0;
	}

}

void checkPossible (int numCase)
{
	for (int i = roundSqrta; i <= roundSqrtb +1 ; ++i)
	{
		int squarei = i*i;
		if (squarei >= a & squarei <= b)
		{
			if (isPalindrome(i) & isPalindrome(squarei))
				++ total;
		}
	}
	ofstream outputFile;
	outputFile.open("C-small.out", ios::app);
	outputFile << "Case #" << numCase + 1 << ": " << total << endl;
	
}

bool isPalindrome (int i)
{
	string possibleString = convertInt(i);
	string reverseString = reverse_str(possibleString);
	if (possibleString.compare(reverseString) == 0)
		return true;
	return false;
}

string convertInt(int number)
{
   stringstream ss;
   ss << number;
   return ss.str();
}

string reverse_str(string str){
 reverse(str.begin(), str.end());
 return str;
}
