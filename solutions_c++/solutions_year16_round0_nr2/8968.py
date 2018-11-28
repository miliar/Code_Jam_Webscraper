#include <stdio.h>
#include <string.h>

int aaste(char *abc, int i)
{
	if (i == 0 && abc[i] == '-')
		return 1;
	if (i == 0 && abc[i] == '+')
		return 0;
	if (abc[i] == '+')
		return aaste (abc,i-1);
	int j;
	int flag = 1;
	for (j = i ; j >= 0 ; j--)
	{
		if (abc[j] == '+')
		{
			flag = 0;
		}
	}
	if (flag == 1)
		return 1;
	for (j = i ; j >=0 ; j--)
	{
		if (abc[j] == '+')
			abc[j] = '-';
		else
			abc[j] = '+';
	}
	return aaste (abc,i-1) + 1;
}

int main ()
{
	freopen("B-large.in","r",stdin);
	freopen("output_file.out","w",stdout);
	int t;
	scanf ("%d",&t);
	int b;
	for (b = 1; b<=t; b++)
	{
		char aaa[101];
		scanf ("%s",aaa);
		int n = strlen (aaa);
		int temp1 = aaste (aaa,n-1);
			printf ("Case #%d: %d\n",b,temp1);
	}
}
