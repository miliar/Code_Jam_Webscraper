#include "stdafx.h"
#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

#define filein "d:\A-small-attempt0.in"
#define fileout "d:\A-small-attempt0.out"


bool inclvowel(string c)
{
	char vowels [5]={'a','e','i','o','u'};
	for(int j=0;j<=4;j++)
	{
		for(int k=0;k<c.size();k++)
		{
			if(c[k]==vowels[j])
			{
				return(true);
			}
		}
	}
	return(false);
}

bool subseq(string c,int n)
{
	for(int j=0;j<=c.size()-n;j++)
	{
		if(inclvowel(c.substr(j,n))==false) return(true);
	}
	return(false);
}

int main ()
{
	
	freopen(filein,"r",stdin);
	freopen(fileout,"w",stdout);
	int numcases;
	cin>>numcases;
	for(int i=1;i<=numcases;i++)
	{
		string str;
		int n;
		int outp=0;
		cin>>str>>n;
		for (int x=0;x<=str.size()-n;x++)
		{
			for(int y=n;y<=str.size()-x;y++)
			{
				if(subseq(str.substr(x,y),n)) outp++;
			}
		}
		cout<<"Case #"<<i<<":"<<" "<<outp<<endl;

	}

	fclose(stdin);
	fclose(stdout);
	return 0;

}
