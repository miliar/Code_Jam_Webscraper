#include<iostream>
#include<stdio.h>
#include<queue>
#pragma warning(disable:4996)

using namespace std;

int N;
int V[1000000];
int q[1000000];

long long int rev(long long int i)
{
	long long int tmp = i;
	long long int cnt = 0;
	long long int ret = 0;
	while (tmp != 0)
	{
		cnt++;
		tmp /= 10;
	}
	tmp = i;
	while (tmp != 0)
	{
		long long int a = tmp % 10;
		for (long long int i = 0; i < cnt-1; i++){
			a *= 10;
		}
		ret += a;
		tmp /= 10;
		cnt--;
	}
	return ret;
}
	
int main()
{
	FILE *in = fopen("input.txt", "r");
	FILE *out = fopen("output.txt", "w");
	int TT;
	long long int ans;
	fscanf(in, "%d", &TT);
	for (int t = 1; t <= TT;t++)
	{
		int head = 0, tail = 0;
		int c;
		fscanf(in, "%d", &N);
		q[++head] = N;
		V[N] = 0;
		while (head != tail)
		{
			c = q[++tail];
			if (c%10!= 0 && rev(c) <= N && rev(c)!=c)
			{
				if (V[rev(c)] == 0)
				{
					q[++head] = rev(c);
					V[rev(c)] = V[c] + 1;
				}
				else if (V[rev(c)] > V[c] + 1)
				{
					V[rev(c)] = V[c] + 1;
					q[++head] = rev(c);
				}
			}
			c--;
			if (c > 0)
			{
				if (V[c] == 0)
				{
					q[++head] = c;
					V[c] = V[c+1] + 1;
				}
				else if (V[c] > V[c+1] + 1)
				{
					V[c] = V[c] + 1;
					q[++head] = c;
				}
			}
		}
		fprintf(out, "Case #%d: %lld\n",t,V[1]+1);
		for (int i = 0; i <= N; i++)
		{
			V[i] = 0;
		}

	}
}