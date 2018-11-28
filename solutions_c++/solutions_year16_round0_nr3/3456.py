#include <bits/stdc++.h>
using namespace std;

int n = 6;

long long interpret(int x , int b)
{
	long long res = 0 , now = 1;
	for(int i = 0 ; i < n ; i++)
	{
		if(x & 1)res += now;
		x >>= 1;
		now *= b;
	}
	return res;
}
long long check(long long val)
{
	for(long long i = 2 ; i * i <= val ; i++)
		if(val % i == 0)return i;
	return -1;
}
void print(int x , int dep)
{
	if(dep == n)printf("%d" , x);
	else
	{
		print(x >> 1 , dep + 1);
		printf("%d" , x & 1);
	}
}
int main()
{
	int T;scanf("%d" , &T);
	for(int tt = 1 ; tt <= T ; tt++)
	{
		printf("Case #%d:\n" , tt);
		int j;scanf("%d%d" , &n , &j);
		for(int x = 0 ; x < (1 << n) ; x++)
		{
			if(x % 2 == 0)continue;
			if((x >> (n - 1)) == 0)continue;
			bool ok = true;
			//printf("x = %d , " , x);
			//print(x , 1);printf("\n");
			for(int i = 2 ; i <= 10 ; i++)
			{
				long long v = check(interpret(x , i));
				if(v == -1){ok = false;break;}
			}
			if(ok)
			{
				print(x , 1);
				for(int i = 2 ; i <= 10 ; i++)
					printf(" %lld" , check(interpret(x , i)));
				printf("\n");
//					printf(" base = %d , val = %lld , factor = %lld\n" 
//						,i , interpret(x , i),check(interpret(x , i)));
//				printf("\n\n");
				j--;
				if(j == 0)break;
			}
		}
	}
}