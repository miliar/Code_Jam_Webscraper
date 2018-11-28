#define _CRT_SECURE_NO_WARNINGS

#include <iostream>

using namespace std;

int getLast(int n)
{
	bool* is_d = new bool[10];
	memset(is_d, false, 10);

	int found = 0;

	for (int mult = 1; mult <= 100; ++mult)
	{
		int tmp = mult*n;
		while (tmp > 0)
		{
			if (is_d[tmp % 10] == false) {
				is_d[tmp % 10] = true;
				found++;
			}
			tmp /= 10;
		}

		if (found == 10)
			return mult*n;
	}
	return -1;
}

int main()
{

	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int* a = new int[1000005];
	a[0] = -1;

	for (int i = 1; i <= 1000000; ++i)
		a[i] = getLast(i);

	int Tcount;
	cin >> Tcount;

	int n; 
	for (int Tcase = 1; Tcase <= Tcount; ++Tcase) {
		scanf("%d", &n);

		if(a[n]==-1)
			printf("Case #%d: INSOMNIA\n", Tcase);
		else
			printf("Case #%d: %d\n", Tcase, a[n]);
	}
	return 0;
}
