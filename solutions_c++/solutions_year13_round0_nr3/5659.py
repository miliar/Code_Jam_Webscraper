#include <fstream>
#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<iostream>
#include<string.h>
using namespace std ;
bool palin(string k)
{
	if(k.size()%2==0)
		{
			 for(int j=0;j<=(k.length()/2)-1;j++)
			{
				if(k[j]==k[k.length()-1-j]);
				else
					return false;
			}
		}
		else
			for(int j=0;j<=(k.size()-1)/2;j++)
			{
				if(k[j]==k[k.length()-1-j]);
				else
					return false;					
			}
return true;
}
int main()
{
	FILE *f,*d;
	f=fopen("D:\\output.txt", "w");
	d=fopen("input.txt", "r");
	ifstream in;
	ofstream out;
	in.open("input.txt");
	out.open("D:\\output.txt");
	int t;
	unsigned long long a,b;
	in>>t;
	
	for (int i = 0; i < t; i++)
	{
		int res=0;
		in>>a>>b;
		for (unsigned long long j = a; j <= b; j++)
		{
			if(palin(to_string(j)))
				if(sqrt(j) == (long long)(int)sqrt(j))
					if(palin(to_string((int)sqrt(j))))
					res++;
				
		
		}
	out<<"Case #"<<i+1<<": "<<res<<endl;
	}
	
	fclose(d);
	fclose(f);
	return 0;
}