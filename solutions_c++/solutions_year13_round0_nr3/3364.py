#include <stdio.h>
#include <string.h>
#include <math.h>

bool fs[10000010];
bool sq[10000010];

bool pld(long long int x)
{
	char nm[20];
	sprintf(nm, "%I64d", x);
	int i, len = strlen(nm), len2 = len/2;
	for(i = 0 ; i < len2 ; i++)
	{
		if(nm[i] != nm[len-i-1]) return false;
	}
	return true;
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small.txt", "w", stdout);
	int T;
	int cs = 1;
	scanf("%d", &T);
	while(T--)
	{
		long long int A, B;
		scanf("%I64d%I64d", &A, &B);
		long long int sqa = sqrt(A), sqb = sqrt(B);
		long long int i;
		int ans = 0;
		if(sqa*sqa != A) sqa++;
		for(i = sqa ; i <= sqb ; i++)
		{
			if(pld(i) == true)
			{
				if(pld(i*i) == true) ans++;
			}
		}
		//printf("%I64d %I64d\n", sqa, sqb);

		printf("Case #%d: %d\n", cs, ans);
		cs++;
	}
	return 0;
}
