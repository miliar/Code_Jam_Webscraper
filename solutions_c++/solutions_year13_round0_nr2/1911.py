/*#include <cstdio>
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm> 
#include <sysutil>
*/
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
using namespace std;

#define forn(x,y) for(int x=0;x<y;x++)
#define mp make_pair 
#define pb pushback
#define inf 0x7f7f7f7f

typedef long long i64;

int tests;
int n,m,test;
int a[115][115];
bool u[115][115];
int lower=inf,x,y;

bool check(int x, int y)
{
	//cerr << "check:\ncurh:";
	int curh=a[x][y];
	//cerr << curh << endl;
	u[x][y]=1;
	bool ok1=1,ok2=1;
	for(int i=0;i<n;i++)
	{
		if (u[i][y]||a[i][y]==curh) 
		{
			
		}   else ok1=0;
	}
	if (ok1)
		forn(i,n)
			u[i][y]=1;
	
	for(int i=0;i<m;i++)
	{
		if (u[x][i]||a[x][i]==curh) 
		{
			
		}   else ok2=0;
		
	}
	if (ok2)
		forn(i,m)
	        u[x][i]=1;

	return (ok1||ok2);
}

void getmin()
{
	lower=inf;
	forn(i,n)
		forn(j,m)
		{
			if((!u[i][j])&&(a[i][j]<lower))
			{
				lower=a[i][j];
				x=i; 
				y=j;
			}
		}
}

int main()
{
	freopen("z.in","rt",stdin);
	freopen("z.out","wt",stdout);
	cin >> tests;

	forn(test,tests)
	{
		memset(u, 0, sizeof(u));
		memset(a, 0, sizeof(a));
		lower=inf;

		scanf("%d%d",&n,&m);

		forn(i,n)
			forn(j,m)
			    {
					scanf("%d",&a[i][j]);
					if (a[i][j]<lower)
					{
						lower=a[i][j];
						x=i; 
						y=j;
					}
				}
		bool allok=1;
		while(lower!=inf)
		{
			/*
			cerr << x << " " << y<< endl;
			forn(i,n)
			{
				forn(j,m)
					cerr << u[i][j];
				cerr << endl;
			}	
			*/
			
			if (!check(x,y))
			//bool b=!check(x,y);
			//cout << b << endl; cout << endl;;
			//if (b)
			{
				allok=0;
				//cerr << "[via check]\n";
				break;
			}
			getmin();		
		}
		if (allok)
			printf("Case #%d: YES\n",test+1);
		else 
			printf("Case #%d: NO\n",test+1);

	}
	return 0;
}
