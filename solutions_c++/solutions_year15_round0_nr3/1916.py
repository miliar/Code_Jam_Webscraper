#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

typedef long long LL;

const int Maxl=10010;

int a[Maxl], u1[9], u2[9];
char str[Maxl];

const int p[5][5]={
	{0, 0, 0, 0, 0},
	{0, 1, 2, 3, 4},
	{0, 2, -1, 4, -3},
	{0, 3, -4, -1, 2},
	{0, 4, 3, -2, -1}
};

const int q[5][5]={
	{0, 0, 0, 0, 0},
	{0, 1, -2, -3, -4},
	{0, 2, 1, -4, 3},
	{0, 3, 4, 1, -2},
	{0, 4, -3, 2, 1},
};

int getDigit(char ch)
{
	switch (ch)
	{
		case 'i': return 2;
		case 'j': return 3;
		case 'k': return 4;
	}
}

int mul(int x, int y)
{
	int z=p[abs(x)][abs(y)];
	if (x<0 && y>0 || x>0 && y<0) z=-z;
	return z;
}

int divide(int x, int y)
{
	int z=q[abs(x)][abs(y)];
	if (x<0 && y>0 || x>0 && y<0) z=-z;
	return z;
}

int main()
{
	int T, l;
	LL x;
	scanf("%d", &T);
	for (int tt=1; tt<=T; ++tt)
	{
		scanf("%d%lld%s", &l, &x, str);
		int s=1;
		for (int i=0; i<l; ++i)
		{
			a[i]=getDigit(str[i]);
			s=mul(s, a[i]);
		}
		printf("Case #%d: ", tt);
		if (!(s==-1 && (x&1)==1 || abs(s)!=1 && (x&3)==2))
		{
			puts("NO");
			continue;
		}

		int s0=s;
		s=1;
		memset(u1, 60, sizeof u1);
		u1[s+4]=0;
		for (int i=1; i<x && i<8; ++i)
		{
			s=mul(s, s0);
			u1[s+4]=min(u1[s+4], i*l);
		}
		memset(u2, 60, sizeof u2);
		for (int i=-4; i<=4; ++i)
			if (i)
			{
				s=i;
				for (int j=0; j<l; ++j)
				{
					s=mul(s, a[j]);
					u2[s+4]=min(u2[s+4], u1[i+4]+j+1);
				}
			}
		LL pos_i=u2[6];

		s=-1;
		memset(u1, 60, sizeof u1);
		u1[s+4]=0;
		for (int i=1; i<x && i<8; ++i)
		{
			s=divide(s, s0);
			u1[s+4]=min(u1[s+4], i*l);
		}
		memset(u2, 60, sizeof u2);
		for (int i=-4; i<=4; ++i)
			if (i)
			{
				s=i;
				for (int j=0; j<l; ++j)
				{
					s=divide(s, a[l-1-j]);
					u2[s+4]=min(u2[s+4], u1[i+4]+j+1);
				}
			}
		LL pos_k=u2[8]<u2[4]? x*l-u2[8]:-1;

		//printf("%lld %lld\n", pos_i, pos_k);
		puts(pos_i<pos_k? "YES":"NO");
	}
	return 0;
}

