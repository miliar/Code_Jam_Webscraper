//Aleksander Łukasiewicz
#include<cstdio>
using namespace std;

const int MAXN = 20;

int t;
bool pos1[MAXN], pos2[MAXN];
int read[MAXN][MAXN];

int main()
{
	scanf("%d", &t);
	for(int pp=1; pp<=t; pp++)
	{
		int q1,q2;
		scanf("%d", &q1);
		for(int i=1; i<=4; i++)
			for(int j=1; j<=4; j++)
				scanf("%d", &read[i][j]);
		for(int j=1; j<=4; j++)
			pos1[ read[q1][j] ] = true;
		
		scanf("%d", &q2);
		for(int i=1; i<=4; i++)
			for(int j=1; j<=4; j++)
				scanf("%d", &read[i][j]);
		for(int j=1; j<=4; j++)
			pos2[ read[q2][j] ] = true;

		int res = 0, out = -1;
		for(int i=1; i<=16; i++)
			if(pos1[i] && pos2[i])
				res++, out = i;
			
		printf("Case #%d: ", pp);
		if(res==1)
			printf("%d\n", out);
		else if(res==0)
			puts("Volunteer cheated!");
		else
			puts("Bad magician!");

		for(int i=1; i<=16; i++) pos1[i] = pos2[i] = false;
	}


return 0;
}