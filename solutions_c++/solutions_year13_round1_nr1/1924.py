# include <iostream>
# include <cstring>
# include <cstdlib>
# include <cstdio>
using namespace std;

unsigned long long Solve (unsigned long long r, unsigned long long t)
{
	unsigned long long Counter = 0, R1 = r, R2 = r + 1, Diff;
	while (true)
	{
		Diff = (R2 * R2) - (R1 * R1);
		if (Diff <= t)
		{
			Counter++;
			R1 += 2;
			R2 = R1 + 1;
			t -= Diff;
		}
		else break;
	}
	return Counter;
}

int main()
{
	freopen ("Input.txt", "r", stdin);
	freopen ("Scratch.txt","w", stdout);
	unsigned long long Total, r, t;
	scanf ("%llu", &Total);
	for (int i = 1; i <= Total; i++)
	{
		scanf ("%llu%llu", &r, &t);
		printf ("Case #%d: %llu\n", i, Solve (r, t));
	}
}
