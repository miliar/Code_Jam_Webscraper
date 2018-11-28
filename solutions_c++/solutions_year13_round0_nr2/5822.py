#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
	int t, i, j;
	cin>>t;
	int count=0;
	int A[100][100], n, m;
	for(;t>0;t--)
	{
		count++;
		cin >> n >> m;
		for(i=0; i<n; i++)
		{
			for(j=0; j<m; j++)
				cin>>A[i][j];
		}
	int max=-1, a=1, k;
	for(i=0; i<n; i++)
	{
		max=-1;
		for(j=0; j<m; j++)
		{
			if(A[i][j] >max)
				max=A[i][j];
		}
		for(j=0; j<m; j++)
		{
			if(A[i][j] < max)
			{
				int f=0;
				for(k=0; k<n; k++)
				{
					if(A[k][j]!=A[i][j]) f=1;
				}
				if(f==1)
				{
					a=0;
					break;
				}
			}
			if(a==0) break;
		}
		if(a==0) break;
	}
	if(a==0) cout << "Case #"<<count<<": NO\n";
	if(a==1) cout << "Case #"<<count<<": YES\n";
	}
}
