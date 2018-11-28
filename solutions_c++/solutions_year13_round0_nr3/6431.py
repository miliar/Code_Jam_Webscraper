#include<conio.h>
#include<stdio.h>
#include<math.h>
int checkpalin(int x)
{
	int m=x;
	int pal=0;
	int rem=0;int div =1;
	while (x)
	{
		rem = x%10;
		x = x/10;
		pal = pal*10 + rem;
	}
	if (pal == m)
		return true;
	else
		return false;
}
int checknum(int num1,int num2)
{
	int i,no=0;
//	printf("HI ");
	for (i = ceil(sqrt(num1)); i<=(sqrt(num2));i++)
	{
		
		if(checkpalin(i * i))
		{
			if (checkpalin(i))
			{
					no++;
			}
		
		}
		
		
	}

	return no;
}
main()
{
	int n,i,num1,num2;
	scanf("%d",&n);
	{
	int op[n];
		for (i=0;i<n;i++)
		{
			scanf("%d %d",&num1,&num2);
			op[i] = checknum(num1,num2);
		}
		for(i=0;i<n;i++)
		{
			printf ("Case #%d: %d\n",i+1,op[i]);
			
		}
	}

		getch();
}
