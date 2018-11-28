#include<iostream>
#include<cstdio>
#include<fstream>
#include<algorithm>
using namespace std;
int main()
{
	int t;
	ifstream fin;
	ofstream fout;
	fin.open("D:\in.txt");
	fout.open("D:\out.txt");
	fin>>t;
	for(int c1=1;c1<=t;c1++){
	int a,b,k,ret=0;
	fin>>a>>b>>k;
	for(int i=0;i<a;i++)
		for(int j=0;j<b;j++)
			if((i&j)<k)
				ret++;
	fout<<"Case #"<<c1<<": "<<ret<<"\n";
	}
	return 0;
}
