#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <queue>
#include <stack>
using namespace std;
uint64_t ans[11];
const int N = 16;
int base2[N];
uint64_t base2num(int base)
{
	uint64_t val = 0;
	for(int i = N - 1; i >= 0; --i)
	{
		val *= base;
		val += base2[i];
	}
	return val;
}
bool isPrime(uint64_t val,int base)
{
	for(int i = 2; i * i <= val; ++i)
	{
		if(val % i == 0) //has a divisor
		{
			ans[base] = i; //is a divisor
			return false;
		}
	}
	return true;
}
bool dfs(uint64_t num)
{
	for(int i = 0; i < N; ++i)
	{
		base2[i] = num & 1;
		num >>= 1;
	}
	for(int i = 2; i <= 10; ++i)
	{
		uint64_t val = base2num(i);
		if(isPrime(val,i))
			return false;
	}
	return true;
}
void print()
{
	for(int i = N - 1; i >= 0; --i)
		printf("%d",base2[i]);
	for(int i = 2; i <= 10; ++i)
		printf(" %d",ans[i]);
	printf("\n");
	return;

}
int main()
{
//	freopen("in.txt","r",stdin);
//	freopen("a_out.txt","w",stdout);
	uint64_t base = (1 << 15) + 1;
	int cnt = 0;
	for(int i = 0;cnt < 50;++i)
	{
		if(dfs(base + (i << 1)))
		{
			cnt++;
			print();
		}
	}
	return 0;
}
