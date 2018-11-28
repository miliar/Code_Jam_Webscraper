#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <map>
using namespace std;

map<long long int, int> cache;

#if 0
long long int get_divisor(long long int val)
{
	long long int div;
	long long int max_cmp;

	if(val % 2 == 0)
		return 2;

	max_cmp = (long long int)sqrt(val);
	for (div=3; div <= max_cmp; div+=2) {
		if (val % div == 0)
			return div;
	}
	return div;
}
#endif

long long int get_divisor(long long int val)
{
	long long int div;
	long long int max_cmp;

	map<long long int,int>::iterator it;

	it = cache.find(val);
	if (it != cache.end())
		return it->second;

	if (val == 1)
		return 0;

	if (val == 2)
		return 0;

	if (val % 2 == 0)
		return 2;

	max_cmp = (long long int)sqrt(val);
	for (div=3; div <= max_cmp; div+=2) {
		if (val % div == 0) {
			cache[val] = div;
			return div;
		}
	}

	cache[val] = 0;
	return 0;
}


void dec2bin(long long int coin_dec, int coinlen, char *coin_bin)
{
	for (int i=0; i<coinlen; ++i) {
		coin_bin[i] = ((coin_dec >> i) & 1) + '0';
	}
	coin_bin[coinlen] = 0;
}

int check_validation(char *coin_bin)
{
	long long int num;
	
	for(int i=2; i<=9; ++i) {
		num = strtoll(coin_bin, NULL, i);
		if(get_divisor(num) == 0)
			return 0;
	}
	return 1;
}

void print_coin(char *coin_bin)
{
	long long int val;

	/* print coin value */
	printf("%s", coin_bin);

	for (int i=2; i<=9; ++i) {
		val = strtoll(coin_bin, NULL, i);
		printf(" %lld", get_divisor(val));
	}
	printf("\n");
}

void generate_coin(int coinlen, int need_rescnt)
{
	int res_cnt = 0;
	long long int coin;
	long long int begin, end;
	char coin_bin[504];
	
	begin = (1 << (coinlen-1)) + 1;
	end = 1 << coinlen;
		
	for (coin = begin; coin < end; coin+=2) {
		dec2bin(coin, coinlen, coin_bin);
		if(check_validation(coin_bin)) {
			print_coin(coin_bin);
			res_cnt++;
		}
		if(res_cnt >= need_rescnt)
			return;
	}
}

int main()
{
	int tcase, n, j;

	scanf("%d", &tcase);

	for(int i=1; i<=tcase; ++i) {
		scanf("%d%d", &n, &j);
		printf("Case #%d:\n", i);
		generate_coin(n, j);
	}
	return 0;
}
