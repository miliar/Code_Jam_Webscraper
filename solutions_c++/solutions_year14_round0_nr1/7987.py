#include <cstdio>

int main()
{
	int T, n;
	freopen("magic.in", "r", stdin);	
	freopen("magic.out", "w", stdout);
	scanf("%d", &T);
	for (int Cs=1; Cs<=T; ++Cs)
	{
		int st[2] = {0, 0};
		for (int step=0; step<2; ++step)
		{
			scanf("%d", &n);
			for (int i=1; i<=4; ++i)
				for (int j=0, num; j<4; ++j)
				{
					scanf("%d", &num);
					if (i == n) st[step] += 1 << num;
				}
		}
		int cnt = 0, ans = -1;
		for (int i=1, state=st[0] & st[1]; i<=16; ++i)
			if (state & (1 << i)) ++cnt, ans = i;
		if (!cnt) printf("Case #%d: Volunteer cheated!\n", Cs);
		else if (cnt > 1) printf("Case #%d: Bad magician!\n", Cs);
		else printf("Case #%d: %d\n", Cs, ans);
	}
	fclose(stdin); fclose(stdout);
	return 0;
}

