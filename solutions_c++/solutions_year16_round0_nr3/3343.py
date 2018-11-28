#include <cstdio>
#include <algorithm>

using namespace std;

int a[64];
int c[100000000];
bool b[1000000000];

int main()
{
	int k = 0;
	for(int i = 2; i < 100000000; ++i)
	{
		if(b[i]) continue;
		c[k++] = i;
		for(int j = i + i; j < 100000000; j += i) b[j] = true;
	}
	int t, N, J;
	scanf("%d %d %d", &t, &N, &J);
	int n = 1;
	for(int i = 0; i < N-1; ++i) n <<= 1;
	printf("Case #1:\n");
	while(J)
	{
		if(!(n&1)) {n++; continue;}
		int t = n;
		for(int i = 0; i < N; i++, t >>= 1)
			a[i] = t&1;
		int d[10];
		for(int i = 2; i <= 10; ++i)
		{
			long long int q = 0, w = 1;
			for(int j = 0; j < N; ++j, w *= i)
				if(a[j]) q += w;
			for(int j = 0; j < k; ++j)
			{
				if(q % c[j] == 0) 
				{
					d[i-2] = c[j];
					goto bbb;
				}
				if((long long int)c[j] * c[j] >= q) goto aaa;
			}
bbb:;
		}
		for(int i = N-1; i >= 0; --i) printf("%d", a[i]);
		printf(" ");
		for(int i = 0; i <= 8; ++i) printf("%d ", d[i]);
		printf("\n");
		J--;
aaa:;
		n++;
	}
}


