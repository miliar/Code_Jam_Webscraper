#include <stdio.h>
#include <string.h>
#include <algorithm>


using namespace std;

const int MAXL = 1000009;
char buf[MAXL];

// vowels (aeiou) 1, consonants 0
int cs[256];

void doet()
{
	int n, len;
	int os = -1, oe = -1;
	long long int sol = 0;
	scanf("%s %d", buf, &n);
	len = strlen(buf);
	
	int rl = 0;
	for (int i = 0; i < len; i++)
	{
		if (cs[buf[i]] == 0)
		{
			rl++;
			if (rl >= n)
			{
				os = i - n + 2;
				oe = i;
				//printf("[%d %d %d]", i, os, oe);
				//sol += os;
			}
		}
		else
		{
			rl = 0;
		}
		if (os > -1) sol += os;
	}

	printf("%lld\n", sol);
}


int main()
{
	cs['a'] = 1; cs['e'] = 1; cs['i'] = 1; cs['o'] = 1; cs['u'] = 1;
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		printf("Case #%d: ", i+1);
		doet();
	}
	return 0;
}

