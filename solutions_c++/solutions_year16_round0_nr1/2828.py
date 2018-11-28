#include <cstdio>

using namespace std;

typedef long long ll;

bool check[10];
int T, count;

void test(ll x)
{
	while (x){
		if (!check[x % 10]){
			check[x % 10] = true;
			count ++;
		}
		x /= 10;
	}
}

int main()
{
	freopen("a1.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; t ++)
	{
		int a;
		scanf("%d", &a);
		for (int i = 0; i < 10; i ++)
			check[i] = false;
		count = 0;
		int l = a;
		if (l < 1000) l = l * 100;
		for (int i = 1; i <= l; i ++)
		{
			test((ll)a * i);
			if (count == 10){
				printf("Case #%d: %lld\n", t, (ll)a * i);
				break;
			}
		}
		if (count < 10)
			printf("Case #%d: INSOMNIA\n", t);
	}
	return 0;
}
