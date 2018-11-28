#include<iostream>
#include<fstream>
using namespace std;
ifstream fin("A.in");
ofstream fout("A.out");
int solve(int k)
{
	int i,j,x,y;
	fin>>x>>y;
	fout<<"Case #"<<k+1<<": ";
	if(x>=0)
		for(i=0;i<x;i++)
		fout<<"WE";
	else
	for(i=0;i<0-x;i++)
	fout<<"EW";
	if(y>=0)
	for(i=0;i<y;i++)
	fout<<"SN";
	else
	for(i=0;i<0-y;i++)
	fout<<"NS";
}
int main()
{
	int l,k;
	fin>>l;
	for(k=0;k<l;k++)
	{solve(k);fout<<endl;}
	return 0;
}
		
