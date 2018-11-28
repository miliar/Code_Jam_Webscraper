#include <iostream>
#include<fstream>
#include<math.h>
using namespace std;

/*int *binary(int a)
{
	int num[100];
	for(int i=0;i<100;i++)
	{
		num[i]=5;
	}
	int j=99;
	if(a==0)
	num[j]=0;
	while(a!=0)
	{
		num[j]=a%2;
		a=a/2;
		j--;
	}
	return num;
}*/

int decimal(int *z)
{
	int i=99;
	int y=0;
	
	while(z[i]!=5)
	{
	  y=y+(z[i]*pow(2,99-i));
	  i--;	
	}
	return y;
}

 
int main() 
{
    ifstream fin("abc.txt");
    ofstream fout("ex.txt",ios::app);
	int test;
	fin>>test;
	int a,b,c,d;
	long int count;
	int a1[100],b1[100],c1[100];
	for(int i=0;i<test;i++)
	{
		count = 0;
		fin>>a>>b>>c;
		for(int m=0;m<a;m++)
		{
		  //a1=binary(m);
		  
		  
	for(int g=0;g<100;g++)
	{
		a1[g]=5;
	}
	int x=99;
	int f=m;
	if(f==0)
	a1[x]=0;
	while(f!=0)
	{
		a1[x]=f%2;
		f=f/2;
		x--;
	}
	

		  
		  
		  
		  
		  
		for(int n=0;n<b;n++)
		{
			//b1=binary(n);
			
			for(int h=0;h<100;h++)
	{
		b1[h]=5;
	}
	int x=99;
	int f=n;
	if(f==0)
	b1[x]=0;
	while(f!=0)
	{
		b1[x]=f%2;
		f=f/2;
		x--;
	}
		    int j=99;
		    for(int l=0;l<100;l++)
	        {
		      c1[l]=5;
	        }
		    while((a1[j]!=5)&&(b1[j]!=5))
		   {
			if(a1[j]==1 && b1[j]==1)
			c1[j]=1;
			else
			c1[j]=0;
			j--;
		   }
		 d = decimal(c1);
		 if(d<c)
		 count++;
		 
		     
	    } 
	    
	    }
	    
		
	fout<<"Case #"<<i+1<<": "<<count<<"\n";	
		
		
		
			
			
		
	}
	return 0;
}
