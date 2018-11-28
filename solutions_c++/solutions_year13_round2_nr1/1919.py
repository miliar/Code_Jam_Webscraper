#include<iostream>
#include<fstream>
#include<stdlib.h>
#include<cstring>
#include<math.h>
#include<inttypes.h>
using namespace std;

ofstream op;

int main()
{
	ifstream ip;
	ofstream op;
	unsigned long i,j,k,l,temp,min;
	unsigned long T,n;
	op.open("output.txt");	
	ip.open("A-large.in");
	ip>>T;
	long A,N,*p,*q;
	long count,val;
	long B;
	for(l=0;l<T;l++)
	{
		ip>>A>>N;
		op<<"Case #"<<l+1<<": ";
		p=new long [N];
		for(i=0;i<N;i++)
			ip>>p[i];
		for(i=0;i<N;i++)
		{
			min=i;
			for(j=i+1;j<N;j++)
			{
				if(p[min]>p[j])
					min=j;
			}
			temp=p[i];
			p[i]=p[min];
			p[min]=temp;	
			
		}
		
		cout<<"\n";
		if(A==1)
		{ op<<N<<"\n"; continue;}
		
		min=N+1;
		
		for(i=0;i<N;i++)
		{
			long moves=i;
			val=A;
			for(j=0;j<N-i;j++)
			{
				if(p[j]<val)
					val+=p[j];
				else
				{
					while(val<=p[j])
					{
						moves++;
						val=2*val-1;
					}
					val=val+p[j];
				}
			}

			if(moves<min)
				{min=moves; cout<<l<<" "<<min<<"\n";}
		}	
		if(min>N)
			min=N;
		op<<min<<"\n";
	}
	ip.close();
	op.close();
	return 0;
	
}
