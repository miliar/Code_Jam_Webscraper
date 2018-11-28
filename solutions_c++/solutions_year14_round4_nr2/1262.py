#pragma comment(linker, "/STACK:100000000")
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iostream>
using namespace std;

typedef long long ll;
#define mod 1000000007
#define pi acos(-1.0)
#define START 1024

int a[1005], sorta[1005], aa[1005];
int b[2100], c[2100];

int sumb(int L, int R)
{
	L += START; R += START;
	int res = 0;
	while(L <= R)
	{
		if(L & 1) res += b[L++];
		if(~R & 1) res += b[R--];
		L >>= 1; R >>= 1;
	}
	return res;
}

int sumc(int L, int R)
{
	L += START; R += START;
	int res = 0;
	while(L <= R)
	{
		if(L & 1) res += c[L++];
		if(~R & 1) res += c[R--];
		L >>= 1; R >>= 1;
	}
	return res;
}

int main()
{
	freopen("B-small-attempt2.in", "r", stdin);
	freopen("B-small-attempt2.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		int n;
		scanf("%d", &n);
		for(int i = 0; i < n; i++)
		{
			scanf("%d", &a[i]);
			sorta[i] = a[i];
		}
		map <int, int> mp;
		int cur = 1;
		sort(sorta, sorta+n);
		for(int i = 0; i < n; i++)
			mp[sorta[i]] = cur++;
		for(int i = 0; i < n; i++)
		{
			a[i] = mp[a[i]];
			aa[i] = a[i];
		}

/*		int res = mod;
		int maxv = 0, maxi = -1;
		for(int i = 0; i < n; i++)
			if(maxv < a[i])
			{
				maxv = a[i];
				maxi = i;
			}
		for(int i = maxi; i < n - 1; i++)
			a[i] = a[i+1];
		for(int m = 0; m < n; m++)
		{
			int cnt = 0;
			memset(b, 0, sizeof(b));
			memset(c, 0, sizeof(c));
			for(int i = 0; i < m; i++)
			{
				cnt += sumb(a[i]+1, 1001);
				b[a[i]+START] = 1;
				for(int j = (a[i]+START) / 2; j > 0; j >>= 1)
					b[j] = b[2*j] + b[2*j+1];
			}
			for(int i = m; i < n - 1; i++)
			{
				cnt += sumc(0, a[i]-1);
				c[a[i]+START] = 1;
				for(int j = (a[i]+START) / 2; j > 0; j >>= 1)
					c[j] = c[2*j] + c[2*j+1];
			}
			cnt += abs(maxi - m);
			res = min(res, cnt);
		}
		//printf("Case #%d: %d\n", t, res);
*/
		int res2 = mod;
		int p[15], good[15];
		for(int i = 0; i < n; i++)
			p[i] = i;
		do
		{
			int i;
			for(i = 1; i < n; i++)
				if(aa[p[i]] < aa[p[i-1]])
					break;
			for(; i < n && aa[p[i]] < aa[p[i-1]]; i++);
			if(i == n)
			{
				int cnt = 0;
				int q[15];
				for(int j = 0; j < n; j++)
					q[j] = j;
				for(int j = 0; j < n; j++)
				{
					int k;
					for(k = 0; k < n; k++)
						if(q[k] == p[j])
							break;
					while(k != j)
					{
						if(k > j)
						{
							swap(q[k], q[k-1]);
							k--;
						}
						else
						{
							swap(q[k], q[k+1]);
							k++;
						}
						cnt++;
					}
				}
				if(res2 > cnt)
				{
					res2 = min(res2, cnt);
					for(int k = 0; k < n; k++)
						good[k] = p[k];
				}
			}
		}while(next_permutation(p, p + n));
/*		if(res2 != res)
		{
			printf("%d %d\n", res, res2);
			for(int i = 0; i < n; i++)
				printf("%d ", aa[i]);
			puts("");
			for(int i = 0; i < n; i++)
				printf("%d ", aa[good[i]]);
			puts("");
		}*/
		printf("Case #%d: %d\n", t, res2);
	}
	return 0;
}