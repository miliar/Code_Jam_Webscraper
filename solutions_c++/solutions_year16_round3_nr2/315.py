#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <complex>
#include <iterator>
#include <set>
#include <bitset>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>

using namespace std;
typedef vector<int> VI;
typedef long long LL;
typedef vector<VI> VVI;
typedef vector<LL> VLL;
typedef vector<double> VD;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define VAR(v, n) typeof(n) v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define PB push_back
#define ST first
#define ND second
#define MP make_pair
#define PF push_front

int n,t;
LL b,m;
LL mak;
LL ile;
LL poz,ful;
LL pot[100];
int graf[100][100];
int dfs(int x)
{
	if(x==b)
	return 1;
	int wyn=0;
	FOR(i,x+1,b)
	{
		if(graf[x][i])
		wyn+=dfs(i);
	}
	return wyn;
}
int main()
{
	scanf("%d", &t);
	FOR(tt,1,t)
	{
		printf("Case #%d: ",tt);
		scanf("%lld %lld", &b, &m);
		FOR(i,0,55)
		{
			pot[i]=0;
		}
		FOR(i,0,b)
		{
			FOR(j,0,b)
			{
				graf[i][j]=0;
			}
		}
		mak=((1LL)<<(b-2));
		if(m>mak)
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		else
		{
			printf("POSSIBLE\n");
			
			if(m==mak)
			{
				FOR(i,1,b)
				{
					FOR(j,1,b)
					{
						(j>i) ? printf("1") : printf("0");
						//(j>i) ? graf[i][j]=1 : graf[i][j]=0;
					}
					printf("\n");
				}
			}
			else
			{
				//cerr<<"kejs !="<<endl;
				ile=b;
				mak=((1LL)<<(ile-2));
				while(mak>m)
				{
					ile--;
					mak=((1LL)<<(ile-2));
				}
				//cerr<<"# ile=="<<ile<<" ful=="<<ful<<" poz=="<<poz<<endl;
				//poz=m-mak;
				poz=m;
				ful=(b-ile);
				pot[b-1]=1;
				FORD(i,b-2,ful+1)
				{
					pot[i]=pot[i+1]*2;
				}
				FOR(i,1,b)
				{
					FOR(j,1,b)
					{
						if(i>ful){
						(j>i) ? printf("1") : printf("0");
						(j>i) ? graf[i][j]=1 : graf[i][j]=0;
						}
						else if(i==1)
						{
							if(pot[j]!=0)
							{
								if(pot[j]<=poz)
								{
									printf("1");
									//graf[i][j]=1;
									poz-=pot[j];
								}
								else
								{
									printf("0");
								}
							}
							else
							printf("0");	
						}	
						else
						printf("0");
					}
					printf("\n");
				}		
			}
		//	if(dfs(1)!=m)
			//{
				//cerr<<"cos nie tak w tescie "<<tt<<endl;
		//	}
		}
	}

}






