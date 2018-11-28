// Problem C. Fair and Square.cpp : 定义控制台应用程序的入口点。
//


#include<stdio.h>
#include<iostream>
bool ispalindromes(int num)
{
	int lenth = 0,i = 0,j;
	int bit[1000];
	while(num)
	{
		lenth++;
		i++;
		bit[i] = num%10;
		num/=10;
	}
	for(j = 1;j <= lenth/2;j++,i--)
	{
		if(bit[j] != bit[i])
		{
			return false;
		}
				
	}
	return true;
}
void make_table(int table[])
{
	int i;
	table[1] = table[4] = table[9] = 1;
	for(i = 1;i < 32; i++)
	{
		if(ispalindromes(i)&&ispalindromes(i*i))
			table[i*i] = 1;
	}
}
int main(int argc, _TCHAR* argv[])
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	int num,a,b,i,casenum;
	scanf("%d",&num);
	casenum = 1;
	int table[1024];
	for(int i = 0;i < 1024;i++)
		table[i] = 0;
	make_table(table);
	while(num--)
	{
		scanf("%d%d",&a,&b);
		int count = 0;
		for(i = a;i <= b;i++)
			count +=table[i];
		printf("Case #%d: %d\n",casenum,count);
		casenum++;
	}
	fclose(stdin);
	fclose(stdout);
	system("pause");
	return 0;
}


