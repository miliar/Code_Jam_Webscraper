#include <stdio.h>
#include <math.h>
#include <string.h>

using namespace std;

#define MAX 1000000
#define INF 0xFFFFFF

int N;
char s[MAX];


int main (int argc, char *argv[])
{
	FILE *ifp, *ofp;

	ifp = fopen(argv[1], "r");
	ofp = fopen(argv[2], "w");

	if (ifp == NULL || ofp == NULL)
		return 0;

	int T;
	fscanf (ifp, "%d\n", &T);

	for (int i = 1; i <= T; i++)
	{
		int m;
		int prevj = 0;
		int cntn = 0;
		unsigned long long count = 0;
		fscanf (ifp, "%s %d\n", s, &N);

		int len = strlen (s);
		int j = 0;
		while(j <= len - N)
		{
			int flag = 1;
			int k = 0;
			while (j < len)
			{
				if ((s[j] == 'a'
					|| s[j] == 'e'
					|| s[j] == 'i'
					|| s[j] == 'o'
					|| s[j] == 'u'))
				{
					k = 0;
				}
				else
					k++;
				if (k == N)
					break;
				j++;
			}
			if (k == N)
			{
				while (prevj <= j - N + 1)
				{
					count += len - j;
					prevj++;
				}
				j = j - N + 1;
			}

			j++;
		}

		fprintf (ofp, "Case #%d: %u\n", i, count);
	}
	fclose(ifp);
	fclose(ofp);
	return 0;
}