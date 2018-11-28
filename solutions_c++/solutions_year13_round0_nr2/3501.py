#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int ma[1000][1000];

int main()
{
	string ipath="B-large.in",opath="1.out";
	ifstream infile(ipath,ios::in);
	ofstream outfile(opath,ios::out);
	int t,n,m;
	bool tf;
	infile>>t;
	for (int loop=1;loop<=t;loop++)
	{
		infile>>n>>m;
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++)
				infile>>ma[i][j];
		tf=true;
		for (int i=0;i<n-1;i++)
			for (int j=i+1;j<n;j++)
				for (int k=0;k<m-1;k++)
					for (int l=k+1;l<m;l++)
					{
						if ((ma[i][k]<ma[i][l])&&(ma[i][k]<ma[j][k])) tf=false;
						if ((ma[i][l]<ma[i][k])&&(ma[i][l]<ma[j][l])) tf=false;
						if ((ma[j][k]<ma[j][l])&&(ma[j][k]<ma[i][k])) tf=false;
						if ((ma[j][l]<ma[j][k])&&(ma[j][l]<ma[i][l])) tf=false;
					}
		outfile<<"Case #"<<loop<<": ";
		if (tf)
			outfile<<"YES\n";
		else 
			outfile<<"NO\n";
	}
}