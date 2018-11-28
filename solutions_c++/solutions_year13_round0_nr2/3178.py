#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <sstream>
using namespace std;

#define LL long long
#define LD long double
#define PR pair<int,int>

#define For(i,n) for (i=0; i<int(n); i++)
#define ForR(i,n) for (i=int(n)-1; i>=0; i--)
#define Sz(s) int((s).size())
#define All(s) (s).begin(),(s).end()
#define Fill(s,v) memset(s,v,sizeof(s))
#define pb push_back
#define mp make_pair
#define x first
#define y second

template<typename T> T Abs(T x) { return(x < 0 ? -x : x); }
template<typename T> T Sqr(T x) { return(x*x); }

const int INF = (int)1e9;
const LD EPS = 1e-9;
const LD PI = acos(-1.0);

#define DEBUG 0
#define LIMN 100
#define LIMA 250
struct pqitem
{
    int r;
    int c;
    int prio;

    pqitem() {}
    pqitem(int r, int c, int prio) : r(r), c(c), prio(prio) {}

    bool operator<(const pqitem &b) const
    {
        return prio < b.prio;
    }
};

vector<pqitem> vs;
int rmask[LIMN];
int cmask[LIMN];
int ma[LIMN][LIMN];
int N,M;
bool is_ok()
{
	for(int i=0;i<N*M;i++)
	{
		pqitem cur = vs[i];
		int r=cur.r;
		int c=cur.c;
		if(rmask[r]) continue;
		if(cmask[c]) continue;
		bool temp=true;
		for(int j=0;j<M;j++)
		{
			if(cmask[j]) continue;
			if(ma[r][j]>cur.prio)
			{
				temp=false;
				break;
			}
		}
		if(temp)
		{
			rmask[r]=1;
			continue;
		}
		temp=true;
		for(int j=0;j<N;j++)
		{
			if(rmask[j]) continue;
			if(ma[j][c]>cur.prio)
			{
				temp=false;
				break;
			}
		}
		if(temp)
		{
			cmask[c]=1;
			continue;
		}
		return false;
	}
	return true;
}


int main()
{
	//files
	freopen("in.txt","r",stdin);
		if (!DEBUG)
			freopen("out.txt","w",stdout);
	//vars
	int tt,TT;
	//testcase loop
	scanf("%d",&TT);
		For(tt,TT)
		{
			//init
			vs.clear();
			memset(rmask,0,sizeof(rmask));
			memset(cmask,0,sizeof(cmask));
			printf("Case #%d: ",tt+1);
			scanf("%d%d",&N,&M);
			for(int i=0;i<N;i++)
				for(int j=0;j<M;j++)
				{
					int v;
					scanf("%d",&v);
					ma[i][j]=v;
					vs.push_back(pqitem(i,j,v));
				}
				sort(vs.begin(),vs.end());
			bool res=is_ok();
			if(res)
			{
				printf("YES\n");
			}else
			{
				printf("NO\n");
			}
		}
	return(0);
}