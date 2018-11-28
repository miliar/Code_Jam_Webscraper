#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

char nums[15];

bool palindrome(long long number)
{
	itoa(number, nums, 10);
	int size = strlen(nums);
	for(int i = 0; i < size/2+1; i++)
	{
		if(nums[i] != nums[size-1-i])
		{
			return false;
		}
	}
	return true;
}


int main()
{
	int num;
	scanf("%d", &num);
	long long less, larger;
	for(int i = 1; i <= num; i++)
	{
		scanf("%lld %lld", &less, &larger);
		long long sqrtLess = (long long)sqrt((double)less);
		long long sqrtLarger = (long long)sqrt((double)larger);
		if(sqrtLess * sqrtLess < less)
			sqrtLess++;

		int count = 0;
		for(long long j = sqrtLess; j <= sqrtLarger; j++)
		{
			if(palindrome(j) && palindrome(j*j))
				count++;
		}
		printf("Case #%d: %d\n", i, count);
	}




	return 0;
}