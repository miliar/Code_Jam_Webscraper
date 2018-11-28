#include<cstdio>
#include<vector>
#include<cmath>

using namespace std;

int T;
long long A, B;
vector <int> tmp;

int pal (long long k)
{
	long long m = k;
	int sz = 0;
	tmp.clear();
	while (m > 0)
	{
		tmp.push_back(m % 10);
		sz++;
		m /= 10;
	}
	for (int i = 0; i < sz; i++)
		if (tmp[i] != tmp[sz - i - 1])
			return 0;
	return 1;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (int g = 0; g < T; g++)
	{
		int ans = 0;
		scanf("%I64d%I64d", &A, &B);
		for (long long i = 0; i <= (int) sqrt(B) + 10; i++)
		{
			if (i * i < A || i * i > B)
				continue;
			if (pal(i) == 1 && pal(i * i) == 1)
				ans++;
		}
		printf("Case #%d: %d\n", g + 1, ans);
	}
	return 0;
}
