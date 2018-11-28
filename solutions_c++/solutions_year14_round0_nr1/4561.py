#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int binarysearch(int a[],int n,int low,int high)
	{ int mid,i,l=1;
	  if (low > high)
	   return 0;
	  mid = (low + high)/2;
	  if(n == a[mid])
	    return(1);
	  if(n < a[mid])
	    { high = mid - 1;
	      binarysearch(a,n,low,high);
	    }
	  if(n > a[mid])
	    { low = mid + 1;
	      binarysearch(a,n,low,high);
	    }
	 }
 
main()
{
	int t,c;
	scanf("%d",&t);
	for(c=0;c<t;c++)
	{
		int n,m;
		scanf("%d",&n);
		int A[4][4],arr[4];
		int i,j;
		for(i=0;i<4;i++)
		{
			for (j = 0; j < 4; ++j)
			{
				scanf("%d",&A[i][j]);
				if(i==n-1)
					arr[j]=A[i][j];
			}
		}
		scanf("%d",&m);
		int B[4][4],brr[4];
		for(i=0;i<4;i++)
		{
			for (j = 0; j < 4; ++j)
			{
				scanf("%d",&B[i][j]);
				if(i==m-1)
					brr[j]=B[i][j];
			}
		}
		sort(arr,arr+4);
		sort(brr,brr+4);
		int ans=0,value=0;
		for (i = 0; i < 4; i++)
		{
			ans += binarysearch(arr,brr[i],0,3);
			if(binarysearch(arr,brr[i],0,3))
				value=brr[i];
		}
		if(ans==1)
			printf("Case #%d: %d\n",c+1,value);
		else if(ans==0)
			printf("Case #%d: Volunteer cheated!\n",c+1);
		else if(ans>1)
			printf("Case #%d: Bad magician!\n",c+1);
	}
}
