#include <iostream>
#include <algorithm>
using namespace std;
typedef long long lint;
const lint inf = lint(1000 * 1000 * 1000)*lint(1000 * 1000 * 1000);
int N;

int a[1000];
int cnt = 500;

lint getV(int base)
{
	lint v = 0;
	for (int i = 0; i < N; i++)
	{
		if (v >= inf) return inf;
		v = v*base + a[i];
	}
	return v;
}



bool canDiv(int d, int base)
{
	lint v = 0;
	for (int i = 0; i < N; i++)
	{
		v = (v*base + a[i])%d;
	}
	return (v == 0);
}

lint div(lint v, int base)
{
	v = min(v - 1, lint(1000));
	for (int i = 2; i <= v; i++)
		if (canDiv(i, base)) return i;
	return -1;
}
void show(lint v, int base)
{
	int b[50];
	int l = 0;
	while (v)
	{
		b[l++] = v%base;
		v /= base;
	}
	for (int i = l - 1; i >= 0; i--) printf("%d", b[i]);
	printf(" ");
}

void check()
{
	lint v[11], d[11];
	for (int base = 2; base <= 10; base++)
	{
		v[base] = getV(base);
		d[base] = div(v[base],base);
		if (d[base] == -1) return;
		
	}
	cnt--;
	//printf("cnt = %d\n", cnt--);
	for (int i = 0; i < N; i++) printf("%d", a[i]);
	//for (int i = 2; i <= 10; i++) printf(" %I64d", v[i]);
	//printf("\n");
	for (int i = 2; i <= 10; i++) printf(" %I64d", d[i]);
	printf("\n");
//	for (int i = 2; i <= 10; i++) show(d[i],i);
//	printf("\n");
	if (cnt == 0) exit(0);
	//printf("\n");
}



void gen(int num, int last)
{
	if (num == N/2)
	{
		check();
		return;
	}
	a[num] = 0; gen(num + 1,0 );
	a[num] = 1; gen(num + 1,1);
}


int main()
{
	
	freopen("output.txt", "w", stdout);
	printf("Case #1:\n");
	scanf("%d", &N);
	a[0] = 1;
	a[N - 1] = 1;
	gen(1,0);
	return 0;
}