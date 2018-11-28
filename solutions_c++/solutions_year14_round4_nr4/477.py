#include<cstdio>
#include<cstring>

char str[10][20];
char cor[10];
bool touched[5];

struct node
{
	node* next[30];
	node()
	{
		for(int i = 0; i < 30; i++)
			next[i] = 0;
	}
} trees[5];

int clear(node* n)
{
	for(int i = 0; i < 30; i++)
		if(n->next[i])
		{
			clear(n->next[i]);
			delete n->next[i];
			n->next[i] = 0;
		}
}

int main()
{
	int T; scanf("%d", &T);
	for(int ii = 0; ii < T; ii++)
	{
		int M, N; scanf("%d%d", &M, &N);
		for(int i = 0; i < M; i++)
			scanf(" %s", str[i]);
		memset(cor,0,sizeof(cor));
		int worst = 0;
		int total = 0;
		while(true)
		{
			for(int i = 0; i < N; i++)
				clear(&trees[i]);
			int score = 0;
			memset(touched,0,sizeof(touched));

			for(int i = 0; i < M; i++)
			{
				node* pnt = &trees[cor[i]];
				if(!touched[cor[i]])
				{
					touched[cor[i]]=1;
					score++;
				}
				for(int j = 0; str[i][j]; j++)
				{
					if(!pnt->next[str[i][j]-'A'])
					{
						score++;
						pnt->next[str[i][j]-'A'] = new node;
					}
					pnt = pnt->next[str[i][j]-'A'];
				}
			}
			if(score == worst) total++;
			if(score>worst) { worst = score; total = 1; }
			bool good = 0;
			for(int i = 0; i < M; i++)
			{
				if(cor[i]<N-1)
				{
					cor[i]++;
					good = 1;
					break;
				}
				else
					cor[i] = 0;
			}
			if(!good) break;
		}
		printf("Case #%d: %d %d\n",ii+1,worst,total);
	}

	return 0;
}
