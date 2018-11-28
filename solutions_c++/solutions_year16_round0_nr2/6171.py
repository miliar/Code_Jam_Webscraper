#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <cstring>
using namespace std;
int main()
{
	FILE *fin = freopen("B-large.in", "r", stdin);
	assert( fin != NULL );
	 FILE *fout = freopen("B-large.out", "w", stdout);
    int t,i,k;
    char a[101];
	cin>>t;
	int count[t];
	for(i=0;i<t;i++)
	{
		cin>>a;
		count[i]=0;
		for(k= 0;k<strlen(a)-1; k++)
		{
			
			if(a[k] != a[k+1])
			{
				count[i]++;
			}
		}

		if(a[k]=='-')
		{
			count[i]++;
		}
		
	}	
	for(i=0;i<t;i++)
	{
	    cout<<"Case #"<<i+1<<": ";
		cout<<count[i]<<endl;
	}
	return 0;
}
