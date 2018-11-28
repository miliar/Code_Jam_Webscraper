//standing ovation

#include<string>
#include<iostream>
#include<ctype.h>
#include<stdio.h>
#include<stdlib.h>
#include<fstream>

using namespace std;


int to_int(char a)
{
	return (int)(a-48);
}
int sum_to(int n,char a[2000])
{
	int sum=0;
	for(int i=0;i<=n;i++)
	sum+=to_int(a[i]);

	//cout<<sum<<"h";
	return sum;	
}
int sum_to_(int n,int x[2000])
{
	int sum=0;
	for(int i=0;i<=n;i++)
	sum+=x[i];
	return sum;
}
int main()
{
	int smax;
	int t,t1=1,i;
	int flag;
	int count=0;
	char a[2000];
	int have[2000],get[2000],need[2000];
	fstream f,f1;
	f.open("in");
	f1.open("out1");
	f>>t;
	
	while(t--)
	{
		f>>smax;
		for(i=0;i<=smax;i++)
		{
			f>>a[i];
		}		
				//initialise have,get,need
		
		for(i=0;i<=smax;i++)
		{
			have[i]=to_int(a[i]);
			need[i]=i;
			get[i]=0;
		}
		
		for(i=1;i<=smax;i++)
		{
			if(a[i]!='0')
			if((need[i])>(sum_to(i-1,a)+sum_to_(i-1,get)))
			{
				get[i]=(need[i])-(sum_to(i-1,a)+sum_to_(i-1,get));
			//	cout<<get[i]<<endl;
			}
			
		}
		int sol=0;
		for(i=0;i<=smax;i++)
		sol+=get[i];
		cout<<"Case #"<<t1<<": "<<sol<<endl;
		t1++;
	}
	return 0;
}
