#include <iostream>
using namespace std;
#include<cstdio>
int main() {
	int t;
	scanf("%d",&t);
	int n=t;
	while(t--)
	{
		int a,b;
		int arr[4][4];
		scanf("%d",&a);
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		scanf("%d",&arr[i][j]);
		scanf("%d",&b);
		int arb[4][4];
		for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		scanf("%d",&arb[i][j]);
		a--;b--;
		int ans,noc=0;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(arr[a][i]==arb[b][j])
				{
					noc++;
					ans=arr[a][i];
				}

			}
		}
		if(noc==1)
		printf("Case #%d: %d\n",n-t,ans);
		else if(noc==0)
		printf("Case #%d: Volunteer cheated!\n",n-t);
		else printf("Case #%d: Bad magician!\n",n-t);
	}
	return 0;
}
