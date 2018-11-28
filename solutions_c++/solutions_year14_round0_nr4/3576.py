#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;
void sort (double *a,int n);
void room (double *a,int n);
int min (double *a,int n);
int tact (double *a,double *b,int n);
int main()
{
	
	ifstream in;
	in.open("D-large.in");
	
	ofstream fout;
	fout.open("output.op");
	
	int n,n2;
	int c,c1;
	
	in>>n;

	
	for(int i=0;i<n;i++)
	{
		c=0;
		int del=0;
		in>>n2;
		
		c1=n2;
		double a[n2];
		double b[n2];
		
		double a1[n2];	
		double b1[n2];
		
		for(int j=0;j<n2;j++)
		{
			in>>a[j];
			a1[j]=a[j];
			
		}
		
		for(int j=0;j<n2;j++)
		{
			in>>b[j];
			b1[j]=b[j];
		}
		
		sort(a,n2);
		sort(b,n2);
		sort(a1,n2);
		sort(b1,n2);
		int top=n2-1;
		
	/*	for(int j=0;j<n2;j++)
		{
			if(a[j]<b[j])
			{
				room(b,n2);
						
				
			}
			else if(a[j]>b[j])
		
		}*/
		
		c=tact(a,b,n2);
		
		double l;
		for(int j=0;j<n2;j++)///////////
		{
			l=a1[j];
			int f=0;
			
			for(int k=0;k<n2;k++)
			{
				if(b1[k]>l)
				{
				f=1;
				c1--;
				b1[k]=-1;
				del++;
				break;
				}
				
				
			}
			if(f==0)
			{
				//cout<<"trawwa"<<endl;
				int p=min(b1,n2);
				b1[p]=-1;
					
			}
			
			
		}
		
		
		fout<<"Case #"<<i+1<<": "<<c<<" "<<c1<<endl;
		
	}
	
	
	
	
	return 0;
}
void sort (double *a,int n)
{
	double t;
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
				if(a[i]>a[j])
				{
				t=a[i];
				a[i]=a[j];
				a[j]=t;	
					
				}
			
			}
		}
	
	
}

void room (double *a,int n)
{
	double t=a[n-1]	;
	
	for(int i=n-1;i>=1;i--)
	{
		a[i]=a[i-1];
		
	}
	a[0]=t;
	
}
int min (double *a,int n)
{
	double t=1	;
	int pos=0;
	
	for(int i=0;i<n;i++)
	{
		if(a[i]<t && a[i]!=-1)
		{
			t=a[i];
			pos=i;
			
		}
		
	}
	return  pos;
	
}

int tact (double *a,double *b,int n)
{
	int s=0;
	
	
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			if(a[i]>b[j])
			{
				s++;
				b[j]=2;
				break;
			}
		
		}
		
	}
	return  s;
	
}

