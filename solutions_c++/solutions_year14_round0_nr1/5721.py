#include <iostream>
#include <cstdio>
#include <map>
using namespace std;

int main() {
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		int arr[4][4];
		int arr2[4][4];
		int num1,num2,ans=-1;
		map<int,int> check;
		scanf("%d",&num1);
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
			{
				scanf("%d",&arr[j][k]);
				if(j+1==num1)
					check[arr[j][k]]++;
			}
		scanf("%d",&num2);
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
			{
				scanf("%d",&arr2[j][k]);
				if(j+1==num2)
				{
					if(ans!=-2&&check[arr2[j][k]])
					{
						if(ans!=-1)
							ans=-2;
						else
							ans=arr2[j][k];
					}
				}
			}
		if(ans==-1)
		{
			printf("Case #%d: Volunteer cheated!\n",i);
		}
		else if(ans==-2)
		{
			printf("Case #%d: Bad magician!\n",i);
		}
		else
		{
			printf("Case #%d: %d\n",i,ans);
		}
	}
	return 0;
}
