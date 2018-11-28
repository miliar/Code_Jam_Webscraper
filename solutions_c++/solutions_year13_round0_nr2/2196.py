#include<stdio.h>
#include<iostream>
#include<cstring>
#include<algorithm>

using namespace std;

#define FOR(i,n) for(int i=0;i<n;++i)
#define MAX 100

void print(int a[MAX][MAX], int n, int m)
{
	FOR(i,n)
	{
		FOR(j,m)
		{
			cout<<a[i][j];
		}
		
		cout<<endl;
	}
}

void print(int a[MAX], int n)
{
	FOR(i,n)
	{
		cout<<a[i]<<" ";
	}

	cout<<endl;
}

bool solve(int a[MAX][MAX], int n, int m)
{
	int rm[n], cm[m];
	memset(rm, 0, sizeof(rm));
	memset(cm, 0, sizeof(cm));

	FOR(i,n)
	{
		FOR(j,m)
		{
			rm[i] = max(a[i][j], rm[i]);
		}			
	}

	FOR(i,m)
	{
		FOR(j,n)
		{
			cm[i] =  max(a[j][i], cm[i]);
		}
		
	}

	//print(rm,n);
	//print(cm,m);

	FOR(i,n)
	{
		FOR(j,m)
		{
			if(rm[i]>a[i][j] && cm[j]>a[i][j])
			{
				return false;
			}	
		}
	}	

	return true;
}

int main()
{
	int t,n,m, a[MAX][MAX];
	scanf("%d", &t);
	
	FOR(T,t)
	{
		scanf("%d%d", &n, &m);

		FOR(i,n)
		{
			FOR(j,m)
			{
				scanf("%d", &a[i][j]);
			}
		}

		bool result = solve(a, n, m);
		//print(a,n,m);
		printf("Case #%d: ", T+1);
		printf("%s\n", result ? "YES": "NO");	
	}	

	return 0;
}

