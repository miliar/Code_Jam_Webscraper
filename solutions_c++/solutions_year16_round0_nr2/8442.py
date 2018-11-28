#include <iostream>
#include <stdio.h>
#include<string.h>
#include<stdlib.h>
using namespace std;
int l;
int count_no = 0;

int isdone(int pancake[])
{
	int i;
	for(i = 0; i<l; i++)
	{
		if(pancake[i] != 1)
			break;
	}

	if(i<l)
		return 1;
	return 0;
}

void flip_value(int a[], int position)
{
	for(int i = 0; i < position; i++)
		a[i] = 1 - a[i];
      count_no++;
}

void task(int a[])
{
		int i;
	while(isdone(a))
	{
		if(a[0] == 0)
		{
			for(i = 0; i < l; i++)
			{
				if(a[i] == 1)
					break;
			}
			flip_value(a, i);
		}

		if(isdone(a))
		{
			if(a[0] == 1)
			{
				for(i = 0; i < l; i++)
				{
					if(a[i] == 0)
						break;
				}
			flip_value(a, i);
			}
		}

	}
}

int main() {

	char s[120];
	int a[120], t;
	int cas = 1;
	scanf("%d", &t);

	while(t>0)
	{
        l=0;
		count_no = 0;
		s[0]='\0';
		scanf("%s",s);
		l = strlen(s);
	 for(int i = 0; i < l; i++)
	{
		if(s[i]=='+')
		{
			a[i] = 1;
		}
		else if(s[i] == '-')
		{
			a[i] = 0;
		}
	}
		task(a);
		printf("Case #%d: %d\n", cas,count_no);
		cas++;
		t--;
	}
	return 0;
}
