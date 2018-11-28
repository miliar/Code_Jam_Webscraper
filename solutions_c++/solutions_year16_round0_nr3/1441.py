#include<cstdio>
int co[33], n;

void print()
{
	for (int i = n - 1; i >= 0; i--) printf("%d", co[i]);
	printf(" 3 2 5 2 7 2 3 2 11\n");
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T, J;
	long long c;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%d %d", &n, &J);
		co[0] = 1;
		co[n - 1] = 1;
		printf("Case #%d:\n", t);
		print();
		J--;
		for (int i = 1; i < n - 1; i += 2)
		{
			co[i] = 1;
			for (int j = 2; j < n - 1; j += 2)
			{
				co[j] = 1;
				print();
				J--;
				if (!J) break;
				co[j] = 0;
			}
			co[i] = 0;
			if (!J) break;
		}
		if (!J) continue;
		for (int i = 1; i < n - 1; i += 2)
		{
			co[i] = 1;
			for (int j = 2; j < n - 1; j += 2)
			{
				co[j] = 1;
				for (int k = i + 2; k < n - 1; k += 2)
				{
					co[k] = 1;
					for (int l = j + 2; l < n - 1; l += 2)
					{
						co[l] = 1;
						print();
						J--;
						if (!J) break;
						co[l] = 0;
						if (!J) break;
					}
					co[k] = 0;
					if (!J) break;
				}
				co[j] = 0;
				if (!J) break;
			}
			co[i] = 0;
			if (!J) break;
		}
	}
}