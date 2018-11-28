#include<iostream>
#include<vector>
#include<string>
#include<fstream>
using namespace std;
int main()
{
	int n, m;
	string s;
	ifstream fin("A-large.in");
	ofstream fout("a.out");
	fin >> n;
	int stage = 1;
	while (stage <= n)
	{
		fin >> m;
		fin >> s;
		int curNum=0, allNum = 0;
		curNum = curNum+s[0] - '0';
		for (int i = 1; i <= m; i++)
		{
			if (s[i] == '0')
				continue;
			if (curNum < i)
			{
				allNum = allNum+i - curNum;
				curNum = i;
			}
			curNum = curNum + s[i] - '0';
		}
		fout << "Case #" << stage << ": " << allNum << endl;
		stage++;

	}
}