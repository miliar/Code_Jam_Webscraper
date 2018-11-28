#include<iostream>
#include<cstdio>
#include<cmath>
#include<fstream>
using namespace std;
int main()
{
	int t,k,r1,r2,i,j,a[5][5],b[5][5],ans;
	ifstream fin("a.txt");
	ofstream fout("b.in");
	fin>>t;
	for(k=1;k<=t;k++)
	{
		fin>>r1;
		for(i=1;i<5;i++)
		for(j=1;j<5;j++)
		fin>>a[i][j];
		fin>>r2;
		for(i=1;i<5;i++)
		for(j=1;j<5;j++)
		fin>>b[i][j];
		ans=0;
		for(i=1;i<=4;i++)
		for(j=1;j<=4;j++)
		{
			if(a[r1][i]==b[r2][j])
			{
				if(ans==0) ans=a[r1][i];
				else {goto BADM;}
			}
		}
		if(ans==0)
		{
			fout<<"case #"<<k<<": Volunteer cheated!\n";
		}
		else
		{
			fout<<"case #"<<k<<": "<<ans<<endl;
		}
		continue;
		BADM:
			fout<<"case #"<<k<<": Bad magician!\n";
			
	}
}
