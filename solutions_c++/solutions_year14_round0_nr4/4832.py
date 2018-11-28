#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstdlib>
#include <iomanip>
#include <ctime>
#include <utility>
#include <fstream>

#define x first
#define y second
#define mp make_pair
#define pb push_back
#define sqr(x) (x)*(x)
#define _with_file
#define TASK ""
#define forn(i, n) for(int i = 0; i < (int)n; ++i)

#define getb(x,y) (x&(1<<y))
#define setb(x,y) (1|(1<<y))
#define unsetb(x,y) (x&(~(1<<y)))

void quit(); 

using namespace std;

typedef long long i64;
typedef unsigned long long u64;
typedef long double ld;
typedef pair <int, int> PII;
typedef pair <i64, i64> PII64;
typedef pair <ld, ld> PLL;

const ld EPS = 1e-12;
double __t;

int T,n;
int ans1,ans2,uk;
double a[1010],b[1010];

void get()
{
	ans1=0,uk=0;
	for(int i=0; i<n && uk<n; i++)
	{
		while(uk<n && a[uk]<b[i])
			uk++;
		if(uk<n)
		{
			ans1++;
			uk++;
		}
	}
}

bool u1[1010],u2[1010];
void dfs(int nh, int pnt)
{
	if(nh==n)
	{
		ans2=max(ans2,pnt);
		return;
	}

	forn(i,n)
	{
		if(!u1[i])
		{
			u1[i]=1;
			double mintowin=9.0;
			int ind=-1;
			forn(j,n)
				if(!u2[j] && b[j]>a[i] && b[j]<mintowin)
				{
					mintowin=b[j];
					ind=j;
				}
			if(mintowin<2.0)
			{
				u2[ind]=1;
				dfs(nh+1,pnt);
				u2[ind]=0;
			}
			else
			{
				forn(j,n)
					if(!u2[j] && b[j]<mintowin)
					{
						mintowin=b[j];
						ind=j;
					}
				u2[ind]=1;
				dfs(nh+1,pnt+1);
				u2[ind]=0;
			}
			u1[i]=0;
		}
	}
}

int main()
{
    #ifdef local
        __t = clock();
        #ifndef _with_files
            freopen("z.in", "rt", stdin);
            freopen("z.out", "wt", stdout);
        #endif
    #endif
    #ifdef _with_files
        freopen(TASK".in", "rt", stdin);
        freopen(TASK".out", "wt", stdout);
    #endif
                                                           
    cin >>T;
    forn(I,T)
    {
    	cerr <<I<<endl;
    	cin >>n;
    	forn(i,n)
    		cin >>a[i];
    	forn(i,n)
    		cin >>b[i];

    	sort(a,a+n);
    	sort(b,b+n);
    	get();

    	ans2=0;
    	memset(u1,0,sizeof(u1));
    	memset(u2,0,sizeof(u2));
    	dfs(0,0);
    	cout <<"Case #"<<I+1<<": "<<ans1<<' '<<ans2<<endl;
    }
    quit();
}

void quit()
{
    #ifdef LOCAL
        cerr << "\n\nTOTAL TIME: "<< (clock() - __t)/1000.0 << " s\n";
    #endif
    exit(0);        
}