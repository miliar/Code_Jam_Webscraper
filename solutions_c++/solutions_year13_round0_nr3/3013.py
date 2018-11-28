#include <stdio.h>
#include <stdlib.h>
#include <math.h>

bool palindromes(int t)
{
	int array[10];
	int begin,end,l;
	l = 0;
	while (t)
	{
		array[l] = t%10;
		l++;
		t = t/10;
	}
	if (l==1)
		return true;
	begin = 0;
	end = l-1;
	while (begin<end)
	{
		if (array[begin]!=array[end])
			return false;
		begin++;
		end--;
	}
	return true;
}

int main()
{
	int cases,bb,ee,sum;
	int i,j,k,tt;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d\n",&cases);
	for (i = 1;i<=cases;i++)
	{
		sum = 0;
		scanf("%d %d\n",&bb,&ee);
		j = ceil(sqrt(bb));
		k = floor(sqrt(ee));
		for (tt=j;tt<=k;tt++)
		{
			if (palindromes(tt))
			{
				int origin = tt*tt;
				if (origin>=bb&&origin<=ee&&palindromes(origin))
					sum++;
			}
		}
		printf("Case #%d: %d\n",i,sum);
	}
	return 0;
}
