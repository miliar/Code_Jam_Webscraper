#include <iostream>
#include <fstream>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <vector>
#include <set>
using namespace std;


int main()
{
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	
	int t;
	fin>>t;
		string str="Case #";
	int cnt=1;
	while(t--)
	{
		int k,c,s;
		fin>>k>>c>>s;
		fout<<str<<cnt<<": ";
		cnt++;
		for(int i=1;i<=k;i++)
		fout<<i<<" ";
		fout<<endl;
	}
	
	return 0;
}
