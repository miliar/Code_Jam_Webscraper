#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;
int main()
{
	int t;
	FILE* in = fopen("A-large.in", "r");
	fscanf(in, "%d", &t);
	FILE* out = fopen("adasdasds.out", "w");

	for (int i = 0; i < t; i++)
	{

		int size = 0;
		fscanf(in, "%d", &size);

		char str[1111];
		fscanf(in, "%s", str);
		int ret = 0;
		int cur = str[0] - '0';
		for (int k = 1; k <= size; k++)
		{
			if (cur < k)
			{
				ret += k - cur;
				cur = k + str[k] - '0';
			}

			else
			{
				cur += str[k] - '0';
			}
		}

		fprintf(out, "Case #%d: %d\n", i + 1, ret);
	}

	fclose(in);
	fclose(out);
}