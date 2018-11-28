#include <cstdio>
int main()
{
	freopen( "input.in", "r", stdin);
	freopen( "output.txt", "w", stdout);
	int run;
	for( int test=scanf("%d", &run); test<=run; ++test)
	{
		int row1[5], row2[5];
		scanf("%d", row1);
		for( int i=1; i<=4; ++i)
		{
			for( int j=1; j<=4; ++j)
			{
				int tmp;
				scanf("%d", &tmp);
				if( i == row1[0] )row1[j] = tmp;
			}
		}
		scanf("%d", row2);
		for( int i=1; i<=4; ++i)
		{
			for( int j=1; j<=4; ++j)
			{
				int tmp;
				scanf("%d", &tmp);
				if( i == row2[0] )row2[j] = tmp;
			}
		}
		int match =0, match_num;
		for( int i=1; i<=4; ++i)
			for( int j=1; j<=4; ++j)
				if(row1[i]==row2[j])
				{
					++match;
					match_num = row1[i];
				}
		printf("Case #%d: ", test);
		if( match == 0)		puts("Volunteer cheated!");
		else if( match == 1)printf("%d\n", match_num);
		else 				puts("Bad magician!");
	}
}
