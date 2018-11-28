#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int a[1001];
int s;

int main()
{
	int tc;
	fin>>tc;
	for (int tcc=1; tcc<=tc; tcc++)
	{
		fout<<"Case #"<<tcc<<": ";
		fin>>s;
		int x=0,y=0;
		for (int i=0; i<=s; i++)
			{char c; fin>>c; a[i]=c-'0'; }

		for (int i=0; i<=s; i++)
		{
			if (!a[i]) continue;
			if (x<i) y+=i-x; 
			x = max(x,i);
			x+=a[i];			
		}

		fout<<y;
		fout<<'\n';
	}
	return 0;
}
