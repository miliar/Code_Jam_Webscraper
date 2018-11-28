//nathanajah's template
//28-11-2012
#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <string.h>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <deque>
#include <map>
#include <ctime>
#define ii pair<int,int>
#define vi vector<int>
#define vii vector<ii>
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define LL long long
#define ULL unsigned LL
#define INF 0x3FFFFFFF
#define INFLL 0x3FFFFFFFFFFFFFFF
#define SZ(a) (int)(a).size()
#define ALL(a) (a).begin(),(a).end()
#ifdef DEBUG
	#define debug(...) \
	fprintf(stderr,__VA_ARGS__)
#else
	#define debug(...) 
#endif
using namespace std;

inline string GetString()
{
	char GS[1000005];
	scanf("%s",GS);string ret=GS;
	return ret;
}

inline char getc()
{
	char c=' ';
	while (c==' ' || c=='\t' || c=='\r' || c=='\n')
		c=getchar();
	return c;
}
//ENDOFTEMPLATE

int t,n,m;
int aaaa;
vector <int> akhir[105];
bool sudah[105];
int i,j,k;
int jarakawal;
int jarakakhir;

int cost(int x)
{
	return x*(x-1)/2;
}


int main()
{
	scanf("%d",&t);
	for (aaaa=0;aaaa<t;++aaaa)
	{
		jarakawal=0;
		jarakakhir=0;
		scanf("%d %d",&n,&m);
		for (i=0;i<n;++i)
			akhir[i].clear();
		for (i=0;i<m;++i)
		{
			int o,e,p;
			scanf("%d %d %d",&o,&e,&p);
			--o;--e;
			for (j=0;j<p;++j)
			{
				akhir[o].pb(e);
				jarakawal+=cost(e-o);
			}
		}
		for (i=0;i<n;++i)
		{
			for (j=0;j<SZ(akhir[i]);++j)
			{
				int now=i+1;
				int nowend=akhir[i][j];
				while (now<=nowend)
				{
					for (k=0;k<SZ(akhir[now]);++k)
					{
						if (akhir[now][k]>nowend)
						{
							int tmp=akhir[now][k];
							akhir[now][k]=nowend;
							nowend=tmp;
						}
					}
					++now;
				}
				akhir[i][j]=nowend;
				jarakakhir+=cost(nowend-i);
			}
		}
		printf("Case #%d: %d\n",aaaa+1,jarakakhir-jarakawal);
	}
}
