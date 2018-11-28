#include <bits/stdc++.h>
#define ii pair<int, int>
using namespace std;
int f[26];
char s[1005];
char sp[20][10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int fin[10];
int con(char x)
{
	return x-'A';
}
int main()
{
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int tt;
	scanf("%d", &tt);
	for(int qq = 1; qq<= tt; qq++)
	{
		//Solution starts//
		memset(f, 0, sizeof f);
		memset(fin, 0, sizeof fin);
		scanf("%s", s);
		int n = strlen(s);
		for(int i = 0; i< n; i++)
		{
			f[con(s[i])]++;
		}
		fin[0] = f[con('Z')];
		for(int i = 0; i< 4; i++)
		{
			f[con(sp[0][i])] -= fin[0];
		}
		fin[2] = f[con('W')];
		for(int i = 0; i< 3; i++)
		{
			f[con(sp[2][i])] -= fin[2];
		}
		//printf("%d\n", f[con('O')]);
		fin[4] = f[con('U')];
		for(int i = 0; i< 4; i++)
		{
			f[con(sp[4][i])] -= fin[4];
		}
		fin[6] = f[con('X')];
		for(int i = 0; i< 3; i++)
		{
			f[con(sp[6][i])] -= fin[6];
		}
		fin[8] = f[con('G')];
		for(int i = 0; i< 5; i++)
		{
			f[con(sp[8][i])] -= fin[8];
		}
		fin[1] = f[con('O')];
		for(int i = 0; i< 3; i++)
		{
			f[con(sp[1][i])] -= fin[1];
		}
		fin[5] = f[con('F')];
		for(int i = 0; i< 4; i++)
		{
			f[con(sp[5][i])] -= fin[5];
		}
		fin[7] = f[con('S')];
		for(int i = 0; i< 4; i++)
		{
			f[con(sp[7][i])] -= fin[7];
		}
		fin[9] = f[con('I')];
		for(int i = 0; i< 4; i++)
		{
			f[con(sp[9][i])] -= fin[9];
		}
		fin[3] = f[con('T')];
		//Solution ends, output//
		printf("Case #%d: ", qq);
		for(int i = 0; i< 10; i++)
		{
			for(int j= 0; j< fin[i]; j++)
			{
				printf("%d", i);
			}
		}
		printf("\n");
	}
}