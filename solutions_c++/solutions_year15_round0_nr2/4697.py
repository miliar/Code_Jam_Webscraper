#include<stdio.h>
#include<algorithm>
#define MAX 100000
using namespace std;
int mainfunction(int ar[],int n,int k)
{
	int counter=0;
	while (ar[n-1]>k)
	{
		int move=n-1;
		while (move>=0&&ar[move]>k)
		{
			int div=ar[move]-k,save=ar[move];
			counter++;
			ar[move]=div;
			ar[n]=save-div;
			n++;
			move--;
		}
		sort(ar,ar+n);
	}
	return counter;
}
int main()
{
	int t;
	scanf(" %d",&t);
	for (int i = 0; i < t; i++)
	{
		int n,c,ar[1000],br[1000],m,min;
		scanf(" %d",&n);
		for (int j = 0; j < n; j++)
		{
			scanf(" %d",&ar[j]);
		}
		sort(ar,ar+n);
		m=ar[n-1];
		min=MAX;
		for (int k = 1; k <=m; k++)
		{
			for (int l = 0; l < n; l++)
			{
				br[l]=ar[l];
			}
			int cal=mainfunction(br,n,k);
			if((cal+k)<min)
				min=cal+k;
		}
		printf("Case #%d: %d\n",i+1,min);
	}
	return 0;
}