#include<fstream>
#include<iostream>
using namespace std;
int main()
{
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	int a[4][4],b[4][4],m,n,cnt,check,p,t,x,y,j,k,ans;
	fin>>t;
	for(p=1;p<=t;p++)
	{
		cnt=0;
		fin>>m;
		for(x=0;x<4;x++)
			for(y=0;y<4;y++)
				fin>>a[x][y];
		fin>>n;
		for(x=0;x<4;x++)
			for(y=0;y<4;y++)
				fin>>b[x][y];
		m--;
		n--;
		for(j=0;j<4;j++)
		{
			check=a[m][j];
			for(k=0;k<4;k++)
			{
				if(check==b[n][k])
				{
					cnt++;
					if(cnt==1)
						ans=check;
					break;
				}
			}
		}
		fout<<"Case #"<<p<<": ";
		if(cnt==1)
			fout<<ans<<"\n";
		else if(cnt==0)
			fout<<"Volunteer cheated!\n";
		else
			fout<<"Bad magician!\n";
	}
}