#include<iostream>
#include<fstream>
#include<vector>
#include<string>
using namespace std;

const int maxn = 110;
bool a[maxn];


int solveNeg(int pos);
int solvePos(int pos);

int solveNeg(int pos)
{
	if (pos==0)
	{
		if (a[0])
			return 1;
		else return 0;
	}
	if (a[pos])
		return solvePos(pos-1)+1;
	else return solveNeg(pos-1);
}

int solvePos(int pos)
{
	if (pos==0)
	{
		if (a[0])
			return 0;
		else return 1;
	}
	if (a[pos])
		return solvePos(pos-1);
	else return solveNeg(pos-1)+1;
}

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("B-large.in");
	fout.open("B-large.out");
	int T;
	fin>>T;
	for (int i = 1;i<=T;i++)
	{
		string s;
		fin>>s;
		int length = s.length();
		for (int j = 0;j<length;j++)
		{
			if (s[j]=='+')
				a[j] = true;
			else a[j] = false;
		}
		int now = 0;
		int pos = length-1;
		int ret = 0;
		while (pos>=0 && a[pos])
			pos--;
		if (pos>=0)
			ret = solveNeg(pos)+1;
		else ret = 0;
		fout<<"Case #"<<i<<": "<<ret<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}