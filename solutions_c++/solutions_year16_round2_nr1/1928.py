#include<iostream>
#include<fstream>
#include<vector>
#include<string>
using namespace std;
const int MAXN = 26;
int a[MAXN];
int count[10];


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
		for (int j = 0;j<10;j++)
			count[j] = 0;
		for (int j = 0;j<MAXN;j++)
			a[j] = 0;
		string s;
		fin>>s;
		for (int j = 0;j<s.length();j++)
			a[s[j]-'A']++;

		count[0] = a['Z'-'A'];
		 a['Z'-'A'] = 0;
		 a['E'-'A']-=count[0];
		 a['R'-'A']-=count[0];
		 a['O'-'A']-=count[0];

		count[2] = a['W'-'A'];
		 a['W'-'A'] = 0;
		 a['T'-'A']-=count[2];
		 a['O'-'A']-=count[2];

		count[4] = a['U'-'A'];
		 a['U'-'A'] = 0;
		 a['F'-'A']-=count[4];
		 a['O'-'A']-=count[4];
		 a['R'-'A']-=count[4];

		count[6] = a['X'-'A'];
		 a['X'-'A'] = 0;
		 a['S'-'A']-=count[6];
		 a['I'-'A']-=count[6];

		count[8] = a['G'-'A'];
		 a['G'-'A'] = 0;
		 a['E'-'A']-=count[8];
		 a['I'-'A']-=count[8];
		 a['H'-'A']-=count[8];
		 a['T'-'A']-=count[8];

		count[1] = a['O'-'A'];
		 a['O'-'A'] = 0;
		 a['N'-'A']-=count[1];
		 a['E'-'A']-=count[1];

		count[3] = a['H'-'A'];
		 a['H'-'A'] = 0;
		 a['T'-'A']-=count[3];
		 a['R'-'A']-=count[3];
		 a['E'-'A']-=count[3]*2;

		count[5] = a['F'-'A'];
		 a['F'-'A'] = 0;
		 a['I'-'A']-=count[5];
		 a['V'-'A']-=count[5];
		 a['E'-'A']-=count[5];

		count[7] = a['V'-'A'];
		 a['V'-'A'] = 0;
		 a['S'-'A']-=count[7];
		 a['N'-'A']-=count[7];
		 a['E'-'A']-=count[7];
		 

		fout<<"Case #"<<i<<": ";
		count[9] = a['I'-'A'];
		for (int j = 0;j<10;j++)
			for (int k = 0;k<count[j];k++)
				fout<<j;
		fout<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}