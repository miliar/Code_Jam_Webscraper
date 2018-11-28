#include <iostream>
#include <vector>
#include <stack>
#include <string>
#include <sstream>
#include <algorithm>
#include <fstream>

using namespace std;

void flipPanCake(string & str, int end)
{
	for(int i = 0; i <= end; i++)
	{
		if(str[i] == '+')
		{
			str[i] = '-';
		}
		else str[i] = '+';
	}
}


int main()
{	
	ifstream fin("test.in",ios::in);
	ofstream fout("result.out",ios::out);

	int t = 0;
	fin>>t;

	for(int i = 0; i < t; i++)
	{
		string str = "";
		fin >> str;

		int len = str.length();
		int cnt = 0;
		for(int j = len-1; j >= 0; j--)
		{
			if(str[j] != '+')
			{
				cnt++;
				flipPanCake(str,j);
			}
		}

		fout << " Case #" << i+1 << ": " << cnt << endl;

	}

	return 0;
}

