
#include <cstring>
#include <cstdio>

#define min(a,b) (((a)<(b))?(a):(b))
#define max(a,b) (((a)>(b))?(a):(b))

const int textSize = 100 * 1024;
const int maxAudience = 1024;
char text [textSize];

void standing_ovation ()
{

	memset(text, 0, textSize);

	fread(text, 1024, 100, stdin);

	int tcNum;
	sscanf(text, "%d", &tcNum);

	int cursor = 0;

	int audience [maxAudience];

	while (text[cursor] != '\n')
	{
		++cursor;
	}
	++cursor;

	for (int tc = 0; tc < tcNum; ++tc)
	{
		int smax;
		sscanf(text+cursor, "%d", &smax);

		while (text[cursor] != ' ')
		{
			++cursor;
		}
		++cursor;

		for (int j = 0; j < smax; ++j)
		{
			audience[j] = text[cursor++]-'0';
		}
		while (text[cursor] != '\n')
		{
			++cursor;
		}
		++cursor;

		int toBeInvited = 0;
		int sum = 0;
		for (int j = 0; j < smax+1; ++j)
		{
			//printf ("j=%d, toBeInvited=%d, sum=%d\n",j, toBeInvited, sum);
			toBeInvited += max(j-(sum+toBeInvited),0);
			sum += audience[j];
		}

		printf ("Case #%d: %d\n", tc+1, toBeInvited);
	}
}
