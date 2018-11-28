#include <bits/stdc++.h>
#include <fstream>
using namespace std;
int main() {
	ifstream fin("B-large.in");
	ofstream fout("output.txt");
	int t;
	fin>>t;
	for(int w=1;w<=t;w++)
	{
		string a;
		fin>>a;
		int count=0,l=a.length();
		for(int i=1;i<l;i++)
		{
			if(a[i]!=a[i-1])
			count++;
		}
		if(a[l-1]=='-')
		count++;
		fout<<"Case #"<<w<<": "<<count<<endl;
	}
	return 0;
}
