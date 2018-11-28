#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <cmath>
using namespace std;

template <typename T>
  string NumberToString ( T Number )
  {
     ostringstream ss;
     ss << Number;
     return ss.str();
  }
bool isPalindrome(string number);
bool isSquareOfPalindrom(double number);
int main()
{
	ifstream cin("C-small-attempt0.in");
	ofstream cout("C-small-attempt0.out");
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		int first,second;
		cin >> first >> second;
		int count = 0;
		for (int i = first; i <= second; i++)
		{
			if (isPalindrome(NumberToString(i)) && isSquareOfPalindrom(i))
				count++;
		}
		cout << "Case #"<< i + 1 << ": " << count << endl; 
	}
	return 0;
}
bool isPalindrome(string number)
{
		string s1 = "";
		string s2 = "";
		for(int i = 0,j = number.size() - 1; i < number.size()/2; i++,j--)
		{
			s1 += number[i];
			s2 += number[j];
		}
		if (s1 == s2)
			return true;
	return false;
}

bool isSquareOfPalindrom(double number)
{
	double s = sqrt(number);
	if ((int) s == s)
	{
		string str = NumberToString((int) s);
		return isPalindrome(str);
	}
	return false;
}
