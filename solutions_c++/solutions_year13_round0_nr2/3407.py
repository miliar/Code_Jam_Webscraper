#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int map[105][105];
int a, b;
int test1(int aa, int bb)
{
	for(int i=0; i<b; i++)
	{
		if(i == bb) continue;
		if(map[aa][i] > map[aa][bb]) 
		{
		//	cout<<aa<<" "<<bb<<" ";
			return 1;
		}
		
	}
	return 0;
}

int test2(int aa, int bb)
{
	for(int i=0; i<a; i++)
	{
		if(i == aa) continue;
		if(map[i][bb] > map[aa][bb])
		{
		//	cout<<aa<<" "<<bb<<" ";
			return 1;
		}
			
	}
	return 0;
}

int main()
{
#ifndef ONLINE_JUDGE
//freopen("D:\\in.txt","r",stdin);
//freopen("D:\\out.txt", "w", stdout);
#endif
	int k;
	cin>>k;
	int th = 1;
	while(k--)
	{
		int i, j;
		cin>>a>>b;
		for(i=0; i<a; i++)
		{
			for(j=0; j<b; j++)
			{
				cin>>map[i][j];
			}
		}
		int ju = 0;
		for(i=0; i<a; i++)
		{
			for(j=0; j<b; j++)
			{
				if(test1(i, j) && test2(i, j))
				{
					printf("Case #%d: NO\n", th++);
					ju = 1;
					break;
				}
			}
			if(ju == 1) break;
		}
		if(ju == 0)	printf("Case #%d: YES\n", th++);
	}
	return 0;
}

