#include <cstdio>
#include <iostream>
#include <cstring>
#include <ctime>
#include <cstdlib>
using namespace std;
typedef long long lint;
const int MAXN = 100000005;
int prime_table[MAXN];
int tot;
bool valid[MAXN];
void get_prime_table()		//10^8以内的素数表
{
	int i, j;
	int n = MAXN;		//！！！！这里应该是10^8，但是没那么大……
	memset(valid, true, sizeof(valid));
	for (i = 2; i <= n; ++i)
	{
		if (valid[i])
			prime_table[tot++] = i;
		for (j = 0; j < tot && i*prime_table[j] < n; ++j)
		{
			valid[i*prime_table[j]] = false;
			if (i%prime_table[j] == 0)
				break;
		}
	}
}
lint change_base(int base, lint n)
{
	lint ret = 0;
	lint cnt = 1;
	while (n)
	{
		ret += (n % 10) * cnt;
		n /= 10;
		cnt *= base;
	}
	return ret;
}
lint inc(lint n)
{
	lint b = 1;
	while (n % 10 == 1)
	{
		b *= 10;
		n /= 10;
	}
	return (n + 1)*b;
}
//Miller-Rabin
lint mod_mul(lint a, lint b, lint n) {
	lint res = 0;
	while (b) {
		if (b & 1)    res = (res + a) % n;
		a = (a + a) % n;
		b >>= 1;
	}
	return res;
}
lint mod_exp(lint a, lint b, lint n) {
	lint res = 1;
	while (b) {
		if (b & 1)    res = mod_mul(res, a, n);
		a = mod_mul(a, a, n);
		b >>= 1;
	}
	return res;
}
bool miller_rabin(lint n) {
	if (n == 2 || n == 3 || n == 5 || n == 7 || n == 11)    return true;

	lint x, pre, u;
	int i, j, k = 0;
	u = n - 1;    //要求x^u % n

	while (!(u & 1)) {    //如果u为偶数则u右移，用k记录移位数
		k++; u >>= 1;
	}
	int S = 80;
	srand((lint)time(0));
	for (i = 0; i < S; ++i) {    //进行S次测试
		x = rand() % (n - 2) + 2;    //在[2, n)中取随机数
		if ((x%n) == 0)    continue;

		x = mod_exp(x, u, n);    //先计算(x^u) % n，
		pre = x;
		for (j = 0; j < k; ++j) {    //把移位减掉的量补上，并在这地方加上二次探测
			x = mod_mul(x, x, n);
			if (x == 1 && pre != 1 && pre != n - 1)    return false;    //二次探测定理，这里如果x = 1则pre 必须等于 1，或则 n-1否则可以判断不是素数
			pre = x;
		}
		if (x != 1)    return false;    //费马小定理
	}
	return true;
}
lint get_divisor(lint n)	//n是素数返回-1，n是合数返回一个因数
{
	if (n < 4)
		return -1;
	if (n % 2 == 0)	return 2;
	if (n % 3 == 0)	return 3;
	if (n % 5 == 0)	return 5;
	if (n % 7 == 0)	return 7;
	if (n % 11 == 0)return 11;
	if (miller_rabin(n))
		return -1;
	for (int j = 0; j < tot; ++j)
	{
		if (n % prime_table[j] == 0)
			return prime_table[j];
	}
}
int main()
{
	get_prime_table();
	//printf("%d %d %d %d %d\n",change_base(2,101),change_base(3,101),change_base(4,101),change_base(5,101),change_base(6,101));
	int N, J, T, cas;
	lint num;
	int i, j;
	lint Mod;
	lint divisor[12];
	scanf("%d", &T);
	for (cas = 1; cas <= T; ++cas)
	{
		scanf("%d %d", &N, &J);
		printf("Case #%d:\n", cas);
		num = 1;
		for (i = 1; i < N; ++i)
			num *= 10;
		Mod = num;
		//printf("%lld\n",num);
		for (i = 0; i < J; ++i)
		{
			num = inc(num);
			int ttt = num & 1;
			if (num / Mod != 1 || ttt != 1)		//剪枝：第一位和最后一位都必须是1
			{
				--i;
				continue;
			}
			for (j = 2; j <= 10; ++j)
			{
				lint cnt = change_base(j, num);
				lint tmp = get_divisor(cnt);
				if (tmp == -1)
					break;
				divisor[j] = tmp;
			}
			if (j < 11)		//这个数不是jamcoin
				--i;
			else
			{
				printf("%lld ", num);
				for (j = 2; j <= 10; ++j)
					printf("%lld ", divisor[j]);
				printf("\n");
			}
		}
	}
	return 0;
}