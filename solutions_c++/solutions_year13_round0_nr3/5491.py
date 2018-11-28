#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <map>
#include <cmath>
#include <string>

using namespace std;

#define HOME_PC
#define SMALL_SIZE 1000

struct cmp
{
	bool operator()(int a,int b)
	{
		return (a<=b);
	}
};

bool palindrome(int num)
{
	int rev = 0,dig=0;
	int n = num;
	while(n > 0)
	{
		dig = n % 10;
		rev = rev*10 + dig;
		n = n / 10;
	}

	return (num == rev);
}

int main()
{
	int t, y=0;
	//16 bits to denote the positions of Xs, Os, and board Ts
	int fAs[SMALL_SIZE];
	int count = 0;
	struct cmp cmpObj;
		
#ifdef HOME_PC
	FILE *err = freopen ("in.txt","r",stdin);
	if(!err)
	{
		printf("Error opening file");
		exit(0);
	}

	freopen ("out.txt","w",stdout);
#endif

	scanf("%d", &t);

	//precompute
	for(int i=1;i<=sqrt(1000);i++)
	{
		if(palindrome(i))
		{
			if(palindrome(i*i))
			{
				fAs[count] = i*i;
				count++;
			}
		}
	}

	while(y < t)
	{
		int a,b,ans=0;
		//Take input
		cin>>a>>b;
		int l = lower_bound(fAs,fAs+count,a) - fAs;
		int r = lower_bound(fAs,fAs+count,b,cmpObj) - fAs;

		
		ans = (r-l);
		/*if(r >= count)
		{
			if(l >= count)
				ans = 0;
			else
				ans = r-l;
		}

		if(fAs[l] == a)

		else if(l == r)
		{
			if(fAs[l] == a | fAs[l] == b)
				ans = 1;
			else
				ans = 0;	
		}*/

		printf("Case #%d: %d\n",y+1,ans);

		y++;
	}

	return 0;
}
