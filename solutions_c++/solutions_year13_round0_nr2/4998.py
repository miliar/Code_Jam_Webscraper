#include<iostream>
#include<stdio.h>
using namespace std;
int n,m;
int a[12][12];
int searchRowNext(int i,int j,int x)
{		if(i==n)
			return 0;
		if(a[i][j]==x)
		{
			if(i==n-1)
				return 1;
			else 
		 		return 1+searchRowNext(i+1,j,x);
		}
		return  0;
	
}
int searchRowPrev(int i,int j,int x)
{		if(i==-1)
			return 0;
		if(a[i][j]==x)
		{
			if(i==0)
				return 1;
			else 
		 		return 1+ searchRowPrev(i-1,j,x);
		}
		return  0;
	
}
int searchColumnNext(int i,int j,int x)
{		if(j==m)
			return 0;
		if(a[i][j]==x)
		{
			if(j==m-1)
				return 1;
			else 
		 		return 1+searchColumnNext(i,j+1,x);
		}
		return  0;
	
}
int searchColumnPrev(int i,int j,int x)
{		if(j==-1)
			return 0;
		if(a[i][j]==x)
		{
			if(j==0)
				return 1;
			else 
		 		return 1+ searchColumnPrev(i,j-1,x);
		}
		return  0;
	
}

int call(int i, int j,int x)
{		
		int srn = searchRowNext(i+1,j,x);
		//cout<<"srn="<<srn<<endl;
		int srp = searchRowPrev(i-1,j,x);
		//cout<<"srp="<<srp<<endl;
		if(srn+srp==n-1)
			return 1;
		int scn = searchColumnNext(i,j+1,x);
		//cout<<"scn="<<scn<<endl;
		int scp = searchColumnPrev(i,j-1,x);
		//cout<<"scp="<<scp<<endl;
		if(scn+scp==m-1)
			return 1;
		return 0;
}
int main()
{	int t;
	scanf("%d",&t);
	int c = 1;
	while(t--)
	{	scanf("%d %d",&n,&m );
		for(int i =0;i<n;i++)
			for(int j=0;j<m;j++)
				scanf("%d",&a[i][j]);
		bool ans = true;
		int check = 0;
		for(int i =0;i<n;i++)
		{
			for(int j = 0 ;j<m;j++)
			{	if(a[i][j]!=1)
				continue;
					int x = call (i,j,a[i][j]);
					//cout<<x<<" "<<i<<" "<<j<<endl;
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
		printf("Case #%d: NO\n",c );
		else
		printf("Case #%d: YES\n",c );
		c++;
		
	}
	
		
}
