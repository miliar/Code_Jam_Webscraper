#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int d;
int p[1001];
int rez=0;

int main()
{
	int tc;
	fin>>tc;
	for (int tcc=1; tcc<=tc; tcc++)
	{
		fout<<"Case #"<<tcc<<": ";
		fin>>d;
		rez=1000;
		for (int i=0; i<d; i++)
		{
			fin>>p[i];
		}

		for (int i=1; i<=1000; i++)
		{
			int j=0;
			for (int k=0; k<d; k++)
				j+=(p[k]-1)/i;
			rez = min(rez,i+j);
		}

		fout<<rez;
		fout<<'\n';
	}
	return 0;
}
