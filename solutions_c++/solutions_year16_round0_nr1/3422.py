#include <cstdio>

	int markedPosition[10];
	
	
int mkn(int input)	
{
	int rc;
	while (input > 0)
	{
		rc |= markedPosition[input%10];
		input /= 10;
	}
	return rc;
}

int solve(int input)
{
	int marked = 0;
	int solved = 0;
	int current = input;
	if (input == 0)
	    return -1;
	for (int c = 0; c< 10; c++)
	{
	    markedPosition[c] = 1<<c;
	    solved |= markedPosition[c];	    
	}
	while (marked != solved)
	{
		marked |= mkn(current);
		current += input;
	}
	return current - input;	
}
 

int main()
{
	int n;
	int c;
	scanf("%d",&c);
	for (n = 0; n < c; n++)
	{
		int a;
		int r;
		scanf("%d",&a);
		r = solve(a);
		if (r > 0)
		printf("Case #%d: %d\n",n+1,r);
		else
		printf("Case #%d: INSOMNIA\n",n+1);
	}
}
