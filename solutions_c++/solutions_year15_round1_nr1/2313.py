#include <iostream>
#include <string.h>
#include <stdio.h>
#include <fstream>
using namespace std;
#define lld long long
int a[1005];
fstream fin,fout;

int main()
{

	int t,n,m,i,j;
	fin.open("input.in");
	fout.open("output1.txt");
	//cin>>t;
	//while(t--)
	fin>>t;

	for(j=1;j<=t;j++)
	{
		//cin>>n;
		fin>>n;
		for(i=0;i<n;i++)
		{
			//cin>>a[i];
			fin>>a[i];
		}
		lld sum1=0;
		lld max=0;
		for(i=0;i<n-1;i++)
		{
			if(a[i+1]<a[i])
			{
				sum1+=a[i]-a[i+1];
			}
			if(a[i+1]<a[i])
			{
				if((a[i]-a[i+1])>max)
					max=a[i]-a[i+1];
			}

		}
		lld sum2=0;
		for(i=0;i<n-1;i++)
		{
			
			if(a[i]<=max)
				sum2+=a[i];
			else if(a[i]>max)
				sum2+=max;
		}
		fout<<"Case #"<<j<<": "<<sum1<<" "<<sum2<<"\n";
		//cout<<sum1<<" "<<sum2<<endl;
	}
}
