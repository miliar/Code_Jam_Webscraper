#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <string>
#include <stdlib.h> 
using namespace std;

int main()
{
int t;
cin>>t;
	for (int ct=0;ct<t;ct++)
	{
	string line;
	cin>>line;
	string a,b;
	a=line.substr(0,line.find("/"));
	b=line.substr(line.find("/")+1);
	int aa=atoi(a.c_str());
	int bb=atoi(b.c_str());
	int n=1;
	int f=0;
	int x=1;
		while (aa>0)
		{
			if (aa%2==1 && f==0)
			{
			f=n;
			}
			n++;
			aa/=2;
			x*=2;
		}
		while(x<bb)
		{
		x*=2;
		f++;
		}
	if (x!=bb) {cout<<"Case #"<<ct+1<<": impossible"<<endl;}
	else cout<<"Case #"<<ct+1<<": "<<f<<endl;
	}
}
