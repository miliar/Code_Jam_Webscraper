#include<iostream>
#include<fstream>
#include <stdlib.h>

using namespace std;

int main()
{
	ifstream fin;
	ofstream fout;
	
	fin.open("A-large.in");
	fout.open("output.txt");
	
	int t;
	fin>>t;
	
	for(int j=1; j<=t; j++)
	{
		int max, count =0; char flush;
		fin>>max;
		int cum[max+1], s[max+1]; char str[max+1];
			fin.get(flush);
		for(int i=0; i<=max; i++)
		{
		
			fin.get(str[i]);
				s[i]= ((int)str[i])-48;
			
			cum[i]=0;
		}
		cum[0]=s[0];
		cum[1]=s[0];
		
		if(cum[1]<1)
			{
				count = count + (1-cum[1]);
				cum[2]=1;
			}
			
		for(int i=2; i<=max; i++)
		{
			cum[i]= cum[i]+ cum[i-1] + s[i-1];
			if(i>cum[i])
				{		
					count= count + (i-cum[i]);
					cum[i+1]= (i-cum[i]);
				}
		}
		
		
			
		fout<<"Case #"<<j<<": "<<count<<endl;
	}
	
return 0;	
}
