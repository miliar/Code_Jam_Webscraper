#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <string>
#include <stdlib.h> 

using namespace std;

int result=0;



int main()
{
int t;
cin>>t;
	for (int ct=0;ct<t;ct++)
	{
	unsigned long long int count=0;
	int n;
	cin>>n;
	int *q=new int [n];
	string  *a=new string[n];
		for (int ct2=0;ct2<n;ct2++)
		{
		cin>>a[ct2];
		q[ct2]=ct2;
		}
		do
		{
			string line="";
			for (int ct2=0;ct2<n;ct2++)
			{
			line+=a[q[ct2]];
			}
			
			bool tab[256]={0};
			bool result=true;
			for (unsigned int i=0;i<line.length();i++)
			{
			
			if (tab[(int)line[i]]==true) result=false;
			tab[(int)line[i]]=true;
			while (line[i+1]==line[i]) i++;
			}
			
		if (result==true) count++;
		}
		while (next_permutation(q,q+n));
		
	cout<<"Case #"<<ct+1<<": "<<count%1000000007<<endl;
	}
}
