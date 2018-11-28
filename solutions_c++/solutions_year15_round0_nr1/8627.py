#include<stdio.h>
#include<string.h>

int sol[101];

int main(int argc, char** argv)
{
	int n, m;
	int s, v;
	int ret;
	FILE *fin, *fout;

	freopen_s(&fin, "input.txt", "r", stdin);
	freopen_s(&fout, "output.txt", "w", stdout);

	scanf_s("%d", &n);
	for (int i = 0; i < n; ++i)
	{
		char audiences[1002] = { 0 };
		scanf_s("%d", &m);
		scanf_s("%s", audiences, sizeof(audiences)); // maximum_shyest level

		ret = 0;
		s = 0;      // currently_standing_people
		for (int j = 0; j <= m; ++j)
		{
			v = audiences[j] - '0';
			if (j >= s)  // more people to stand
			{
				ret = ret + (j - s);
				s = s + (j - s);
			}
			s += v;
		}
		sol[i] = ret;
	}
	for (int i = 0; i < n; ++i)
		printf("Case #%d: %d\n", (i + 1), sol[i]);
	return 0;
}
