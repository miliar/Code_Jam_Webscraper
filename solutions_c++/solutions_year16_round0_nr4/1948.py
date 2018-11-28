#include <bits/stdc++.h>
#include <iostream>
#include <fstream>
#define lli long long int
#define vi vector <lli>
using namespace std;
fstream coutf;

int main()
{
	//fstream coutf;
	fstream cinf;
	cinf.open("D-small-attempt0.in");
	coutf.open("Bsmall.txt");
	int t; cinf>>t;

	for(int tt=1;tt<=t;tt++)
	{
	int k,c,s;
	cinf>>k>>c>>s;
	coutf<<"Case #"<<tt<<": ";
	if(k>s) coutf<<"IMPOSSIBLE";
	else
	{
		for(int i=1;i<=k;i++) coutf<<i<<" ";
	}
	coutf<<endl;
	}
	coutf.close();
	cinf.close();
}
