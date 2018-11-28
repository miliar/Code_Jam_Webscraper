#include"iostream"
#include"cstdio"
#include"algorithm"
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
	for(c=1;c<=t;c++)
	{
		int n,m;
		scanf("%d",&n);
		int A[4][4],Acp[4];
		int i,j;
		for(i=0;i<4;i++)
		{
			for (j = 0; j < 4; ++j)
			{
				scanf("%d",&A[i][j]);
				if(i==n-1)
					Acp[j]=A[i][j];
			}
		}
		scanf("%d",&m);
		int B[4][4],Bcp[4];
		for(i=0;i<4;i++)
		{
			for (j = 0; j < 4; ++j)
			{
				scanf("%d",&B[i][j]);
				if(i==m-1)
					Bcp[j]=B[i][j];
			}
		}
		sort(Acp,Acp+4);
		sort(Bcp,Bcp+4);
		int ans=0,value=0;
		for (i = 0; i < 4; i++)
		{
			ans += binarysearch(Acp,Bcp[i],0,3);
			if(binarysearch(Acp,Bcp[i],0,3))
				value=Bcp[i];
		}
		if(ans==1)
			printf("case #%d: %d\n",c,value);
		else if(ans==0)
			printf("case #%d: Volunteer cheated!\n",c);
		else if(ans>1)
			printf("case #%d: Bad magician!\n",c);
	}
}