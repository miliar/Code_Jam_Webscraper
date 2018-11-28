#include<iostream>
#include<fstream>
#include<cstring>
#include<cstdlib>
#include<cassert>
using namespace std;
int main()
{	
	FILE *fin = freopen("A-large.in", "r", stdin);
	assert( fin != NULL );
	FILE *fout = freopen("A-large.out", "w", stdout);
	static int check[10];
	static int counter;
	int t;
	int y=0,x;
	int store;
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
			check[k]=0;
		counter=0;		
		for(int j=1;;j++)
		{
			store=in[i]*j;		
			while(store>0)
			{
				int x=store%10;
				store/=10;	
				if(check[x]==0)
				{
					check[x]=1;
					if(x==0)
						counter+=100;
					else
						counter+=x;
					if(counter==145)
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
		
