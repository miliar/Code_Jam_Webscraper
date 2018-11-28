#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	ifstream in;
	ofstream out;
  	in.open ("B-small-attempt1(1).in");
  	out.open("out.in");
 	int s,m,n,i,j,k,f,g,c;
 	in>>s;
	for(i=1;i<=s;i++)	
	{   f=0;
		in>>m>>n;
		int x[m][n];
		int y[m][n];
		for(j=0;j<m;j++)
		{
			for(k=0;k<n;k++)
			{
				in>>x[j][k];
				y[j][k]=2;	
			}	
		}	
		
		for(j=0;j<m;j++)
		{
			c=0;
			if(x[j][0]==1)
				for(k=0;k<n;k++)
				{
					if(x[j][k]==1)
					{
						c++;	
					}
				}
			if(c==n)
			{
				for(k=0;k<n;k++)
				{
					y[j][k]=1;	
				}		
			}	
		}
		
		
		
		for(k=0;k<n;k++)
		{
			c=0;
			if(x[0][k]==1)
				for(j=0;j<m;j++)
				{
					if(x[j][k]==1)
					{
						c++;	
					}
				}
			if(c==m)
			{
				for(j=0;j<m;j++)
				{
					y[j][k]=1;	
				}		
			}	
		}
		
		
		for(j=0;j<m;j++)
		{
			for(k=0;k<n;k++)
			{
				if(x[j][k]==y[j][k])
				{
					f++;	
				}	
			}	
		}
		
		
		
		
		
		
		
		if(f==m*n)
			out<<"Case #"<<i<<": YES"<<endl;
		else
			out<<"Case #"<<i<<": NO"<<endl;
	}
	
	
		
	return 0;
}
