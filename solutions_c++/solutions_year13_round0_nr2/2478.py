#include<fstream>
#include<iostream>
#include<math.h>

using namespace std;

int main()
{
	int t,tc,a[101][101],b[101][101],chk,x,y,n,m,max;
	ifstream ifile("D:/in.in");
	ofstream ofile("D:/out.txt");
	ifile>>t;
	for(x=0;x<101;++x)
	for(y=0;y<101;++y)
	b[x][y]=0;
	for(tc=0;tc<t;++tc)
	{
		ifile>>n>>m;
		for(x=0;x<n;++x)
		for(y=0;y<m;++y)
		ifile>>a[x][y];
		for(x=0;x<n;++x)
		{
			max=a[x][0];
			for(y=1;y<m;++y)
			if(max<a[x][y]) max=a[x][y];
			for(y=0;y<m;++y)
			if(a[x][y]==max) b[x][y]=1;
		}
		for(x=0;x<m;++x)
		{
			max=a[0][x];
			for(y=1;y<n;++y)
			if(max<a[y][x]) max=a[y][x];
			for(y=0;y<n;++y)
			if(a[y][x]==max) b[y][x]=1;
		}
		chk=1;
		for(x=0;x<n;++x)
		{
			for(y=0;y<m;++y)
			if(b[x][y]==0)
			{
				chk=0;
			}
			else b[x][y]=0;
		}
		if(chk==1) ofile<<"Case #"<<tc+1<<": YES\n";
		else ofile<<"Case #"<<tc+1<<": NO\n";
	}
	return 0;
}
