#include <stdio.h>
#include <string.h>
int tree[10007*4];

int table[9][9]={{0,0,0,0,0,0,0,0,0},{0,1,2,3,4,5,6,7,8}, {0,2,5,4,7,6,1,8,3}, {0,3,8,5,2,7,4,1,6}, {0,4,3,6,5,8,7,2,1}, {0,5,6,7,8,1,2,3,4}, {0,6,1,8,3,2,5,4,7}, {0,7,4,1,6,3,8,5,2}, {0,8,7,2,1,4,3,6,5}};
char str[10005];
int L, X;

void init()
{
	int i;

	char tmp[10005];
	scanf("%d %d\n", &L, &X);
	scanf("%s", tmp);

	for(i=0; i<L*X; i++)
		str[i]=tmp[i%L];
}

void inittree(int index, int a, int b)
{	
	if(a==b)
	{
		tree[index]=str[a-1]-'i'+2;
		return;
	}

	inittree(index*2, a, (a+b)/2);
	inittree(index*2+1, (a+b)/2+1, b);

	tree[index]=table[tree[index*2]][tree[index*2+1]];
}

int query(int index, int a, int b, int i, int j)
{
	if(a==i && b==j)
		return tree[index];

	if(j<=(a+b)/2)
		return query(index*2, a, (a+b)/2, i, j);
	if(i>=(a+b)/2+1)
		return query(index*2+1, (a+b)/2+1, b, i, j);
	else
		return table[query(index*2, a, (a+b)/2, i, (a+b)/2)][query(index*2+1, (a+b)/2+1, b, (a+b)/2+1, j)];
}

bool solve()
{
	int i, j;

	if(tree[1]!=5)
		return 0;

	for(i=1; i<=L*X; i++)
		if(query(1, 1, L*X, 1, i)==2)
			for(j=i+1; j<=L*X; j++)
				if(query(1, 1, L*X, i+1, j)==3 && query(1, 1, L*X, j+1, L*X)==4)
					return 1;
	
	return 0;
}

int main()
{
	int T, i;

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	scanf("%d", &T);

	for(i=1; i<=T; i++)
	{
		init();
		inittree(1, 1, L*X);
		if(solve())
			printf("Case #%d: YES\n", i);
		else
			printf("Case #%d: NO\n", i);
	}
	return 0;
}