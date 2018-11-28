#include<fstream>
#include<iostream>
using namespace std;
bool check(int a[100][100],int m,int n)
{
	int i,j,k,c,flag1=0,flag2=0;
	for(i=0;i<m;i++)
	for(j=0;j<n;j++)
	{
		c=a[i][j];
		flag1=0;
		for(k=0;k<n&&flag1==0;k++)
		if(a[i][k]>c)flag1=1;
		flag2=0;
		for(k=0;k<m&&flag2==0;k++)
		if(a[k][j]>c)flag2=1;
		if(flag1==1&&flag2==1)
		return false;
	}
	return true;
}
int main()
{
	int t;
	ifstream f("1.in");
	ofstream g("1.out");
	int m,n,k,i,j;
	f>>t;
	int a[100][100];
	for(k=1;k<=t;k++)
	{
		f>>m>>n;
		for(i=0;i<m;i++)
		for(j=0;j<n;j++)
		f>>a[i][j];
		g<<"Case #"<<k<<": ";
		if(check(a,m,n))
		g<<"YES\n";
		else
		g<<"NO\n";
	}
	return 0;
}
