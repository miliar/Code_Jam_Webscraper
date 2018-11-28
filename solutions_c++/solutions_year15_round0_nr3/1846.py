#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

const int MAXN = 10005;

//define 1,2->i,3->j,4->k

char s[MAXN];
int Pre[MAXN];
int A[MAXN],Fr[MAXN],Bk[MAXN],Sum[MAXN],N,T;

int Case(char c)
{
	if (c == 'i') return 2;
	if (c == 'j') return 3;
	if (c == 'k') return 4;
}

int Get(int a,int b)
{
	if (a == 1) return b;
	if (b == 1) return a;
	if (a == 2) 
	{
		if (b == 2) return -1;
		if (b == 3) return 4;
		if (b == 4) return -3;
	}
	if (a == 3)
	{
		if (b == 2) return -4;
		if (b == 3) return -1;
		if (b == 4) return 2;
	}
	if (a == 4)
	{
		if (b == 2) return 3;
		if (b == 3) return -2;
		if (b == 4) return -1;
	}
}

int Multi(int u,int v)
{
	return (((u < 0) ^ (v < 0)) ? -1 : 1) * Get(abs(u),abs(v));
}

int Rev(int c,int a)
{
	for(int p = -4;p <= 4;p ++)
	if (p)
		if (Multi(a,p) == c) return p;
}

int Get_S(int l,int r)
{
	int cur = 1;
	for(;l <= r;l ++) cur = Multi(cur,A[l]);
	return cur;
}

int main()
{
	//freopen("data.in","r",stdin),freopen("data.out","w",stdout);
	scanf("%d", &T);
	for(int Ti = 1;Ti <= T;Ti ++)
	{
		bool f = 0;
		int X,L;scanf("%d%d", &X, &L);
		scanf("%s", s + 1);
		for(int i = 1;i <= X * L;i ++) 
			A[i] = Case(s[(i - 1) % X + 1]);
		N = X * L;
		Sum[1] = A[1];
		for(int i = 2;i <= N;i ++) Sum[i] = Multi(Sum[i - 1],A[i]);
		int c1 = 0,c2 = 0,cur = 1;
		for(int i = 1;i <= N;i ++)
		{
			cur = Multi(cur,A[i]);
			if (cur == 2) Fr[++ c1] = i;
		}
		cur = 1;
		for(int i = N;i;i --)
		{
			cur = Multi(A[i],cur);
			if (cur == 4) Bk[++ c2] = i;
		}
		for(int i = 1;i <= c1;i ++)
		{
			for(int j = 1;j <= c2;j ++)
			if (Fr[i] + 1 > Bk[j] - 1) break; else
			{
				int l = Fr[i] + 1,r = Bk[j] - 1;
				if (Rev(Sum[r],Sum[l - 1]) == 3) {f = 1;break;}
				//if (Get_S(l,r) == 3) {f = 1;break;}
			}
			if (f) break;
		}
		printf("Case #%d: %s\n",Ti, f ? "YES" : "NO");
	}
	return 0;
}
	