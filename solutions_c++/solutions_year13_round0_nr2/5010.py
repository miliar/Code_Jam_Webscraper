#include<iostream>
#include<stdio.h>
using namespace std;
int nrow,mcolumn;
int a[12][12];
int searchCNext(int i,int j,int x)
{		if(j==mcolumn)
			return 0;
		if(a[i][j]==x)
		{
			if(j==mcolumn-1)
				return 1;
			else 
		 		return 1+searchCNext(i,j+1,x);
		}
		return  0;
	
}
int searchCPrev(int i,int j,int x)
{		if(j==-1)
			return 0;
		if(a[i][j]==x)
		{
			if(j==0)
				return 1;
			else 
		 		return 1+ searchCPrev(i,j-1,x);
		}
		return  0;
	
}

int searchRNext(int i,int j,int x)
{		if(i==nrow)
			return 0;
		if(a[i][j]==x)
		{
			if(i==nrow-1)
				return 1;
			else 
		 		return 1+searchRNext(i+1,j,x);
		}
		return  0;
	
}
int searchRPrev(int i,int j,int x)
{		if(i==-1)
			return 0;
		if(a[i][j]==x)
		{
			if(i==0)
				return 1;
			else 
		 		return 1+ searchRPrev(i-1,j,x);
		}
		return  0;
	
}

int call(int i, int j,int x)
{		
		int srn = searchRNext(i+1,j,x);
		int srp = searchRPrev(i-1,j,x);
		if(srn+srp==nrow-1)
			return 1;
		int scn = searchCNext(i,j+1,x);
		int scp = searchCPrev(i,j-1,x);
		if(scn+scp==mcolumn-1)
			return 1;
		return 0;
}
int main()
{	int test;
	scanf("%d",&test);
	int cap = 1;
	while(test--)
	{	scanf("%d %d",&nrow,&mcolumn );
		for(int i =0;i<nrow;i++)
			for(int j=0;j<mcolumn;j++)
				scanf("%d",&a[i][j]);
		bool ans = true;
		int check = 0;
		for(int i =0;i<nrow;i++)
		{
			for(int j = 0 ;j<mcolumn;j++)
			{	if(a[i][j]!=1)
				continue;
					int x = call (i,j,a[i][j]);
					
				if(x==0)
				{	check = 1;
					ans = false;
					break;
				}
			}
			if(check==1)
				break;
		}
		if(ans ==false)
		printf("Case #%d: NO\n",cap );
		else
		printf("Case #%d: YES\n",cap );
		cap++;
		
	}
	
		
}
