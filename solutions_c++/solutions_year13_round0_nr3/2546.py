#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <map>
#include <sstream>

using namespace std;

char Add(char& a, char b)
{
	int q = a - '0';
	int w = b - '0';
	int h = q + w;
	a = h + '0';
	if( a > '9' )
	{
		a -= 10;
		return '1';
	}
	return '0';
}

string AddStrings(const string& s1, const string& s2)
{
	int nCurDigit = 0;
	string sLong, sShort;
	if( s1.size() > s2.size() )
	{
		sLong = s1; 
		sShort = s2;
	}
	else
	{
		sLong = s2; 
		sShort = s1;
	}

	char cAdd = '0';
	while( nCurDigit < sShort.size() )
	{
		if( cAdd != '0' )
			cAdd = Add(sLong[sLong.size() - nCurDigit - 1], cAdd);
		
		
		if( cAdd != '0' )
		{
			//this case we can receive only if 9 was last digit
			sLong[sLong.size() - nCurDigit - 1] = sShort[sShort.size() - nCurDigit - 1];
		}
		else
			cAdd = Add(sLong[sLong.size() - nCurDigit - 1], sShort[sShort.size() - nCurDigit - 1]);

		nCurDigit++;
	}

	while( nCurDigit < sLong.size() && cAdd != '0' )
	{
		cAdd = Add(sLong[sLong.size() - nCurDigit - 1], cAdd);
		nCurDigit++;
	}

	if( cAdd != '0' )
		return string('1' + sLong);
	else
		return string(sLong);
}

bool IsPalindrom(const string& s)
{
	for( int i = 0; i < s.size()/2; i++ )
	{
		if( s[i] != s[s.size() - i - 1] )
			return false;
	}
	return true;
}

bool IsLess(const string& s1, const string& s2)
{
	if( s1.size() < s2.size() )
		return true;
	else if( s1.size() > s2.size() )
		return false;
	else
		return s1 < s2;
}

int main()
{
	//ifstream in("C-small-attempt0.in");
    //ofstream out("C-small-attempt0.out");

	ifstream in("C-large-1.in");
    ofstream out("C-large-1.out");
	
	vector<string> vNeeded;
	string sRes = "1";
	string sSquare = "1";
	string sNum = "1";
	string A = "1", B = "100000000000000";
	
	while( !(IsLess(B, sSquare)) )
	{
		if( IsPalindrom(sNum) && IsPalindrom(sSquare) )
			vNeeded.push_back(sSquare);

		sNum = AddStrings(sNum, "1");
		sRes = AddStrings(sRes, "2");
		sSquare = AddStrings(sSquare, sRes);
	}

	int iTasks;
	in >> iTasks;

	for( int iCount = 1; iCount <= iTasks; iCount++ )
	{

		in >> A >> B;

		size_t nNumbers = 0;
		for( size_t i = 0; i < vNeeded.size() && !(IsLess(B, vNeeded[i])); i++ )
		{
			if( !(IsLess(vNeeded[i], A)) )
				nNumbers++;
		}
				
		out << "Case #" << iCount << ": " << nNumbers << endl;
	}
	return 0;
}
