#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


void main()
{
	FILE *infp = fopen("input.txt","r");
	FILE *outfp = fopen("output.txt","w");

	int n, A,B;
	int i,j,k;
	int l;
	int cnt;
	int flag;

	char palindrome[100];
	
	fscanf(infp,"%d",&n);

	for(i=1;i<=n;i++)
	{
		cnt=0;
		fscanf(infp, "%d %d",&A,&B);

		for(j=A;j<=B;j++)
		{
			flag=0;
			itoa(j,palindrome,10);
			l = strlen(palindrome);
			for(k=0;k<=l/2;k++)
			{
				if(palindrome[k]!=palindrome[l-k-1])
				{
					flag = 1;
					break;
				}
			}
			if(flag == 0)
			{
				double x;
				int x1;
				int x2;
				x1 = sqrt(double(j));
				x2 = pow(double(x1),2);
				if(x2>B || j!=x2)
				{
					continue;
				}
				itoa(x1,palindrome,10);
				l = strlen(palindrome);
				for(k=0;k<=l/2;k++)
				{
					if(palindrome[k]!=palindrome[l-k-1])
					{
						flag = 1;
						break;
					}
				}
			}
			if(flag == 0)
				cnt++;
		}
		fprintf(outfp,"Case #%d: %d\n",i,cnt);
	}
}