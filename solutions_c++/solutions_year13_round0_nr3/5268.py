#include<stdio.h>
#include<math.h>

bool isPal(int num)
{
	int c[110];
	int part=num, i=0, j;

	while(part!=0)
	{
		c[i]=part%10;
		part=part/10;
		++i;
	}
	i--;
	for(j=0; j<i; ++j)
	{
		if(c[j]!=c[i-j])
		{
			return false;
		}
	}
	return true;
}

bool hasSqrt(int num)
{
	float s, d;
	int e;
	s=sqrt(num);
	e=(int)sqrt(num);
	d=(float)e;
	if(s-d>0.0001)
	{
		return false;
	}
	return true;
}

int main(int argc, char *argv[])
{
	int totalCases, caseNum=1;
	int A, B, i, j, counter=0;

	scanf("%d", &totalCases);
	for(i=0; i<totalCases; ++i)
	{
		scanf("%d %d", &A, &B);
		for(j=A; j<=B; ++j)
		{
			if(isPal(j) && hasSqrt(j) && isPal((int)sqrt(j)))
			{
				counter++;
			}
		}
		printf("Case #%d: %d\n", i+1, counter);
		counter=0;
	}
	return 0;
}
