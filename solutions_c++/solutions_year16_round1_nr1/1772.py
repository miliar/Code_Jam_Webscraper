#include<iostream>
#include<fstream>
#include<vector>
#include<string>
using namespace std;

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in");
	fout.open("A-large.out");
	int T;
	fin>>T;
	for (int i = 1;i<=T;i++)
	{
		string s;
		fin>>s;
		string ret;
		if (s.length()==0)
		{
			fout<<"Case #"<<i<<": "<<s<<endl;
			continue;
		}
		ret = s[0];
		for (int j = 1;j<s.length();j++)
		{
			char ch1 = s[j];
			char ch2 = ret[0];
			if (ch1>=ch2)
				ret = s[j]+ret;
			else ret = ret+s[j];
		}
		fout<<"Case #"<<i<<": "<<ret<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}