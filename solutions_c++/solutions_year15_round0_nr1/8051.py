#include<cstdio>
#include<iostream>

using namespace std;

int main()
{
	char vstup[1200];
	int t, smax, kamarati, size, zatial;

	scanf("%d", &t);

	for (int f = 0; f < t; ++f)
	{
		scanf("%d %s", &smax, vstup);
		zatial = vstup[0] - '0';
		kamarati = 0;
		size = strlen(vstup);

		for (int i = 1; i < size; ++i)
		{
			if (zatial < i)kamarati += i - zatial, zatial+=(i-zatial);
			zatial += vstup[i] - '0';
		}
		printf("Case #%d: %d\n", f + 1, kamarati);
	}
	return 0;
}