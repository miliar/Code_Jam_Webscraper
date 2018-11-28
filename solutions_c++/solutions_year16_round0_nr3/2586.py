#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>

void GetDivListIfPrime(char arr[], unsigned long long  divList[])
{
	unsigned long long num;
	for(int n=2; n<=10; ++n)
	{
		num = 0;
		for(int c=0; c<16; ++c)
		{
			if(arr[c] == '1')
			{
				num = num + pow(n, 15-c);
			}
		}
		unsigned long long sqrtN = sqrt(num);
		unsigned long long divisor = 1;
		for(int i=2; i<sqrtN; ++i)
		{
			if(num%i == 0)
			{
				divisor = i;
				break;
			}
		}
		divList[n-2] = divisor;
	}
}

void ConvertToBitArray(char arr[], unsigned long num)
{
	arr[16] = '\0';
	arr[15] = '1';
	for(int i=14; i>0; --i)
	{
		if(num%2==1)
		{
			arr[i]='1';
		}
		else 
		{
			arr[i]='0';
		}
		num = num/2;
	}
	arr[0]='1';
}

bool IsComposite(char arr[], unsigned long long divList[])
{
	bool composite = true;
	unsigned long long num;
	for(int i=2; i<=10; ++i)
	{
		num = 0;
		for(int c=0; c<16; ++c)
		{
			if(arr[c] == '1')
			{
				num = num + pow(i, 15-c);
			}
		}
		if(num%divList[i-2] == 0 && divList[i-2]!=1)
		{
			composite = composite && true;
		}
		else 
		{
			composite = composite && false;
			break;
		}
	}
	return composite;
}

int main()
{
	char a[100];
	unsigned long Test, N, J, count=0;
	scanf("%lu", &Test);
	scanf("%lu %lu", &N, &J);
	char arr[17];
	unsigned long max = (1 << 14);
	unsigned long long divList[9];
	unsigned long long div;
	printf("Case #1:\n");
	for(int i=0; i<max; ++i)
	{
		if(count < J)
		{
			ConvertToBitArray(arr, i);
			GetDivListIfPrime(arr, divList);
			if(IsComposite(arr, divList))
			{
				count++;
				printf("%s ", arr);
				for(int n=2; n<=10; ++n)
				{
					printf("%llu ", divList[n-2]);
				}
				printf("\n");
			}			
		}
		else 
		{
			break;
		}
	}
	return 0;
}