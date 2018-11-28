# include <stdio.h>
# include <string.h>


int n, m, max_node, num;
char s[10][15];
char adds[10][15];
int vis[10];

int trie[110][26], tcc;


int insert(char str[])
{
	int rtn = 0;
	int idx = 0;
	for (int i = 0; str[i]; i++)
	{
		if (trie[idx][str[i]-'A'] == 0)
		{
			trie[idx][str[i]-'A'] = idx = tcc++;
			rtn++;
		}
		else idx = trie[idx][str[i]-'A'];
	}
	return rtn;
}


int calc(int cc)
{
	int rtn = 1;
	if (cc == 0) return 0;
	memset (trie, 0, sizeof(trie));
	tcc = 1;
	for (int i = 0; i < cc; i++)
		rtn += insert(adds[i]);
	return rtn;
}


int gao()
{
	int i, j, rtn = 0;
	for (i = 0; i < 4; i++)
	{
		int cc = 0;
		for (j = 0; j < m; j++) if (vis[j] == i)
			strcpy(adds[cc], s[j]), cc++;
		rtn += calc(cc);
	}
	return rtn;
}


void dfs(int cur)
{
	int i;
	if (cur == m)
	{
		int buff = gao();
		if (buff > max_node)
			max_node = buff, num = 1;
		else if (buff == max_node)
		{
		/*	for (i = 0; i <m; i++)
				printf ("%4d", vis[i]);
			printf ("\n");
		*/
			num++;
		}
		return ;
	}
	for (i = 0; i < n; i++)
	{
		vis[cur] = i;
		dfs(cur+1);
	}
}


int main ()
{
	int T, cas, i;
	freopen ("D-small-attempt0.in", "r", stdin);
	freopen ("dout.txt", "w", stdout);
	scanf ("%d", &T);
	for (cas = 1 ; cas <= T; cas++)
	{
		scanf ("%d%d", &m, &n);
		for (i = 0; i < m; i++)
			scanf ("%s", s[i]);
		max_node = 0;
		num = 0;
		dfs (0);
		printf ("Case #%d: %d %d\n", cas, max_node, num);
	}
	return 0;
}
