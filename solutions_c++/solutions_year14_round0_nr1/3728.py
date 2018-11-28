#include<iostream>
#include<fstream>
using namespace std;
int n_repat(int *a,int *b,int & x);
int main()
{
	ifstream in;
	in.open("A-small-attempt0.in");
	
	ofstream out;
	out.open("A-small-attempt0.op");
	int n;// # case
	int an;// ansser
	int a[4][4];
	in>>n;
	int b[4];
	int b1[4];
	
	for(int i=0;i<n;i++)
	{
		in>>an;
		
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				in>>a[i][j];
				
			
			}
			
		}
		for(int i=0;i<4;i++)
			{
				b[i]=a[an-1][i];
		
			}
			
			
			/////////////////////////////////////11 
			in>>an;
			
			for(int i=0;i<4;i++)
			{
			for(int j=0;j<4;j++)
			{
				in>>a[i][j];
				
			}
			
			
			
		}
		for(int i=0;i<4;i++)
			{
				b1[i]=a[an-1][i];
			
			}
			
			
			int card;
			
			if( n_repat(b,b1,card)==1)
			{
				out<<"Case #"<<i+1<<": "<<card<<endl;	
			}
			if(n_repat(b,b1,card)>1)
			{
				out<<"Case #"<<i+1<<": Bad magician!"<<endl;	
			}
			if(n_repat(b,b1,card)==0)
			{
				out<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;	
			}
			
		
		
		
	}
	
	
	return 0;
}
int n_repat(int *a,int *b,int & x)
{
	int s=0;

	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
		if(a[i]==b[j] )//&& a[i]!=0 && b[j]!=0)
			{
			s++;
			x=a[i];
			break;
			
			}
		
		}
		
		
	}
	
	return s;
}