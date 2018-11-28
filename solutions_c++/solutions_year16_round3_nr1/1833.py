#include <stdio.h>
#include <fstream>
#include <string.h>
#include <iostream>
using namespace std;

int main()
{
	long t;
	ifstream myfile;
	ofstream myfile1;
	myfile.open ("A-large.in");
	myfile>>t;
	myfile1.open("Output1");
	int i,j;
	long k = t;
	while(t--)
	{
		int n;
		myfile>>n;
		int arra[n],max=0;
		char a,b;
		for(i=0;i<n;i++)
		{
			myfile>>arra[i];
			if(arra[i]>max)
			{
				max = arra[i];
			}
		}
		myfile1<<"Case #"<<(k-t)<<": ";
		int maxc;
		while(max>0)
		{
			maxc=0;
			for(i=0;i<n;i++)
			{
				if(arra[i]==max)
				{
					maxc++;
				}
			}
			int flag=0;
			if(maxc%2==0)
			{
				for(i=0;i<n;i++)
				{
					if(arra[i]==max&&flag==0)
					{
						a=65+i;
						flag=1;
						arra[i]--;
					}	
					if(arra[i]==max&&flag==1)
					{
						b=65+i;
						arra[i]--;
						break;
					}
				}
				myfile1<<a<<b<<" ";
			}
			else
			{
				for(i=0;i<n;i++)
				{
					if(arra[i]==max)
					{
						a=65+i;
						arra[i]--;
						break;
					}	
				}
				myfile1<<a<<" ";
			}
			max = 0;
			for(i=0;i<n;i++)
			{
				if(arra[i]>max)
				{
					max=arra[i];
				}
			}
		}
		myfile1<<endl;
	}
	myfile.close();
	myfile1.close();
}