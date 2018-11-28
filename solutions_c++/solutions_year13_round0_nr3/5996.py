#include<iostream>
#include<cmath>
using namespace std;
int is_square(int a)
{
	int square=(int)floor(sqrt(a));
	//printf("root %d\n",square);
	return (square*square==a);
}
int is_palindrome(int a)
{
	int rev=0,a1=a;
	
	while(a)
	{
		rev=(a%10)+rev*10;
		a/=10;
	}
	//printf("reverse %d\n",rev);
	return (rev==a1);
}
main()
{
	int t,count1=1;
	scanf("%d",&t);
	while(t--)
	{
	int a,b,count=0;	
	scanf("%d%d",&a,&b);
	//printf("check palindrome %d",is_palindrome(1210));
	for(int i=a;i<=b;i++)
	{
		if(is_square(i))
		{
			int root=(int)sqrt(i);
			if(is_palindrome(root) && is_palindrome(i))
			{
				//printf("i %d\n",i);
				count++;
			}
		}
	}
	printf("Case #%d: %d\n",count1++,count);
	}
	}
