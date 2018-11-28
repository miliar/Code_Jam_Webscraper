#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

typedef long USLONG;
typedef string ipType;
//typedef vector<char> ipType;

#define BlankSide '-'
#define HappySide '+'

bool check(const ipType& ip, USLONG pos)
{
	for(USLONG i = 0; i <= pos; i++)
	{
		if(ip[i] == BlankSide) { return true; }
	}
	return false;
}

ipType Flip(const ipType& ip, USLONG pos, USLONG size)
{
	USLONG i(0);
	ipType NewIp = ip;
	for(; i <= pos; i++)
	{
		NewIp[i] = (ip[pos - i] == HappySide) ? BlankSide : HappySide;

	}
	return NewIp;
}
//#define fin cin
//#define fout cout

//int main(int argc, char **argv)
int main()
{
	USLONG nCases = 0;
	USLONG pos(0), size(0);
	#ifndef fin
	ifstream fin("B-small-attempt0.in");
	ofstream fout("Output.txt");
	#endif
	
	fin >> nCases;
	USLONG i(0), Count(0);
	
	vector<ipType> str(nCases);
	for(; i < nCases; i++)
	{
		Count = 0;
		fin >> str[i];
		size = str[i].size();
		pos = size - 1;
		while(Count < size)
		{
			if(check(str[i], pos))
			{
				pos = str[i].find(BlankSide);
				if(pos > 0)
				{
					str[i] = Flip(str[i], pos - 1, size);
					Count++;
				}
				pos = str[i].rfind(BlankSide);
				str[i] = Flip(str[i], pos, size);
				Count++;
			}
			else
			{
				break;
			}
		}
		fout << "Case #" << i+1 << ": " << Count << "\n";
	}
	return 0;
}
