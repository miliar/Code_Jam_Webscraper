#include<iostream>
#include<cstdio>
#include<cstring>
#include<fstream>
using namespace std;
int m,n,no[101][101];
bool chk_row(int a,int b)
{
	int x=no[a][b];
	for(int i=1;i<=m;i++)
		if(no[a][i]>x)
			return true;
	return false;
}
bool chk_clm(int a,int b)
{
	int x=no[a][b];
	for(int i=1;i<=n;i++)
		if(no[i][b]>x)
			return true;
	return false;
}
int main()
{
	ifstream rf("input.txt");
	ofstream wf("result.txt");
	int t,sw=0;
	rf>>t;
	for(int z=1;z<=t;z++)
	{
		sw=0;
		rf>>n>>m;
		for(int i=1;i<=n;i++)
			for(int j=1;j<=m;j++)
				rf>>no[i][j];
		for(int i=1;i<=n;i++)
		{
			for(int j=1;j<=m;j++)
			{
				if(chk_row(i,j) && chk_clm(i,j))
				{
					sw=1;
					break;
				}
			}
			if(sw==1)
				break;
		}
		if(sw==1)
			wf<<"Case #"<<z<<": NO\n";
		else
			wf<<"Case #"<<z<<": YES\n";
	}
	
	
	return 0;
}
