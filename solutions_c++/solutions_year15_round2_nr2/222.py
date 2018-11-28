#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int nr, nc, na, nb;

int max_half(int nr, int nc)
{
	return (nr * nc + 1) >> 1;
}

int min_sides(int nr, int nc)
{
	int tr = nr >> 1, tc = nc >> 1;
	if (nr & 1)
		tc <<= 1;
	else
		tc = nc;
	if (nc & 1)
		tr <<= 1;
	else
		tr = nr;
	return tr + tc;
}

int solve()
{
	if (na <= nb + 1)
		return 0;
	int res = nr * (nc - 1) + nc * (nr - 1);
	if (nr == 1 || nc == 1)
		return res - 2 * nb;
	int t4 = max_half(nr - 2, nc - 2);
	if (nb <= t4)
		return res - 4 * nb;
	res -= 4 * t4;
	nb -= t4;
	int t3 = min_sides(nr - 2, nc - 2);
	if (nb <= t3)
		return res - 3 * nb;
	res -= 3 * t3;
	nb -= t3;
	if ((nr & 1) && (nc & 1) && (nb <= 4))
		return res + 1 - 3 * nb;
	//printf("t4 = %d, t3 = %d, nb = %d\n", t4, t3, nb);
	return res - 2 * nb;
}

int main()
{
	int itest, ntest;
	scanf("%d", &ntest);
	for (itest = 0; ++itest <= ntest; )
	{
		scanf("%d%d%d", &nr, &nc, &na);
		nb = nr * nc - na;
		printf("Case #%d: %d\n", itest, solve());
	}
	return 0;
}
