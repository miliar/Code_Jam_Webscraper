#include<fstream>
#include<iostream>
#include<stdio.h>
#include<math.h>

using namespace std;

int square(long long int l)
{
	long long int n;
	n=sqrt(l);
	
	if(n*n==l)
	return 1;
	else
	return 0;
}

int ispalin(long long int l)
{
	long long int k,p=0;
	int i,j,n,r;
	k=l;
	
	for(i=0;k>0;k/=10,i++);
	k=l;
	i--;
	
	for (;k>0;k/=10,i--)
	{
		r=k%10;
		p+=r*pow(10,i);
	}	
	if(p==l)
	return 1;
	else return 0;
}

int main()
{
	long long int l[40],a,b,i,na,nb;
	int j,k,t,cnt,n1,n2;
	
	na=1;
	nb=10000000;
	
	for(i=na,j=0;i<=nb;i++)
		{
			if(ispalin(i))
				if(ispalin(i*i))
					l[j++]=i*i;
		}
	
//	for(i=0;i<39;i++)
//	printf("%lld\n",l[i]);
	
	l[j]=100000000000001;
		
	ifstream ifile("I:/C-large-1.in");
 	ofstream ofile("I:/out.txt");
 	ifile>>t;
	
	for(k=0;k<t;k++)
	{
		ifile>>a>>b;
		
		cnt=0;
		j=0;
		while(j<39){
			
			if(l[j+1]>=a && l[j]<a)
			na=j+1;
			else if(l[j]==a)
			na=j;
			
			
			if(l[j+1]>b && l[j]<=b)
			{
			nb=j+1;	
			}
			else if(l[j+1]==b)
			{
			nb=j+2;
			}
			    
		    j++;
		}
		
	
		cnt=nb-na;
		
		ofile<<"Case #"<<k+1<<": "<<cnt<<"\n";
	}
	
	return 0;
}
