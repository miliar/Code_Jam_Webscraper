#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>

#define TEST_NUM "d1"
//#define DEBUGGGGGGGGGGGGGGGGGGGGGGGGGG
char inname[100];
char outname[100];

char arr[30][30];
bool sta[30][30];
int s[30];
bool chk[30];
int n, r;

bool g(int c)
{
	if(c==n)
		return 1;
	bool u = 0;
	int x, i;
	x = s[c];
	for(i = 0; i<n; i++)
	{
		if(!chk[i] && sta[x][i])
		{
			u = 1;
			chk[i] = 1;
			if(!g(c+1))
				return 0;
			chk[i] = 0;
		}
	}
	if(!u)
		return 0;
	return 1;
}

void f(int c)
{
	if(c==n*n)
	{
		bool u = 1;
		int i, j, t;
		for(i = 0; i<n; i++)
			s[i] = i;
		do
		{
			memset(chk, 0, sizeof(chk));
			if(!g(0))
			{
				u = 0;
				break;
			}
		}
		while(std::next_permutation(s, s+n));

		if(u)
		{
			t = 0;
			for(i = 0; i<n; i++)
			{
				for(j = 0; j<n; j++)
				{
					if(arr[i][j]=='1' && !sta[i][j])
						return;
					if(arr[i][j]=='0' && sta[i][j])
						t++;
				}
			}
			r = std::min(r, t);
		}
		return;
	}
	sta[c/n][c%n] = 0;
	f(c+1);
	sta[c/n][c%n] = 1;
	f(c+1);
}

void process()
{
	int i, j;
	scanf("%d", &n);
	for(i = 0; i<n; i++)
		scanf("%s", arr[i]);

	r = 1000;
	f(0);
	printf("%d", r);
}

void pre_process()
{

}

int main()
{
#ifndef DEBUGGGGGGGGGGGGGGGGGGGGGGGGGG
	sprintf(inname, "%s.in", TEST_NUM);
	sprintf(outname, "%s.out", TEST_NUM);
#endif
	freopen(inname, "r", stdin);
	freopen(outname, "w", stdout);
	int tn, ti;
	scanf("%d", &tn);
	pre_process();
	for(ti = 1; ti<=tn; ti++)
	{
		printf("Case #%d: ", ti);
		process();
		printf("\n");
	}
	return 0;
}