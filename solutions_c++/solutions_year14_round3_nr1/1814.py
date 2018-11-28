#define _CRT_SECURE_NO_WARNINGS

//source here
#include <iostream>
#include <string>
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <functional>
#include <unordered_map>
#include <assert.h>
using namespace std;

long long gcd(long long a, long long b)
{
	int c;
	while (a != 0) {
		c = a; a = b%a;  b = c;
	}
	return b;
}


int main(){

	freopen("A-small-attempt2.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T;i++)
	{
		long long P, Q;
		int result=1;
		scanf("%lld/%lld", &P, &Q);
		long long g = gcd(P, Q);
		if (g!=1)
		{
			P = P / g;
			Q = Q / g;
		}
		bool flag = true;
		long long temp = Q;
		while (temp >1)
		{
			if (temp % 2 != 0)
			{
				printf("Case #%d: impossible\n", i);
				flag = false;
				break;
			}
			temp = temp / 2;
		}
		if (flag == false)
		{
			continue;
		}
		
		while (P*2<Q)
		{
			Q = Q / 2;
			result++;
		}
		printf("Case #%d: %d\n", i, result);
	}

	return 0;
}

