#include <fstream>
#include <iostream>

using namespace std;


int a[4][4],b[4][4];
int count[17];
int t,tt,row1,row2,i,j,c,ans;

ifstream fin("A-small.in");
ofstream fout("a.txt");


int main()
{
	fin>>t;
	for(tt=1;tt<=t;tt++)
	{
		for(i=1;i<=16;i++)
			count[i]=0;
		fin>>row1;
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			fin>>a[i][j];
		fin>>row2;
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			fin>>b[i][j];
		for(i=0;i<4;i++)
		{
			count[a[row1-1][i]]++;
			count[b[row2-1][i]]++;
		}
		c=0;
		for(i=1;i<=16;i++)
			if (count[i]==2)
			{
				c++;
				ans=i;
			}
		fout<<"Case #"<<tt<<": ";
		if (c==0) fout<<"Volunteer cheated!";
		else if (c==1) fout<<ans;
		else fout<<"Bad magician!";
		fout<<endl;
	}
	return 0;
}