#include<cstdio>
#include<cstring>
#include<algorithm>

enum
{
	MAX = 1010
};

int pow_tree[MAX];
int tab[MAX];
int ids[MAX];

bool comp(int a, int b)
{
	return tab[a] < tab[b];
}

void pow_write(int x)
{
	pow_tree[x]++;
	if(x+(x&(-x)) < MAX)
		pow_write(x+(x&(-x)));
}

int pow_read(int x)
{
	int res = pow_tree[x];
	if(x && x-(x&(-x)))
		res += pow_read(x-(x&(-x)));
	return res;
}

int main()
{
	int T; scanf("%d", &T);
	for(int ii = 0; ii < T; ii++)
	{
		int N; scanf("%d", &N);
		memset(pow_tree,0,sizeof(pow_tree));
		for(int i = 0; i < N; i++)
		{
			scanf("%d", tab+i);
			ids[i] = i;
		}
		std::sort(ids,ids+N,comp);
		int res = 0;
		for(int i = 0; i < N; i++)
		{
			int left = ids[i]-pow_read(ids[i]);
			int right = N-ids[i]-1-(pow_read(N)-pow_read(ids[i]+1));
			res += (left<right)?left:right;
			pow_write(ids[i]+1);
		}
		printf("Case #%d: %d\n",ii+1,res);
	}

	return 0;
}
