#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <cstring>
using namespace std;

main()
{
	FILE *fin = freopen("B-large.in", "r", stdin);
	assert( fin != NULL );
	FILE *fout = freopen("B-large.out", "w", stdout);
	
	int T=0,i,j;
	cin>>T;
	char a[T][101];
	int count[T];
	
	for(i = 0; i < T; i++)
	{
		cin>>a[i];
	}
	
	for(i = 0; i < T; i++)
	{
		count[i] = 0;
		for(j = 0; j < strlen(a[i])-1; j++)
		{
			
			if(a[i][j] != a[i][j+1])
			{
				count[i]++;
			}
		}

		if(a[i][j] == '-')
		{
			count[i]++;
		}
		
	}
	
	for(i = 0; i < T; i++)
	{
		cout << "Case #" << i+1 << ": ";
		cout << count[i] << endl;
	}
	
	exit(0);
}
