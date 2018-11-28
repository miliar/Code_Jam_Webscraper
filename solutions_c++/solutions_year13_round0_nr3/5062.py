// C_ConsoleApplication.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <math.h>

using namespace std;

std::vector<std::string> &split(const std::string &s, char delim, std::vector<std::string> &elems) {
    std::stringstream ss(s);
    std::string item;
    while(std::getline(ss, item, delim)) {
        elems.push_back(item);
    }
    return elems;
}

std::vector<std::string> split(const std::string &s, char delim) {
    std::vector<std::string> elems;
    return split(s, delim, elems);
}

bool isPalindrome(const long double num)
{
	long double b = 0, c = num, d = 10, param, intpart;
	while(c!=0)
	{
		b = b * d + fmod(c, d);
		param = c / d;
		modf(param , &intpart);
		c = intpart;
	}
	if(num == b) return true;
	return false;
}

const long double zero = 0;
bool isSquare(const long double num)
{
	long double b = 0, fractpart, intpart;
	b = sqrtl(num);
	fractpart = modf(b , &intpart);
	if(fractpart == zero) return isPalindrome(b);
	return false;
}

int ANS(ifstream &infile, string &str)
{	
	long double i;
	int answ = 0;	
	
	vector<string> x = split(str, ' ');
	const long double A = stoi(x[0]);
	const long double B = stoi(x[1]);

	i = A;
	while(i <= B)
	{
		if(isPalindrome(i) && isSquare(i)) ++answ;
		++i;
	}
	
	return answ;
}

void test()
{
	string str1, str2;
	ifstream infile;
	infile.open ("data.out");
	ifstream testfile;
	testfile.open ("test.out");

	int n = 0;
	while(getline(infile, str1) && getline(testfile, str2))
	{
		++n;
		if(str1.compare(str2) != 0) cout << str1 << ":::" << str2 << endl;		
	}
	cout << "Compared " << n << " cases!" << endl;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ofstream outfile( "data.out" , ios::app );
	
	string str;
    ifstream infile;
    infile.open ("data.in");
	getline(infile, str);
    int const cases = stoi(str);
	int n = 1;	
	while(getline(infile, str))
	{
		outfile << "Case #" << n << ": " << ANS(infile, str) << endl;
		++n;
	}
	infile.close();

	//test();
	
	//cin >> n;
	return 0;
}