#include <iostream>
#include <cstdio>
#include <cmath>
#define ll long long
using namespace std;
void add16(ll *arr)
{
	ll i, carry = 0;
	for(i = 14; 1 ; i--)
	{
		if(arr[i] == 0)
		{
			arr[i] = 1;
			break;
		}
		arr[i] = 0;
	}
}
ll findfactor16(ll base, ll *arr, ll *soltable)
{
	ll i, numbase10 = 0, flag = 0;
	for(i = 0; i <= 15; i++)
	{
		numbase10 = numbase10 + arr[i]*pow(base,15 - i);
	}
	for(i = 2; i <= sqrt(numbase10); i++)
	{
		if(numbase10 % i == 0){
			soltable[base-2] = i;
			flag = 1;
			break;
		}
	}
	return flag;
}
int main()
{
	freopen("PA5.in", "r", stdin);
	freopen("PA5.out", "w", stdout);
	ll it, T, N, i, ij, jujj=0, J, tick;
	scanf("%lld", &T);
	scanf("%lld %lld", &N, &J);
	printf("Case #1:\n");
	if(N == 16)
	{
		ll arr[16] = {0}, soltable[9] = {0};
		arr[0] = 1;
		arr[15] = 1;
		while(jujj != J)
		{
			for(i = 2; i <= 10; i++)
			{
				tick = 0;
				if(findfactor16(i,arr,soltable) == 0) 
				{
					tick = 1;
					break;
				}
			}
			if(tick == 0)
			{
				for(ij = 0; ij < 16; ij++)
					printf("%lld",arr[ij]);
				printf(" ");
				for(ij = 0; ij < 9; ij++)
					printf("%lld ", soltable[ij]);
				putchar('\n');
				jujj++;
			}
			add16(arr);
		}
	}
	return 0;
}
