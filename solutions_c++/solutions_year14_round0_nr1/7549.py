#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
using namespace std;
 
#define REP(i,N)	for(int i = 0; i < N; i++)
 
// Mehtod to do a binary search
int BS(int * ptr,int n,int size)
{
	int lo = 0,hi = size-1,mid;
	while(lo <= hi)
	{
		mid = lo + (hi - lo)/2;
		if(ptr[mid] == n)		return mid;
		else if(ptr[mid] > n)	hi = mid - 1;
		else					lo = mid + 1;
	}
	return -1;
}
 
void solve(int Case)
{
	int q1, q2 , e;
	int * ptr1, * ptr2;
	ptr1 = (int *)malloc(4*sizeof(int));
	ptr2 = (int *)malloc(4*sizeof(int));
 
	scanf("%d",&q1);
	for(int i = 0; i < (q1-1)*4; i++)
		scanf("%d",&e);
	for(int i = 0; i < 4; i++)
		scanf("%d",&ptr1[i]);
	for(int i = 0; i < (4-q1)*4; i++)
		scanf("%d",&e);
 
	scanf("%d",&q2);
	for(int i = 0; i < (q2-1)*4; i++)
		scanf("%d",&e);
	for(int i = 0; i < 4; i++)
		scanf("%d",&ptr2[i]);
	for(int i = 0; i < (4-q2)*4; i++)
		scanf("%d",&e);
 
	sort(ptr1, ptr1 + 4);
	sort(ptr2, ptr2 + 4);
 
 
	int b1,b2,b3,b4;
 
	b1 = BS(ptr2,ptr1[0],4);
	b2 = BS(ptr2,ptr1[1],4);
	b3 = BS(ptr2,ptr1[2],4);
	b4 = BS(ptr2,ptr1[3],4);
 
	if(b1 == b2 && b2 == b3 && b3 == b4 && b4 == -1)
	{
		printf("Case #%d: Volunteer cheated!\n",Case+1);
		return;
	}
	else
	{
		if(b1 != -1 && b2 == b3 && b3 == b4 && b4 == -1)
		{
			printf("Case #%d: %d\n",Case+1,ptr1[0]);
			return;
		}
		else if(b2 != -1 && b1 == b3 && b3 == b4 && b4 == -1)
		{
			printf("Case #%d: %d\n",Case+1,ptr1[1]);
			return;
		}
		else if(b3 != -1 && b1 == b2 && b2 == b4 && b4 == -1)
		{
			printf("Case #%d: %d\n",Case+1,ptr1[2]);
			return;
		}
		else if(b4 != -1 && b1 == b3 && b3 == b2 && b3 == -1)
		{
			printf("Case #%d: %d\n",Case+1,ptr1[3]);
			return;
		}
		else
		{
			printf("Case #%d: Bad magician!\n",Case+1);
			return;
		}
	}
 
 
	free(ptr1), free(ptr2);
}
 
int main()
{
	int t;
	scanf("%d",&t);
	for(int i = 0; i < t; i++)
	{
		solve(i);
	}
	return 0;
}