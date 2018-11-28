#include<iostream>
#include<algorithm>
#include<fstream>
using namespace std;
int i,l,n,nval=0;
string pos;
	ifstream fin("A.in");
	ofstream fout("A.out");
int con(char a)
{
	if(a=='a'||a=='e'||a=='i'||a=='o'||a=='u')return 0;
	return 1;
}
int solve(int a)
{
	nval=0;
	fin>>pos>>n;
	int i,j,k,l,cons=0;
    for(i=0;i<pos.length();i++)
    for(j=i;j<pos.length();j++)
    {
		int k,l,f=0;
		for(k=i;k<=j-n+1;k++)
		{int f1=1;
		for(l=k;l<k+n;l++)
		if(!con(pos[l]))f1=0;
		if(f1==1)f=1;
		}
		if(f)nval++;
	}
	fout<<"Case #"<<a<<": "<<nval<<endl;
}
		
int main()
{

	fin>>l;
	for(i=0;i<l;i++)
	solve(i+1);
	return 0;
}
