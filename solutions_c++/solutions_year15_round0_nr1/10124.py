#include<iostream>
#include<string>
#include<fstream>
#include<vector>
#include<algorithm>

int main(int argc, char* argv[])
{
	std::ifstream fin("A-small-attempt1.in");
	std::ofstream fout("A-small-attempt1.out");
	int T;
	fin >> T;
	for (int CaseNum = 1; CaseNum <= T; CaseNum++)
	{
		fout << "Case #" << CaseNum << ": ";
		int Smax;
		fin >> Smax;
		std::string str;
		fin >> str;
		std::vector<int> v;
		int addterm = 0;
		int fixnum = 0;
		for (int i = 0; i != str.length(); i++)
		{
			char ch;
			ch = str.at(i);
			v.push_back(ch - '0');
			if (i > addterm && v.at(i)!=0)
			{
				fixnum += i - addterm;
				addterm += fixnum;
			}
			addterm += v.at(i);
		}
		fout << fixnum;
		fout << std::endl;
	}
	return 0;
}