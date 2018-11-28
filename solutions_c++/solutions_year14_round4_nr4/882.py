#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>
#include <map>
#include <vector>

using namespace std;

int N, Svr;
char Str[10][12];
int Worst, Cnt;
int nTrie[5];
int Next[5][100][26];

void Insert(int ID, char* S)
{
	int C = 0;
	for (char* t = S; *t; t ++)
	{
		if (Next[ID][C][*t - 'A'] == -1)
		{
			Next[ID][C][*t - 'A'] = nTrie[ID];
			memset(Next[ID][nTrie[ID]], -1, sizeof(Next[ID][nTrie[ID]]));
			nTrie[ID] ++;
		}
		C = Next[ID][C][*t - 'A'];
	}
}

int Usage[10];
set < long long > Set;

void DFS(int V)
{
	if (V == N)
	{
		int Cur = 0;
		for (int i = 0; i < Svr; i ++)
			if (nTrie[i] > 1)
				Cur += nTrie[i];
		if (Cur > Worst)
		{
			Worst = Cur;
			Cnt = 1;
		}
		else if (Cur == Worst)
		{
			Cnt ++;
		}
		return;
	}
	int TmpnTrie;
	int TmpNext[100][26];
	for (int i = 0; i < Svr; i ++)
	{
		Usage[V] = i;
		TmpnTrie = nTrie[i];
		memcpy(TmpNext, Next[i], sizeof(TmpNext));
		Insert(i, Str[V]);
		DFS(V + 1);
		nTrie[i] = TmpnTrie;
		memcpy(Next[i], TmpNext, sizeof(TmpNext));
	}
}

void Work()
{
	Worst = 0;
	Cnt = 0;
	scanf("%d%d", &N, &Svr);
	for (int i = 0; i < N; i ++)
		scanf("%s", &Str[i]);
	for (int i = 0; i < Svr; i ++)
	{
		nTrie[i] = 1;
		memset(Next[i][0], -1, sizeof(Next[i][0]));
	}
	DFS(0);
	printf("%d %d\n", Worst, Cnt);
	fflush(stdout);
}

int main()
{
	freopen("D-small.in", "r", stdin);
	freopen("D-small.out", "w", stdout);
    int Cases;
    scanf("%d", &Cases);
    for (int Case = 1; Case <= Cases; Case ++)
    {
		printf("Case #%d: ", Case);
		Work();
    }
    return 0;
}