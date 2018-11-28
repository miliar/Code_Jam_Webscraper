#include <cstdio>
using namespace std;

int mul[8][8] = 
{
	{0, 1, 2, 3},
	{1, 4, 3, 6},
	{2, 7, 4, 1},
	{3, 2, 5, 4},
};

char buf[10050];
int t, l, a[110050], pt;
long long x;

int walk(int v)
{
	int cv = 0;
	while(cv != v && pt < l)
		cv = mul[cv][a[pt++]];
	return cv;
}

int main()
{
	for(int i = 0; i < 8; i++)
		for(int j = 0; j < 8; j++)
			if(i >= 4 || j >= 4)
				mul[i][j] = mul[i % 4][j % 4] ^ ((i ^ j) & 4);
	scanf("%d", &t);
	for(int tt = 1; tt <= t; tt++)
	{
		scanf("%d %lld %s", &l, &x, buf);
		if(x >= 8)
			x = 8 + x % 4;
		for(int i = 0; i < x; i++)
			for(int j = l * i; j < l * i + l; j++)
				a[j] = (buf[j % l] - 'i' + 1);
		l *= x; pt = 0;
		printf("Case #%d: ", tt);
		if(walk(1) == 1 && walk(2) == 2 && walk(-1) == 3)
			printf("YES\n");
		else
			printf("NO\n");
	}

	return 0;
}
