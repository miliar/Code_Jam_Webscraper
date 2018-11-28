#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
void main()
{
	FILE *fp,*fp1;
	int test,add,testt=0,index,sum=0,count=0;
	int flag[10];
	long *no,temp;
	scanf("%d",&test);
	fp = fopen("file1.in", "r");
	fp1 = fopen("file.in", "w");
	no = (long*)malloc(test*sizeof(long));
	fscanf(fp,"%li\n", &no[testt]);
	while (testt <test)
	{
		fscanf(fp,"%li\n", &no[testt]);//scanf("%li",&no[testt]);
		testt++;
	}
	testt = 0;
	while (testt < test)
	{
		sum = 0;
		count = 0;
		for (index = 0; index < 10; index++)
			flag[index] = 0;
		temp = no[testt];
		add = no[testt];
		if (temp == 0)
			count = 100;
		while (sum < 10 && count < 100)
		{
			if (temp == 0)
			{
				temp = no[testt] +add;
				no[testt] = temp;
			}
			if (temp < 10 && flag[temp] == 0)
			{
				sum++;
				flag[temp] = 1;
				temp = 0;
			}
			else if (temp>9)
			{
				if (flag[temp % 10] == 0)
				{
					flag[temp % 10] = 1;
					sum++;
				}
				temp = temp / 10;
			}
			else
			{
				temp = temp / 10;
				count++;
			}
		}
		if (count == 100)
			fprintf(fp1,"Case #%d: INSOMNIA\n",testt+1);
		else if (sum == 10)
			fprintf(fp1,"Case #%d: %d\n", testt+1,no[testt]);
		testt++;
	}
	_getch();
}