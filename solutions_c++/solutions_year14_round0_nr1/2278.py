#include <stdio.h>
#include <string.h>
#include "../../input.h";
#include "../../output.h";
//#define print(f,...) printf(f,__VA_ARGS__)
int T,row,res,count;
int case_num;
int main()
{
	scanf("%d",&T);
	for (case_num = 1; case_num <= T; case_num++)
	{
		print("Case #%d: ",case_num);
		bool a[17]={0};
		scanf("%d",&row);
		for (int i = 1; i <= 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				int k;
				scanf("%d",&k);
				if(i==row) a[k]=1;
			}
		}
		res=0;
		count=0;
		scanf("%d",&row);
		for (int i = 1; i <= 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				int k;
				scanf("%d",&k);
				if (i==row&&a[k])
				{
					count++;
					res=k;
				}
			}
		}
		if (count==1)
		{
			print("%d\n",res);
		}
		else if (count>1)
		{
			print("Bad magician!\n");
		}
		else
		{
			print("Volunteer cheated!\n");
		}
	}	
}