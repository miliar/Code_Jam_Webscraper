#include<bits/stdc++.h>
using namespace std;

int arr[1005];

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	
	int T, k=0;
	scanf("%d",&T);
	while(T--)
	{
		k++;
		int D;
		scanf("%d",&D);
		for(int i=0; i<D; i++)
			scanf("%d",&arr[i]);
		
		int ret = 1<<30;
		
		for(int i = 1; i <= 1000; i++)
		{
			int r = 0, r2 = 0;
			for(int j=0; j<D; j++)
			{
				if(arr[j]/i + (bool)(arr[j]%i) - 1 < 0) fprintf(stderr,"%d\n",arr[j]);
				r += max(0, arr[j]/i + (bool)(arr[j]%i) - 1);
				if(arr[j]/i)r2 = i;
				else r2 = max(r2, arr[j]%i);
			}
			ret = min(ret, r + r2);
		}
		printf("Case #%d: %d\n",k,ret);
	}
}







