#include<iostream>
#include<fstream>

using namespace std;

int main() 
{

	ifstream in;
	ofstream out;
	in.open("A-small-attempt1.in");
	out.open("out.in");
	int T,i,j,k,a,b,f,m;
	int x[4][4],y[4],z[4],d[4][4];
	in>>T;
	for(i=0;i<T;i++)
	{
		
		f=0;
		in>>a;
		
		for(j=0;j<4;j++)
			for(k=0;k<4;k++)
				in>>x[j][k];
			
		
					
		in>>b;
		
		for(j=0;j<4;j++)
			for(k=0;k<4;k++)
				in>>d[j][k];
		
		for(j=0;j<4;j++)
		{
			y[j]=x[a-1][j];
			z[j]=d[b-1][j];
		}
			
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
				if(z[j]==y[k])
				{
					f++;
					m=j;
				}		
		}
		
		if(f==0)
				out<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
		if(f==1)
				out<<"Case #"<<i+1<<": "<<z[m]<<endl;
		if(f>1)
				out<<"Case #"<<i+1<<": Bad magician!"<<endl;
	}
	
	return 0;
}
