#include<iostream>
#include <algorithm>
using namespace std;
int main()
{
	int T;

	errno_t err1;
	FILE *f;
	err1 = freopen_s(&f, "D-large.in", "r", stdin);
	errno_t err2;
	FILE *f2;
	err2 = freopen_s(&f2, "3.txt", "w", stdout);
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		int n;
		cin >> n;
		double A[1100], B[1100];
		for (int j = 0; j < n; j++)
			cin >> A[j];
		for (int j = 0; j < n; j++)
			cin >> B[j];

		sort(A, A + n);
		sort(B, B + n);
		int kb = 0, ke = n - 1;;
		int socwar = 0;
		for (int j = n-1; j >= 0; j--)
		{
			if (A[j]>B[ke])
			{
				kb++;
				socwar++;
			}
			else
				ke--;
		}
		int socwdef = 0;
		kb = 0;
		ke = n - 1;;
		for (int j = 0; j < n; j++)
		{
			if (A[j]>B[kb])
			{
				kb++;
				socwdef++;
			}
			else
				ke--;
		}
		printf("Case #%d: %d %d\n", i + 1, socwdef, socwar);
	}
	return 0;
}