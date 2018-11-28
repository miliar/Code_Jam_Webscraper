#include <cmath>
#include <fstream>
#include <iostream>
//#include <cctype>
#include <sstream>
#include <string>

using namespace std;

string itoa(int n);
bool palindrome (const string & str);
bool square (int num);

string itoa(int n)
{
    ostringstream output;
    output << n;   
    return output.str();
}

bool palindrome (const string & str)
{
	int s = str.length();
	for (int i = 0; i < s/2; i++)
		if (str.at(i) != str.at(s-(i+1))) return false;
	return true;
}

bool square (int num)
{
	double sq = sqrt((double)num);
	sq = floor(sq);
	if (sq*sq == num && palindrome(itoa(sq))) return true;
	else return false;
}

int main()
{
	ifstream file("f.txt");
	ofstream out("out.txt");
	string line;
	int t;
	getline(file,line);
	t = atoi(line.c_str());
	for (int a = 1; a <= t; a++)
	{
		int counter = 0;
		int lower, upper;
		getline(file,line);
		istringstream temp(line);
		temp >> lower >> upper;
		while (lower <= upper)
		{
			if (square(lower) && palindrome(itoa(lower))) counter ++;
			lower++;
		}
		out << "Case #" << a << ": ";
		out << counter;
		if (a != t) out << endl;
	}
	out.close();
	system("PAUSE");
	return 0;
}
