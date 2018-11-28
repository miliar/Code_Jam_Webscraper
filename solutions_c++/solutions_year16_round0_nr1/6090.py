#include<iostream>
#include<fstream>
#include<cstring>
#include<cstdlib>
#include<cassert>
using namespace std;
int main()
{	
	FILE *fin = freopen("A-small-attempt0.in", "r", stdin);
	assert( fin != NULL );
	FILE *fout = freopen("A-small-attempt0.out", "w", stdout);
	static int hash[10];
	static int counter;
	int t;
	int y=0,x;
	int n;
	cin>>t;
	int in[200];
	for(int i=0;i<t;i++)
		cin>>in[i];
	for(int i=0;i<t;i++)
	{
		y=0;
		if(in[i]==0)
		{
			cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;	
			continue;
		}
		for(int k=0;k<10;k++)
			hash[k]=0;
		    counter=0;		
		for(int j=1;;j++)
		{
			n=in[i]*j;		
			while(n>0)
			{
				int x=n%10;
				n/=10;	
				if(hash[x]==0)
				{
					hash[x]=1;
					counter++;
					if(counter==10)
					{
						cout<<"Case #"<<i+1<<": "<<in[i]*j<<endl;
						y=1;
						break;
					}
				}		
			}
			if(y==1)
				break;		
		}	
		if(y!=1)
			cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;	
	}	
	return 0;
}
		
