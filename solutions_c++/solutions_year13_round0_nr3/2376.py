#include <iostream>
#include <cstdio>

using namespace std;

int t;

bool h[150];
int n , m;
int dig[110];

long long getval(int len)
{
	long long t = 1;
	long long ret = 0;
	for (int i = 0 ; i < len ; i ++)
	{
		ret += t * dig[i];
		t *= 10;
	}
	return ret;
}
bool ispal(long long s)
{
	int sd[110];
	int c = 0;
	while (s)
	{
		sd[c ++] = s%10;
		s/=10;
	}
	for (int i = 0 ; i < c/2 ; i ++)
	{
		if( sd[i] != sd[c -1 - i])return false; 
	}
	return true;
}
int ans = 0;
long long a , b;
void generatePally1(int p , int len)
{
	if (p == len/2)
	{
		for (int i = 0 ; i <= 9 ; i ++)
		{
			dig[p] = i;
			long long v = getval(len);
			long long sq = v * v;
			if (sq >= a && sq <= b && ispal(sq))
			{
				ans ++;
			}
		}
		return;
	}
	int st = 0;
	if (p == 0)st = 1;
	for (int i = st ; i <= 9 ; i ++){

		dig[ p ] = i;
		dig[ len - 1 - p ] = i;
		generatePally1(p + 1 , len);

	}
}
void generatePally2(int p , int len)
{
	int st = 0;
	if (p == len/2)
	{
		long long v = getval(len);
		long long sq = v * v;
		if (ispal(sq) && sq >= a && sq <= b)
		{
			ans ++;
		}
		return;
	}
	if (p == 0)st = 1;
	for (int i = st ; i <= 9 ; i ++){

		dig[ p ] = i;
		dig[ len - 1 - p ] = i;
		generatePally2(p + 1 , len);

	}
}

int main()
{
	freopen("C-large-1.in" , "r" , stdin);
	freopen("C-large-1.out" , "w" , stdout);

	scanf("%d" , &t);
	int cas = 0;

	while (t --)
	{
		cas ++;

		ans = 0;
		scanf("%lld %lld" , &a , &b);
	//	memset(dig  , 0 , sizeof(dig));
		for (int i = 1 ; i <= 8 ; i ++){
			if (i % 2 == 0){
				generatePally2(0 , i);
			}
			else{
				generatePally1(0 , i);
			}
		}
		printf("Case #%d: %d\n" , cas , ans);
		
		
	}
}