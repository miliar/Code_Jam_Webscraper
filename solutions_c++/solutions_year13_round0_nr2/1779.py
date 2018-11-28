#include<iostream>
#include<cstdio>
using namespace std;
#define MAX 101
int main()
{
	int t,n,m,a[MAX][MAX];
	scanf("%d",&t);
	for(int k=1;k<=t;k++)
	{
		scanf("%d",&n);
		scanf("%d",&m);
		bool poss=true;
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
				scanf("%d",&a[i][j]);
		for(int i=0;i<n;i++)
				for(int j=0;j<m;j++)
				{
					bool checkr=true;
					bool checkc=true;	
					for(int c=0;c<m;c++)
						if(a[i][c]>a[i][j])checkr=false;
					if(!checkr)
					{
						for(int r=0;r<n;r++)
							if(a[r][j]>a[i][j])checkc=false;
					}
					if(!checkr && !checkc)
					{
						poss=false;
						break;
					}
				}
		if(poss)printf("Case #%d: YES\n",k);
		else printf("Case #%d: NO\n",k);
	}
	return 0;
}
