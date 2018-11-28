#include <iostream>
#include <cstdio>

using namespace std;

char G[4][10];

const char *solve()
{
}

int main()
{
	FILE *in,*out;
//	char line[1000];
	int T, t;
	int i, j;
	in = fopen("A.in","r");
	out = fopen("A.out","w+");
//	fgets(line,999,in);
//	sscanf(line,"%d",&T);
	fscanf(in,"%d ",&T);
	for(t = 1; t <= T; t++)
	{
		int row, mask, card, answer;
		fscanf(in, "%d ", &row);
		row--;
		mask = 0;
		for(i = 0; i < 16; i++)
		{
			fscanf(in, "%d ", &card);
			if((i>>2) == row)
				mask |= (1<<card);
		}
		fscanf(in, "%d ", &row);
		row--;
		answer = 0;
		for(i = 0; i < 16; i++)
		{
			fscanf(in, "%d ", &card);
			if((i>>2) == row && (mask & (1<<card)))
			{
				if(answer)
					answer = 17;
				else
					answer = card;
			}
		}
		switch(answer)
		{
		case 0:
			fprintf(out, "Case #%d: Volunteer cheated!\n", t);
			break;
		case 17:
			fprintf(out, "Case #%d: Bad magician!\n", t);
			break;
		default:
			fprintf(out, "Case #%d: %d\n", t, answer);
		}
	}
	fclose(in);
	fclose(out);
}
