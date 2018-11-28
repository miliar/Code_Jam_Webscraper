#include<iostream>
#include<cstdio>

using namespace std;

int n,m;
int a[12][12];

int searchRowNext1(int i,int j,int x)
{		
		if(i==n)
			return 0;
		if(a[i][j]==x)
		{
			if(i==n-1)
				return 1;
			else 
		 		return 1+searchRowNext1(i+1,j,x);
		}
		return  0;
}

int searchRowPrev1(int i,int j,int x)
{		
		if(i==-1)
			return 0;
		if(a[i][j]==x)
		{
			if(i==0)
				return 1;
			else 
		 		return 1+ searchRowPrev1(i-1,j,x);
		}
		return  0;
}

int searchColumnNext1(int i,int j,int x)
{		
		if(j==m)
			return 0;
		if(a[i][j]==x)
		{
			if(j==m-1)
				return 1;
			else 
		 		return 1+searchColumnNext1(i,j+1,x);
		}
		return  0;
}

int searchColumnPrev1(int i,int j,int x)
{		
		if(j==-1)
			return 0;
		if(a[i][j]==x)
		{
			if(j==0)
				return 1;
			else 
		 		return 1+ searchColumnPrev1(i,j-1,x);
		}
		return  0;
}

int call1(int i, int j,int x)
{		
		int srn = searchRowNext1(i+1,j,x);
		int srp = searchRowPrev1(i-1,j,x);
		if(srn+srp==n-1)
			return 1;
		int scn = searchColumnNext1(i,j+1,x);
		int scp = searchColumnPrev1(i,j-1,x);
		if(scn+scp==m-1)
			return 1;
		return 0;
}

int main()
{	
	int tc,i,j;
	scanf("%d",&tc);
	int count = 1;
	while(tc--)
	{	
		scanf("%d %d",&n,&m);
		for(int i =0;i<n;i++)
			for(int j=0;j<m;j++)
				scanf("%d",&a[i][j]);
		bool ans = true;
		int check = 0;
		for(i =0;i<n;i++)
		{
			for(j = 0 ;j<m;j++)
			{	if(a[i][j]!=1)
				continue;
				int x = call1(i,j,a[i][j]);
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
		printf("Case #%d: NO\n",count);
		else
		printf("Case #%d: YES\n",count);
		count++;	
	}		
}
