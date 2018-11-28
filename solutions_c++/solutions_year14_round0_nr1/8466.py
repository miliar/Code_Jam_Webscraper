#include <string>
#include <vector>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <cassert>
#include <cstdio>
#include <stdio.h>
#include <string.h>
#include <ctime>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <stack>
#include <ctime>
using namespace std;
typedef long long LL;
typedef long double LD;
#define FOR(k,a,b) for(int k(a); k < (b); ++k)
#define FORD(k,a,b) for(int k(b-1); k >= (a); --k)
#define REP(k,a) for(int k=0; k < (a); ++k)
#define ABS(a) ((a)>0?(a):-(a))

typedef vector<int> VI;
typedef vector<LL> VL;
typedef vector<string> VS;

int main()
{
#ifdef HOME
	freopen ("A-small-attempt0.in","r",stdin);
	freopen ("A-small-attempt0.out","w",stdout);
#endif 
	int T;
	double C,F,X;
	scanf("%d",&T);
	int t1[4][4];
	int t2[4][4];
	FOR(tc,1,T+1)
	{
		int r1,r2;
		scanf("%d",&r1);
		REP(i,4) REP(j,4)
		{
			scanf("%d",&t1[i][j]);
		}
		scanf("%d",&r2);
		REP(i,4) REP(j,4)
		{
			scanf("%d",&t2[i][j]);
		}
		--r1,--r2;
		set<int> s;
		vector<int> v;
		REP(j,4)
		{
			s.insert(t1[r1][j]);
		}
		REP(j,4)
		{
			if(s.count(t2[r2][j]))
			{
				v.push_back(t2[r2][j]);
			}
		}
		if(v.size()==1)
		{
			printf("Case #%d: %d\n",tc,v[0]);
		}
		else if(v.empty())
		{
			printf("Case #%d: Volunteer cheated!\n",tc);
		}
		else
		{
			printf("Case #%d: Bad magician!\n",tc);
		}
	}
	return 0;

}

