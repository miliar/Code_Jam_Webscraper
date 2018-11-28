#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

void checkdigit(long long int num, int count[])
{
	if(num == 0)
	{
		if(count[0] == 0)
			count[0]++;
	}
	while(num > 0)
	{
		int digit = num%10;
		if(count[digit] == 0)
			count[digit]++;
		num = num/10;
	}
}

int main()
{
	int T, z = 1;
	scanf("%d",&T);
	while(T--)
	{
		long long int num = 0, newnum = 0;int count[10] = {0}, flag = 1;
		scanf("%lld",&num);

		if(num == 0)
			printf("Case #%d: INSOMNIA\n",z);
		else
		{
			for(long long int i = 1; ;i++)
			{
				newnum = i * num;
				checkdigit(newnum,count);
				for(int j = 0; j < 10; ++j)
				{	
					flag = 1;
					if(count[j] == 0)
					{
						flag = 0;
						break;
					}
				}

				if(flag == 1)
					break;
			}

			printf("Case #%d: %lld\n",z,newnum);
		}
		z++;
	}
	return 0;
}