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
	FILE *fout = freopen("D-small-attempt0.out", "w", stdout);
	long long int i,j,t,k,c,s;
	cin>>t;
	for(i=0;i<t;i++)
	{
		cin>>k;
		cin>>c;
		cin>>s;
		cout<<"Case #"<<i+1<<": ";
		if(c==1)
		{
			if(s<k)
				cout<<"IMPOSSIBLE";
			else	
			{
				for(j=1;j<=k;j++)
					cout<<j<<" ";	
			}
		}
		else
		{
			if(k==1||k==2)
				cout<<k;
			else
			{
					for(j=2;j<=(k);j++)
					cout<<j<<" ";
			}		
		}
		cout<<endl;
	}
	return 0;
}
	
	
	
	
	
	
	
	
	
	
	
	
