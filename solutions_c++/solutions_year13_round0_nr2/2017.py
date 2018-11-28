#include<stdio.h>
#include<string.h>
#include<fstream>
#include<iostream>
#include<algorithm>
#include<math.h>

using namespace std;
int max (int a[101][101],int i,int m);
int maxr (int a[101][101],int i,int m);
int main()
{
	int tc,tcc,n,m,a[101][101],c[101],j,k,r[101],var;
	ifstream ifile("d:/lawn.txt");
	ofstream ofile("d:/lawnans.txt");
	ifile>>tc;
	for (tcc=0;tcc<tc;tcc++)
	{
		var=0;
		ifile>>n>>m;
		for (j=0;j<n;j++)
		for (k=0;k<m;k++)
		ifile>>a[j][k];
		for (k=0;k<m;k++)
		{
			c[k]=max(a,k,n);
		}
		for (k=0;k<n;k++)
		{
			r[k]=maxr(a,k,m);
		}
		for (j=0;j<n;j++)
		{
			for (k=0;k<m;k++)
			{
				if (a[j][k]<r[j])
				{
					if (a[j][k]!=c[k])
					{
						ofile<<"Case #"<<tcc+1<<": NO"<<endl;
						var=1;
						break;
					}
				}
			}
			if (var==1)
			break;
		}
		if (var==0)
		ofile<<"Case #"<<tcc+1<<": YES"<<endl;
	}
	return 0;
}


int max (int a[101][101],int i,int m)
{
	int j,mx;
	mx=a[0][i];
	for (j=1;j<m;j++)
	{
		if (a[j][i]>mx)
		mx=a[j][i];
	}
	return mx;
}

int maxr (int a[101][101],int i,int m)
{
	int j,mx;
	mx=a[i][0];
	for (j=1;j<m;j++)
	{
		if (a[i][j]>mx)
		mx=a[i][j];
	}
	return mx;
}
