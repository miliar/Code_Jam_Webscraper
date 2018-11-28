#include <bits/stdc++.h>
using namespace std;

bool vit[10];
bool ok(int n)
{
	memset(vit, false, sizeof(vit));
	for(int i = 1; i <= 200; i++)
	{
		int k = i*n;
		while(k)
		{
			vit[k%10] = true;
			k /= 10;
		}
	}
	for(int i = 0; i < 10; i++)
		if(!vit[i]) return false;
	return true;
}

int main()
{
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);
	int t, n, k, h, tn = 1;
	scanf("%d", &t);
	while(t--)
	{
		scanf("%d", &n);
		if(!n)
		{
			printf("Case #%d: INSOMNIA\n", tn++);
			continue;
		}
		k = 0;
		memset(vit, false, sizeof(vit));
		while(true)
		{
			k += n;
			h = k;
			while(h)
			{
				vit[h % 10] = true;
				h /= 10;
			}
			for(h = 0; h < 10; h++)
				if(!vit[h]) break;
			if(h == 10)
			{
				printf("Case #%d: %d\n", tn++, k);
				break;
			}
		}
	}
	return 0;
}
