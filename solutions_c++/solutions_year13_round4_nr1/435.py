#pragma warning(disable:4786)
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<cmath>
#include<stack>
using namespace std;

#define MEM(a, b) memset(a, (b), sizeof(a))
#define CLR(a) memset(a, 0, sizeof(a))
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define ABS(X) ( (X) > 0 ? (X) : ( -(X) ) )
#define S(X) ( (X) * (X) )
#define SZ(V) (int )V.size()
#define FORN(i, n) for(i = 0; i < n; i++)
#define FORAB(i, a, b) for(i = a; i <= b; i++)

typedef pair<int,int> PII;
typedef pair<double, double> PDD;

//typedef int LL;
//typedef __int64 LL;

struct Ticket
{
	int enter, exit, people;

	Ticket(int a, int c)
	{
		enter = a;

		people = c;
	}

	Ticket(){}
};

bool operator<(Ticket A, Ticket B)
{
	return A.enter < B.enter;
}

priority_queue<Ticket> Q;
vector<PII> V;

int COST(int a, int b, int c)
{
	return a*(c-b-1)*(c-b)/2;
}

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
//	freopen("A-large.in", "r", stdin);
//	freopen("A-large.out", "w", stdout);

	int T, N, M;
	int ks, st, en, i;
	int global, now, later;
	int people;
	int sz;
	Ticket u;

	scanf("%d", &T);
	for(ks = 1; ks <= T; ks++)
	{
		scanf("%d %d", &N, &M);

		while(!Q.empty()) Q.pop();
		V.clear();

		global = 0;
		for(i = 1; i <= M; i++)
		{
			scanf("%d %d %d", &st, &en, &people);

			global += people*(en - st - 1)*(en - st)/2;

			V.push_back( PII(st, -people) );
			V.push_back( PII(en, +people) );
		}

		later = 0;
		sort(V.begin(), V.end());

		sz = V.size();
		for(i = 0; i < sz; i++)
		{
			if(V[i].second < 0) //entering
			{
				Q.push(Ticket(V[i].first, -V[i].second));
			}
			else
			{
				now = V[i].second;
				while(now)
				{
					u = Q.top();
					Q.pop();

					if(u.people <= now)
					{
						now -= u.people;
						later += COST(u.people, u.enter, V[i].first);
					}
					else
					{
						u.people -= now;
						later += COST(now, u.enter, V[i].first);
						now = 0;
						Q.push(u);
					}
				}
			}
		}

		int ans = later - global;

		printf("Case #%d: %d\n", ks, ans);


	}


	return 0;
}
