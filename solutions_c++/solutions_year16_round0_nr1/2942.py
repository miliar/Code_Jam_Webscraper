#include <iostream>
#include <cstdio>

using namespace std;

int t, n, rez;
int dig[15], cate;

void solve()
{
	cate = 0;
	for (int i = 0; i <= 9; i++) dig[i] = 0;
	for (int i = 1; cate != 10; i++){
		int nr = i*n;
		rez = nr;
        while (nr) {
			if (dig[nr%10]==0) cate++;
            dig[nr%10] = 1;
            nr /= 10;
        }
	}
}

int main()
{
    freopen("sheep.in", "r", stdin);
    freopen("sheep.out", "w", stdout);

	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
        scanf("%d", &n);
        printf("Case #%d: ", i);
        if (n == 0)
			printf("INSOMNIA\n");
		else {
			solve();
			printf("%d\n", rez);
		}
	}

    return 0;
}
