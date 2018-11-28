#include<cstdio>
#include<iostream>
#include<queue>
#include<map>
#include<set>
#include<algorithm>
#include<cmath>
#include<cstdlib>
using namespace std;

#define inf 1023456789
#define linf 1023456789123456789ll
#define pii pair<int,int>
#define pipii pair<int, pii >
#define pll pair<long long,long long>
#define vint vector<int>
#define vvint vector<vint >
#define ll long long
#define pdd pair<double, double>

#define DEBUG
#ifdef DEBUG
#define db(x) cerr << #x << " = " << x << endl
#else
#define db(x)
#endif

const int dX[4] = {0,1,0,-1}, dY[4] = {-1,0,1,0};

int main()
{
	int t;
	scanf("%d",&t);
	for(int test=0; test<t; test++)
	{
		int r,c;
		char s[142];
		scanf("%d %d",&r,&c);
		vvint smer(r, vint(c,-1));
		vint v_stlpci(c,0), v_riadku(r,0);
		for(int y=0; y<r; y++)
		{
			scanf(" %s",s);
			for(int x=0; x<c; x++)
			{
				if(s[x] != '.')
				{
					if(s[x] == '^')smer[y][x] = 0;
					if(s[x] == '>')smer[y][x] = 1;
					if(s[x] == 'v')smer[y][x] = 2;
					if(s[x] == '<')smer[y][x] = 3;
					v_riadku[y]++;
					v_stlpci[x]++;
				}
			}
		}
		bool possible = 1;
		int res = 0;
		for(int y=0; y<r; y++)
		{
			for(int x=0; x<c; x++)
			{
				if(smer[y][x] != -1)
				{
					if(v_riadku[y]==1 && v_stlpci[x]==1)
					{
						possible = 0;
						break;
					}
					int px=x, py=y;
					while(1)
					{
						px += dX[smer[y][x]];
						py += dY[smer[y][x]];
						if(px < 0 || px >= c || py < 0 || py >= r)
						{
							res++;
							break;
						}
						if(smer[py][px] != -1)break;
					}
				}
			}
		}
		
		printf("Case #%d: ",test+1);
		if(!possible)
		{
			printf("IMPOSSIBLE\n");
		}
		else
		{
			printf("%d\n",res);
		}
	}
	return 0;
}