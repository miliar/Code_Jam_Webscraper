#include<bits/stdc++.h>
using namespace std;

int he[3000];
int ff[51][51];
int ans[51];
int found[3000];
set<int> s;
int main()
{
	int test;
	scanf("%d",&test); getchar();
	for(int a=1;a<=test;a++)
	{
		int k=0,r;
		memset(he,0,sizeof(he));
		memset(found,0,sizeof(found));
		scanf("%d",&r); getchar();
		for(int b=0;b<2*r-1;b++)
			for(int c=0;c<r;c++)
			{
				scanf("%d",&ff[b][c]);
				he[ff[b][c]]++;
			}
		for(int b=0;b<2*r-1;b++)
		{
			for(int c=0;c<r;c++)
			{
				if(he[ff[b][c]]%2!=0)
				{
					//printf("%d ",he[ff[b][c]]);
					if(found[ff[b][c]]==0)
					{
						//printf("here\n");
						ans[k]=ff[b][c];
						//printf("%d: %d\n",k,ans[k]);
						found[ff[b][c]]^=1;
						k++;
					}
				}
			}
			//printf("\n");
		}
		sort(ans,ans+k);
		printf("Case #%d:",a);
		for(int b=0;b<k;b++)
			printf(" %d",ans[b]);
		printf("\n");
	}
}
