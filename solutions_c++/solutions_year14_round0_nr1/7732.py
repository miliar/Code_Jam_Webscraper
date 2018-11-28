#include<iostream>
#include<fstream>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.out");

void matrix(int a[5][5])
{
	for(int j=1; j<=4; j++)
		for(int k=1; k<=4; k++)
			fin>>a[j][k];
}

int main(void)
{
	int a[5][5];
	int b[5][5];

	int T;
	int ans1=0,ans2=0;
	int nr_sol=0;
	int sol=0;

	fin>>T;

	for(int i=1; i<=T; i++)
	{
		nr_sol=0;
		sol=0;

		fin>>ans1;
		matrix(a);
		fin>>ans2;
		matrix(b);

		for(int j=1; j<=4; j++)
		{
			for(int k=1; k<=4; k++)
			{
				if(a[ans1][j]==b[ans2][k])
				{
					nr_sol++;
					sol=a[ans1][j];
				}
			}
		}

		if(nr_sol==1)
			fout<<"Case #"<<i<<": "<<sol<<endl;
		else if(nr_sol==0)
			fout<<"Case #"<<i<<": "<<"Volunteer cheated!"<<endl;
		else
			fout<<"Case #"<<i<<": "<<"Bad magician!"<<endl;
	}
	return 0;
}