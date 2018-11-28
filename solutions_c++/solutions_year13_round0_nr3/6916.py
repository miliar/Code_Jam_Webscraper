#include <iostream>
#include <vector>
#include <list>
#include <cmath>
#include <string>
#include <fstream>
#include <algorithm>
#include <sstream>

using namespace std;

string NumberToString ( int Number )
{
   ostringstream ss;
   ss << Number;
   return ss.str();
}

bool isPalindrom (string str)
{

	int len = str.length();
	int i = 0, j = len-1;
	while(j>=i)
	{
		if(str[i] != str[j])
			return false;
		i++;
		j--;
	}
	return true;
}


int main ()
{
	ifstream fin;
	ofstream fout;

	fin.open("test.in",ios::in);
	fout.open("test.out",ios::out);

	int testCases = 0;
	
	fin>>testCases;
	for(int i=0;i<testCases;i++)
	{
		int a = 0, b = 0, cnt = 0;
		fin>>a>>b;
		for(int j=a;j<=b;j++)
		{
			string str1 = NumberToString(j);
			long long val = (int)sqrt(j*1.0);
			if(val * val != j)
				continue;
			string str2 = NumberToString(val);
			if(isPalindrom(str1) && isPalindrom(str2))
				cnt++;
			
		}
		fout<<"Case #"<<i+1<<": "<<cnt<<endl;
	}
	return 0;
}