#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>
using namespace std;
int main()
{
	int t,i,j;
	ifstream fin("1.txt");
	ofstream fout("2.txt");
	fin >> t;
	int s;
	string tmp;
	int ans,now,tt;
	for (i=0;i<t;i++)
	{
		ans=0;now=0;
		fin >> s;
		fin >> tmp;
		for (j=0;j<=s;j++)
		{
			tt=tmp[j]-'0';
			if (now<j)
			{
				ans+=j-now;
				now=j;
			}
			now+=tt;
		}
		fout << "Case #"<<i+1<<": "<<ans << endl;
	}
	return 0;
}