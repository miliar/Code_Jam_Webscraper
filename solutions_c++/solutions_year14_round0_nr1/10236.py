#include <iostream>
#include <algorithm>
#include <cstring>
#include <bitset>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORe(i,n) for(int i=0;i<n;i++)
#define FOR1(i,n) for(int i=1;i<=n;i++)
#define w(t) while(t--)
#define s(i) scanf("%d",&i)
#define p(i) printf("%d",i)
#define line printf("\n")
using namespace std;

int main() {
	int t;
freopen ("input.txt", "r", stdin);
        freopen ("output.txt", "w", stdout);
	s(t);
	for(int k=0;k<t;k++)
	{
		int first,sec;
	int arr1[5][5]={0};
	int arr2[5][5]={0};
	s(first);
	for(int i=1;i<=4;i++)
	{
		for(int j=1;j<=4;j++)
		{
			s(arr1[i][j]);
		}
	}
	s(sec);
	for(int i=1;i<=4;i++)
	{
		for(int j=1;j<=4;j++)
		{
			s(arr2[i][j]);
		}
	}
	int count=0;int flag;
	for(int i=1;i<=4;i++)
	{	for(int j=1;j<=4;j++){
		if(arr1[first][i]==arr2[sec][j])
		{
			count++;
			if(count==1)
			{
				flag=arr1[first][i];
			}
			if(count>1)
			{
				count=999;
				break;
			}
		}
	}}
	if(count==0)
	{
		printf("Case #%d: Volunteer cheated!\n",k+1);
	}
	else if(count==1)
	{
		printf("Case #%d: %d\n",k+1,flag);
	}
	else
	{
		printf("Case #%d: Bad magician!\n",k+1);
	}
	}
	return 0;
}
