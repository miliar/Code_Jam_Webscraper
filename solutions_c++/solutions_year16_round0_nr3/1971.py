#include <iostream>
#include <cstdio>
#include <vector>
#include "sitispasttenseofsat.h"
using namespace std;

void preprocess()
{
	vector<bool> prim(maxn);
	for(int i = 2;i <= maxn;i++)
	{
		if(prim[i])
		{
			prime.push_back(i);
			for(int j = i*i;j <= maxn;j += i)
			{
				prim[i] = false;
			}
		}
	}
}

int recurse(int idx, int mask)
{
	if(idx == n-1)
	{
		bool done = true;
		for(int base = 2;base < 11;base++)
		{
			int tmp;
			for(int i = 1;i <= mask;i <<= 1)
			{
				tmp += (mask&(1<<i))*base;
			}

			for(auto it: prime)
			{
				if(tmp%it == 0)
				{
					res.push_back(it);
					done = false;
					break;
				}
			}
		}
		if(int(res.size()) < 10)
		{
			return;
		}
		else
		{
			j--;
			printf("%d ", tmp)
			for(auto it: res) printf("%d ", it);
			printf("\n");
		}
	}
}

int main(void)
{
	int t;
	scanf("%d", &t);
	for(int tt = 1;tt <= t;tt++)
	{
		int n, j;
		scanf("%d%d", &n, &j);

		int mask = 1+(1<<(n-1));
		recurse(1, mask);
	}
}