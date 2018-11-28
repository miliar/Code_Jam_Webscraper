#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	ifstream fin("A-small-attempt0.in");
	ofstream fout("A-small-attempt0.out");
	int t,k,x,y,i,j,a[4][4],b[4][4],s,ans;
	fin>>t;
	for (k=1;k<=t;k++)
	{
		fin>>x;
		for (i=0;i<4;i++)
			for (j=0;j<4;j++) fin>>a[i][j];
		fin>>y;
		for (i=0;i<4;i++)
			for (j=0;j<4;j++) fin>>b[i][j];
		s=0;
		for (i=0;i<4;i++)
			for (j=0;j<4;j++)
				if (a[x-1][i]==b[y-1][j])
				{
					s++;
					ans=a[x-1][i];
				}
		fout<<"Case #"<<k<<": ";
		if (!s) fout<<"Volunteer cheated!"<<endl;
		else if (s>1) fout<<"Bad magician!"<<endl;
		else fout<<ans<<endl;
	}
	return 0;
}