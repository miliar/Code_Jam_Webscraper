#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
int N = 16, all = 50;
long long tmp[15];
int use[100];
char s[100];
int check(long long t)
{
	//printf("%I64d\n", t);
	for (int i = 2; (long long)i * i <= t; i++)
	if(t % i == 0) return i;
	return 0;	
} 
void check()
{
	for (int i = 2; i <= 10; i++)
	{
		use[i] = check(tmp[i]);
		if(use[i] == 0) return; 
	} 
	printf("%s ", s + 1);
	for (int i = 2; i <= 10; i++)
		printf("%d ", use[i]);
	printf("\n"); 
	all--;
} 
void dfs(int now)
{
	long long rem[15];
	for (int i = 2; i <= 10; i++)
		rem[i] = tmp[i];
	if(now == 1 || now == 16)
	{
		s[now] = '1';
		for (int i = 2; i <= 10; i++)
		tmp[i] = (long long)tmp[i] * i + 1ll;	
		if(now == 16) {check(); return;}
		dfs(now + 1); 
	} 
	if(all == 0) return;
	else
	{
		for (int p = 0; p <= 1; p++)
		{
			s[now] = ((p == 0 )? '0' : '1');
			for (int i = 2; i <= 10; i++)
			tmp[i] = (long long)tmp[i] * i + p;
			dfs(now + 1);
			for (int i = 2; i <= 10; i++)
			tmp[i] = rem[i];
		}
		
	}
} 
int main()
{
	//freopen("in.out", "w", stdout);
	 printf("Case #1: \n");
	 dfs(1);
} 
