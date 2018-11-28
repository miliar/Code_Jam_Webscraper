#include <cstdio>
const int maxn = 100, maxm = 100, maxs = 500;
int t, r, c, perm[maxn], fa[maxs];
int find(int x)
{
	return x == fa[x] ? x : fa[x] = find(fa[x]);
}
void merge(int u, int v)
{
	//printf("merge (%d, %d) (%d, %d)\n", u / ((c + 1) * 2), u % ((c + 1) * 2), v / ((c + 1) * 2), v % ((c + 1) * 2));
	fa[find(u)] = find(v);
}
int idx(int x)
{
	if(x <= c)
		return x * 2 - 1;
	x -= c;
	if(x <= r)
		return (x * 2 - 1) * ((c + 1) * 2) + (c * 2);
	x -= r;
	if(x <= c)
		return (r * 2) * ((c + 1) * 2) + ((c - x + 1) * 2 - 1);
	x -= c;
	return ((r - x + 1) * 2 - 1) * ((c + 1) * 2);
}
int main()
{
	scanf("%d", &t);
	for(int Case = 1; Case <= t; ++Case)
	{
		scanf("%d%d", &r, &c);
		for(int i = 0; i < r + c << 1; ++i)
			scanf("%d", perm + i);
		int ans = -1;
		for(int msk = 0; msk < 1 << (r * c); ++msk)
		{
			for(int i = 0; i < maxs; ++i)
				fa[i] = i;
			/*
			for(int i = 0; i < r; ++i)
			{
				for(int j = 0; j < c; ++j)
					printf("%c", "\\/"[(msk >> (i * c + j)) & 1]);
				putchar('\n');
			}
			*/
			for(int i = 0; i < r; ++i)
				for(int j = 0; j < c; ++j)
					if((msk >> (i * c + j)) & 1) // /
					{
						merge(((i + 1) * 2 - 1 - 1) * ((c + 1) * 2) + ((j + 1) * 2 - 1), ((i + 1) * 2 - 1) * ((c + 1) * 2) + ((j + 1) * 2 - 1 - 1));
						merge(((i + 1) * 2 - 1 + 1) * ((c + 1) * 2) + ((j + 1) * 2 - 1), ((i + 1) * 2 - 1) * ((c + 1) * 2) + ((j + 1) * 2 - 1 + 1));
					}
					else
					{
						merge(((i + 1) * 2 - 1 - 1) * ((c + 1) * 2) + ((j + 1) * 2 - 1), ((i + 1) * 2 - 1) * ((c + 1) * 2) + ((j + 1) * 2 - 1 + 1));
						merge(((i + 1) * 2 - 1 + 1) * ((c + 1) * 2) + ((j + 1) * 2 - 1), ((i + 1) * 2 - 1) * ((c + 1) * 2) + ((j + 1) * 2 - 1 - 1));
					}
			bool flag = 1;
			for(int i = 0; i < r + c; ++i)
				flag &= find(idx(perm[i * 2])) == find(idx(perm[i * 2 + 1]));
			if(flag)
			{
				ans = msk;
				break;
			}
		}
		printf("Case #%d:\n", Case);
		if(ans == -1)
			puts("IMPOSSIBLE");
		else
			for(int i = 0; i < r; ++i)
			{
				for(int j = 0; j < c; ++j)
					printf("%c", "\\/"[(ans >> (i * c + j)) & 1]);
				putchar('\n');
			}
	}
	return 0;
}
