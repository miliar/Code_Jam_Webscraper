#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>
#include<vector>
#include<algorithm>
#include<map>
#include<queue>
#include<set>
#include<limits.h>
#include<iostream>
#include<conio.h>

#define MOD 1000000007

using namespace std;

int main()
{

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

	int t,num;
	
	scanf("%d",&t);
	
	for(int test=1;test<=t;test++)
	{
		int r1;
		
		int a[20]={0};
		int b[20]={0};

		scanf("%d",&r1);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				scanf("%d",&num);

				if(r1-1==i)
				a[num]=1;
			}
		}
		
		int r2;
		scanf("%d",&r2);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				scanf("%d",&num);

				if(r2-1==i)
				b[num]=1;
			}
		}

		int ctr=0;
		int ans;
		
		for(int i=1;i<=16;i++)
		{
			if(a[i]&&b[i])
			{
				ctr++;
				ans=i;
			}
		}
		
		printf("Case #%d: ",test);
		
		if(ctr==1)
		printf("%d\n",ans);
		
		else if(ctr==0)
		printf("Volunteer cheated!\n");

		
		else
		printf("Bad magician!\n");
	}


    return 0;
}
