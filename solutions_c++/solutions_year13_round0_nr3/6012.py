#include<stdio.h>
typedef long long LL;

int isPalindrome(LL num)
{
 	LL n = num;
	LL rev = 0;
	while (num > 0)
	{
	  rev = rev * 10 + num % 10;
	  num = num / 10;
	}	
	if( n == rev )
		return 1;
	return 0;	
	
}

int a[1000];

int main()
{
	int c=0;
	for(int i=1; i<101; i++)
	{
		if(isPalindrome(i))
		{
			if(isPalindrome(i*i))
				a[c++]=i*i;
		}
	}

	int T, A, B, count;
	scanf("%d\n",&T);
	for(int j=1; j<=T; j++) {
		scanf("%d %d\n",&A,&B);
		count = 0; 
		printf("Case #%d: ",j);
		for(int i=0; i<c; i++) {
			if(a[i]>=A && a[i]<=B)
			 count++;
		}
		printf("%d\n",count); 

	}
	
}
