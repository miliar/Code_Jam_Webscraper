#include <stdio.h>
#include <string.h>

int stepsp(char *a, int i)
{
	if (i == 0 && a[i] == '-')
		return 1;
	if (i == 0 && a[i] == '+')
		return 0;
	if (a[i] == '+')
		return stepsp (a,i-1);
	int j;
	int flag = 1;
	for (j = i ; j >= 0 ; j--)
	{
		if (a[j] == '+')
		{
			flag = 0;
		}
	}
	if (flag == 1)
		return 1;
	for (j = i ; j >=0 ; j--)
	{
		if (a[j] == '+')
			a[j] = '-';
		else
			a[j] = '+';
	}
	return stepsp (a,i-1) + 1;
}

/*int stepsn(char *a, int i)
{
        if (i == 0 && a[i] == '+')
                return 1;
        if (i == 0 && a[i] == '-')
                return 0;
        if (a[i] == '-')
                return stepsn (a,i-1);
        int j;
        int flag = 1;
        for (j = i ; j >= 0 ; j--)
        {
                if (a[j] == '-')
                {
                        flag = 0;
                }
        }
        if (flag == 1)
                return 1;
        for (j = i ; j >=0 ; j--)
        {
                if (a[j] == '-')
                        a[j] = '+';
                else
                        a[j] = '-';
        }
        return stepsn (a,i-1) + 1;
}*/


int main ()
{
	freopen("B-large.in", "r", stdin);
	freopen("file_name.out", "w", stdout);
	int t;
	scanf ("%d",&t);
	int p;
	
	for (p=1; p<=t; p++)
	{
		char a[101];
		scanf ("%s",a);
		int n = strlen (a);
		int temp1 = stepsp (a,n-1);
//		int temp2 = stepsn (a,n-1);
//		if (temp1 <= temp2+1)
			printf ("Case #%d: %d\n",p,temp1);
//		else
//			printf ("%d\n",temp2+1);
	}
}
