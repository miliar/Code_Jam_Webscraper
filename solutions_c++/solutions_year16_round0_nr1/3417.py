#include <cstdio>
#include <cstdlib>

int when_asleep(int N) {
	bool digits[10] = {false, false, false, false, false, false, false, false, false, false};
	int n = 0,m, d, ndigits = 0;
	do
	{
		n += N;
		m = n;
		while (m) {
			d = m%10;
			m /= 10;
			if (!digits[d])
			{
				digits[d] = true;
				++ndigits;	
			}
		}
	}
	while (ndigits < 10);
	return n;

}

int main(int argc, char const *argv[]) {
	
	int T, N;
	scanf("%d", &T);

	for (int i = 0; i < T; ++i)
	{
		scanf("%d", &N);
		if (N == 0)
			printf("Case #%d: INSOMNIA\n", i+1);
		else
			printf("Case #%d: %d\n", i+1, when_asleep(N));
	}

	return 0;
}