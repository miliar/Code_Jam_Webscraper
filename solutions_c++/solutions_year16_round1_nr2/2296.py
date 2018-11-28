#include<iostream>
#include<fstream>
#include<cstring>
#include<cstdlib>
#include<cassert>
using namespace std;
int main()
{
	FILE *fin = freopen("B-large (1).in", "r", stdin);
	assert( fin != NULL );
	FILE *fout = freopen("B-large (1).out", "w", stdout);
    int t,n,a[51],b[2501]={0},max,max1,i,k,m;
	cin>>t;
	for(m=1;m<=t;m++)
	{
		cin>>n;
		max=2*n;
		max1=0;
		for(i=0;i<(max-1);i++)
		{
			for(k=0;k<n;k++)
			{		
				cin>>a[k];
		        b[a[k]]++;		
			}
			if(max1<a[n-1])
			max1=a[n-1];
		}
		
		cout<<"Case #"<<m<<": ";
		for(i=1;i<=max1;i++)
		{
	 	   if(b[i]%2==1)
	 	   {
	 	   	    cout<<i<<" ";
	 	   }
	 	   b[i]=0;
	    }
	    cout<<"\n";
	}	
}
