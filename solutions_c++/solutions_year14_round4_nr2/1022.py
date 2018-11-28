#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <string>
#include <algorithm>
#include <math.h>
using namespace std;
const long long int modl=1000000007;
ifstream in("in.txt");
ofstream out("out.txt");
struct srt
{
	int a,i;
};
bool srtbl(srt p,srt q)
{
	return (p.a<q.a);
}
int main()
{
	int t,n,a[1000],d[1001][1001],g;
	srt c[1000];
	in >> t;
	for(int i=1;i<=t;i++)
	{
		in >> n;
		for (int j=0;j<n;j++) in >> a[j];
		for (int j=0;j<n;j++)
		{
			c[j].a=a[j];
			c[j].i=j;
		}
		sort(c,c+n,srtbl);
		for (int j=0;j<n;j++) d[0][j]=c[j].i;
		for (int j=0;j<n;j++)
		{
			for (int k=j+1;k<n;k++) 
			{
				if (c[k].i<c[j].i) d[j+1][k]=d[j][k];
				else d[j+1][k]=d[j][k]-1;
			}
		}
		g=0;
		for (int j=0;j<n;j++) g+=min(d[j][j],n-1-j-d[j][j]);
		out << "Case #" << i << ": " << g << "\n";
	}
	return 0;
}
