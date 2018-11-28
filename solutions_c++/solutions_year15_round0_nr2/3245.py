#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<string>
#include<vector>

#define f first
#define s second
#define pb push_back

using namespace std;

typedef pair<int,int> pr;
typedef long long ll;

int A[1003][1003];
int arr[1003];

void precomp()
{
	int i,j;

	for(i = 1;i <= 1000;i++)
	{
		for(j = i+1;j <= 1000;j++)
		{
			A[j][i] = A[j-i][i]  + 1; 
		}
	}
}

int main()
{
	int t,i,j,idx,mx,d,res,ans;
	
	precomp();
	/*for(i = 1;i <= 9;i++)
	{
		for(j = 1;j <= 9;j++)
		{
			printf("%d ",A[i][j]);	
		}
		printf("\n");
	}*/


	scanf("%d",&t);
	idx = 1;
	mx = 1000000;
	while(t--)
	{
		scanf("%d",&d);
		for(i = 1;i <= d;i++)
		{
			scanf("%d",&arr[i]);
			mx = max(arr[i],mx);
		}
		ans = mx;
		for(i = 1;i <= mx;i++)
		{
			res = 0;
			for(j = 1;j <= d;j++)
			{
				if(arr[j] > i)
				{
					res += A[arr[j]][i];
				}				

			}
			ans = min(ans,res+i);
		}
		printf("Case #%d: %d\n",idx,ans);
		idx++;
		
	}	
	return 0;
}
	

