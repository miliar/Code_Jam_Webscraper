#include<iostream>
#include<fstream>
#include<cstring>
#include<cstdlib>
#include<cassert>
using namespace std;
int main()
{	
	FILE *fin = freopen("D-small-attempt0.in", "r", stdin);
	assert( fin != NULL );
	FILE *fout = freopen("D-small-Attempt0.out", "w", stdout);
	int t,k,c,s;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>k;
		cin>>c;
		cin>>s;
		cout<<"Case #"<<i<<": ";
		if(c==1)
		{
			for(int j=1;j<=k;j++)
				cout<<j<<" ";	
		}
		else
		{
			if(k==1||k==2)
				cout<<k;
			else
			{
				int j;
				for(j=1;j<=(k-2);j++)
					cout<<j<<" ";
				cout<<(j*k);			
			}		
		}
		cout<<endl;
	}
	return 0;
}
	
	
	
	
	
	
	
	
	
	
	
	
