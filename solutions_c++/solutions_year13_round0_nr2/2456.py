#include<iostream>
#include<fstream>
#include<stdlib.h>
#include<cstring>
using namespace std;

ofstream op;


int main()
{
	ifstream ip;
	int i,j,k,l;
	int T,N,M;
	int min;
	int flag;
	int **p,**q;
	int max;

	op.open("output.txt");	
	ip.open("B-large.in");
	ip>>T;
	for(k=0;k<T;k++)
	{
		flag=0;
			ip>>N>>M;
			p=new int *[N];
			q=new int *[N];
			for(i=0;i<N;i++)
			{
				p[i]=new int[M];
				q[i]=new int[M];
			}
			for(i=0;i<N;i++)
			{
				max=0;
				for(j=0;j<M;j++)
				{
					ip>>p[i][j];
					if(p[i][j]>p[i][max])
						max=j;
				}
				for(j=0;j<M;j++)
					q[i][j]=p[i][max];
				
			}
			for(j=0;j<M;j++)
			{
				max=0;
				for(i=0;i<N;i++)
				{
					if(p[i][j]>p[max][j])
						{max=i;}
				}
				cout<<p[max][j]<<"\n";	
				for(i=0;i<N;i++)
				{
					cout<<q[i][j]<<" "<<p[i][j]<<"\n";
					if(q[i][j]!=p[i][j] && p[i][j]<p[max][j])
						{flag=1; break;}
				}
				if(flag==1)
					break;
			}
			op<<"Case #"<<k+1<<": ";
			if(flag==1)
				op<<"NO\n";
			else 
				op<<"YES\n";
			cout<<"\n";
				
		}
	ip.close();
	op.close();
	return 0;
	
}
