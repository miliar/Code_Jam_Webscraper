#include <cstdio>
#include <cstring>

int solve(char * input)
{
	int inputLen = strlen(input);
	int flips = 0;
	for (int c = 1; c < inputLen; c++)
	{
		if (input[c] != input[c -1]) 
		    flips++;		
	}
	if (input[inputLen - 1] == '-') 
	    flips++;
	return flips;
}


int main()
{
	int n;
	int c;
	scanf("%d",&c);
	for (n = 0; n < c; n++)
	{
		char a[200];
		int r;
		scanf("%s",&a);
		r = solve(a);
		printf("Case #%d: %d\n",n+1,r);
	}
}
