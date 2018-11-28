#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <utility>
#include <cstdlib>
#include <string>
#include <sstream>
#include <gmpxx.h>

using namespace std;

#define VS vector<string>
#define VI vector<int>
#define VVI vector< VI >
#define pb push_back
#define mp make_pair
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FORC(it,kont) for(__typeof((kont).begin()) it = (kont).begin(); it!=(kont).end(); ++it)
#define MOD 1000002013
char buff[20000];
struct edge
	{
	long long x1, x2;
	long long p;
	edge() { x1 = x2 = p = 0;}
	edge(long long a, long long b, long long c)
		{x1 = a; x2 = b; p = c;}
	};
long long N, M;
vector< edge > E;
long long cost( long long a, long long b )
	{
	return ((b-a)*(N+N+1-(b-a))/2)%MOD;
	}

vector< pair<long long, long long> > stack;
vector< pair<long long, long long> > event;
int main()
    {
    int T;
    gets(buff);
    sscanf(buff,"%d",&T);

    FOR( tp, 0, T )
        {
	event.clear();
	stack.clear();
	long long cost1 = 0;
        long long sol = 0;        
	cin >> N >> M;
	E.resize(M);
	FOR( i, 0, M )
		{
		long long a1, a2, a3;
		cin >> a1 >> a2 >> a3;
		E[i] = edge(a1,a2,a3);
		cost1 = (cost1 + a3*cost(a1,a2))%MOD;
		}
	FOR(i,0,M)
		{ event.pb(mp(E[i].x1,-E[i].p)); event.pb(mp(E[i].x2,E[i].p));}
	sort(event.begin(),event.end());
	//FOR(i,0,event.size()) cout << event[i].first << " " << event[i].second << endl;
	long long cost2 = 0;
	FOR( i, 0, event.size() )
		{
		if( event[i].second < 0 )
			{
			stack.pb(mp( event[i].first, -event[i].second));
			}
		else 
			{
			int tmp = event[i].second;
			while( stack.back().second <= tmp )
				{
				//%cout << tmp;
				cost2 = (cost2 + stack.back().second*cost(stack.back().first,event[i].first))%MOD;
				tmp -= stack.back().second;
				stack.pop_back();
				//cout << i << " " << cost2 << endl;
				}
			//cout << tmp;
			cost2 = (cost2 + tmp*cost(stack.back().first,event[i].first)) % MOD;
			stack.back().second -= tmp;
			//cout << cost(stack.back().first,event[i].first) << endl;
			//cout << i << " " << cost2 << endl;
			}
		}
	//cout << cost1 << " " << cost2 << endl;
	if( cost1 > cost2 )
		sol = cost1 - cost2;
	else 
		sol = (MOD +cost1 - cost2)%MOD;
        printf("Case #%d: %lld\n",tp+1,sol);
        }
    return 0;
    }
