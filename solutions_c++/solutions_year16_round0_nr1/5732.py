#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <stack>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
#define MOD 1000000007
#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
int num[10];

int div(ull n)
{
	int cnt = 0;
	ull act;
	while(n != 0)
	{
		act = n % 10;
		if(num[act] == 0){num[act] = 1; cnt++;}
		n /= 10;
	}
	return cnt;
}


int main()
{	
	int cnt = 0;
	int t;
	scanf("%d",&t);
	ull n,x,j;
	for(int test = 1; test <= t; test++)
	{
		j = 1;
		cnt = 0;
		for(int i = 0; i < 10; i++) num[i] = 0;
		printf("Case #%d: ",test);
		scanf("%llu",&n);
		if(n == 0){printf("INSOMNIA\n"); continue;}
		while(cnt < 10)
		{
			x = n * j;
			cnt += div(x);
			j++;
		}
		printf("%llu\n",x);
	}


	return 0;
}