#include<iostream>
#include<fstream>
#include<vector>
using namespace std;
const int MAXN = 60;
const int MAXCOUNT = 2510;
int count[MAXCOUNT];

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
		int N;
		fin>>N;
		for (int j = 1;j<=MAXCOUNT;j++)
			count[j] = 0;
		for (int j = 0;j<2*N-1;j++)
			for (int k = 0;k<N;k++)
			{
				int temp;
				fin>>temp;
				count[temp]++;
			}
		int now = 0;
		fout<<"Case #"<<i<<": ";
		for (int j = 1;j<=MAXCOUNT;j++)
		{
			if (count[j]%2==1)
			{
				now++;
				if (now==N)
				{
					fout<<j<<endl;
					break;
				}
				else fout<<j<<" ";
			}
		}
	}
	fin.close();
	fout.close();
	return 0;
}