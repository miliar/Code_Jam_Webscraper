#include <stdio.h>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <fstream>
#include <stdlib.h>
#include <math.h>
#include <cmath>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <limits.h>
#include <time.h>
#include <bitset>
#include <list>

#define EPS 1e-11
#define PI M_PI
#define LL long long
#define INF 2123123123
#define MP(a,b) make_pair(a,b)
#define PB(a) push_back(a)
#define swap(a,b) a=a^b, b=a^b, a=a^b;
#define OPENR(a) freopen(a,"r",stdin)
#define OPENW(a) freopen(a,"w",stdout)

int x4[4] = { 0, 0,-1, 1};
int y4[4] = {-1, 1, 0, 0};
int x8[8] = {-1,-1,-1, 0, 0, 1, 1, 1};
int y8[8] = {-1, 0, 1,-1, 1,-1, 0, 1};
int xhorse[8] = {1,2,1,2,-1,-2,-1,-2};
int yhorse[8] = {2,1,-2,-1,2,1,-2,-1};

using namespace std;

struct f{
	bool operator () (int a,int b)
	{
		return a>b;
	}
};

int t,cap,n,s;
multiset<int,f> ms;
int ans;

void reset()
{
	ms.clear();
	ans = 0;
}

int main()
{
	OPENR("A-large.in");
	OPENW("A-large.out");
	
	scanf("%d",&t);
	
	for (int tc=1;tc<=t;tc++)
	{
		reset();
		
		scanf("%d %d",&n,&cap);
		for (int i=0;i<n;i++)
		{
			scanf("%d",&s);
			ms.insert(s);
		}
		
		while(!ms.empty())
		{
			ans++;
			int a = *ms.begin();
			ms.erase(ms.begin());
			
			if (ms.empty()) break;
			
			int b = cap - a;
			
			multiset<int>::iterator it = ms.end();
			it--;
			if (*it <= b)
			{
				it = ms.lower_bound(b);
				int c = *it;	
				ms.erase(it);
			}
		}
		
		printf("Case #%d: %d\n",tc,ans);
	}
	
 	return 0;
}



