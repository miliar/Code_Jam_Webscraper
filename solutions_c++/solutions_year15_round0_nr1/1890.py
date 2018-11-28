#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int main()
{
	int T;
	
	ifstream fin("A-large.in");
	ofstream fout("out.txt");
	fin >> T;
	for (int TT = 0; TT != T; TT++)
	{
		int Smax;
		string s;
		fin >> Smax >> s;
		int Sum = s[0]-48,Addition = 0;
		for (int i = 1; i != Smax + 1; i++)
		{
			if (s[i]!='0'&&Sum < i)
			{
				Addition += i-Sum;
				Sum = i;
			}
			Sum += s[i] - 48;
		}
		fout<<"Case #"<<TT+1<<": " << Addition<<endl;
	}
}