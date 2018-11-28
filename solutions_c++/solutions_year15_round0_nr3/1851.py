#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

/*
		i   j  k
	i   -1  k  -j
	j	-k	-1	i
	k	j	-i  -1

	i=2 j=3 k=4
*/

map<int, map<int,int> > m;
void init()
{
	m[1][1]=1;
	m[1][2]=2;
	m[1][3]=3;
	m[1][4]=4;
	m[2][1]=2;
	m[3][1]=3;
	m[4][1]=4;
	//
	m[2][2] = -1;
	m[3][3] = -1;
	m[4][4] = -1;
	//
	m[2][3] = 4;
	m[2][4] = -3;
	//
	m[3][2]=-4;
	m[3][4]=2;
	//
	m[4][2]=3;
	m[4][3]=-2;

	for (int i=1; i<=4; i++)
		for (int j=1; j<=4; j++)
			{
				m[-i][j] = -m[i][j];
				m[i][-j] = -m[i][j];
				m[-i][-i] = m[i][i];
			}
}

int a[10005];
int bi[10005];
int ci[10005];

int main()
{
	int tc;
	fin>>tc;
	init();
	string s;
	for (int tcc=1; tcc<=tc; tcc++)
	{
		fout<<"Case #"<<tcc<<": ";

		int l,x;
		fin>>l>>x;
		fin>>s;

		for (int i=0; i<s.length(); i++)
			if (s[i]=='i') a[i]=2;
			else if (s[i]=='j') a[i]=3;
			else a[i]=4;

		for (int i=0; i<l*x; i++)
			a[i] = a[i%l];

		int n=1;
		for (int i=0; i<l*x; i++)
		{
			n = m[n][a[i]];
			if (n==2) bi[i]=1;
			else bi[i]=0;
		}

		n=1;
		for (int i=l*x-1; i>=0; i--)
		{
			n = m[a[i]][n];
			if (n==4) ci[i]=1;
			else ci[i]=0;
		}

		bool flag=false;

		for (int i=0; i<l*x && !flag; i++)
			if (bi[i])
		{
			int n=1;
			for (int j=i+1; j<l*x && !flag; j++)
			{
				n=m[n][a[j]];
				if (n==3 && ci[j+1]) flag=true;
			}
		}

		if (flag) fout<<"YES";
		else fout<<"NO";

		fout<<'\n';
	}
	return 0;
}
