#include<iostream>
#include<stdio.h>
#include <fstream>

using namespace std;

int main()
{
	long long int i,j,n,t,ctr[10]={},flag,fg,temp,k,r,tt,p;
	
	int l;
	
	ofstream outfile;
  	outfile.open("E:\\codejam\\gcodeout.txt");
	
	ifstream infile; 
   infile.open("E:\\codejam\\gcodein.txt");
	
	cin>>t;
p=1;
	while(t--)
	{
		
		k=1;
		
		cin >> n; 
		
		
		flag=0;
		fg=0;
		
		for(i=0;i<10;i++)
		ctr[i]=0;
		
		while(flag!=1)
	{
		temp=k*n;
		tt=temp;
		
		while(temp>0)
		{
			r=temp%10;
			if(ctr[r]==0)
			ctr[r]=1;
			temp=temp/10;
		}
		
		for(i=0;i<10;i++)
		{
			if(ctr[i]==1)
			flag=1;
			else
			{
				flag=0;
				break;
			}
		}
		
		if(flag==1)
		 break;
		 
		
		for(i=0;i<10;i++)
		{
			if(k>=10 && ctr[i]==0)
			fg=1;
			else
			{
				fg=0;
				break;
			}
		}
		
		if(fg==1)
		break;
		 
		k++;
	}
	
	if(flag==1 && fg==0)
	outfile <<"Case #"<<p++<<":  " << tt << endl;
	else
	 outfile <<"Case #"<<p++<<":  "<< "INSOMNIA" << endl;

   }
   
   outfile.close();
   
	infile.close();
}

