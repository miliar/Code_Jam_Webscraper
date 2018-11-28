#include <stdio.h>



bool isPalindrome(int n)
{
	char str[100];
	int i, len;

	if( n < 10 )
		return true;

	sprintf(str, "%d",n);

	len = -1;
	while(str[++len]);
	
	for(i=0;i<len;i++)
	{
		if( str[i] != str[len-1-i] )
			return false;
	}

	return true;
}

void main()
{

	FILE *fin = fopen("C-small-attempt0.in","r");
	FILE *fout = fopen("C-small-attempt0.out","w");

	int n, i, a, b, cnt=1, sum;

	fscanf(fin,"%d",&n);

	
	while(n--)
	{
		fscanf(fin, "%d %d", &a, &b);

		sum=0;
		for(i=1;;i++)
		{
			if( i*i > b )
				break;

			if( i*i >= a )
			{
				if( isPalindrome(i*i) && isPalindrome(i) )
					sum++;
			}
		}

		fprintf(fout,"Case #%d: %d\n",cnt++, sum);
	}
}