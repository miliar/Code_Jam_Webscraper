/*
    Author: Zhouxing Shi
    Created on May3, 2015
*/
#include <bits/stdc++.h>
#define rep(i, a, b) for (int i = (a); i <= (b); ++i)
#define drep(i, a, b) for (int i = (a); i >= (b); --i)
#define REP(i, a, b) for (int i = (a); i < (b); ++i)
#define pb(x) push_back(x)
#define mp(x, y) (make_pair(x, y))
#define clr(x) memset(x, 0, sizeof(x))
#define xx first
#define yy second

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
const int inf = ~0U >> 1;
const ll INF = ~0ULL >> 1;

//***************************

namespace subtask1
{
	
	int v[100][100], best, N, M, K;
	
	void dfs(int x, int y, int c) 
	{
		if (x == N + 1) 
		{
			if (c != K) return;
			int cost = 0;
			rep(i, 1, N) 
				rep(j, 1, M) 
					if (v[i][j])
					{
						if (v[i + 1][j]) cost++;
						if (v[i][j + 1]) cost++;
					}
			best = min(best, cost);
			return;
		}
		v[x][y] = 1;
		if (y == M) dfs(x + 1, 1, c + 1);
		else dfs(x, y + 1, c + 1);
		v[x][y] = 0;
		if (y == M) dfs(x + 1, 1, c);
		else dfs(x, y + 1, c);
	}
	
	int solve()
	{
		best = inf;
		scanf("%d%d%d", &N, &M, &K);
		dfs(1, 1, 0);
		return best;
	}
	
	int main()
	{
		int cases;
		scanf("%d", &cases);
		rep(_, 1, cases) 
			printf("Case #%d: %d\n", _, solve());
	}
}


namespace subtask2
{
	
	map<int, int> C[20000];
	set<pair<int, pii> > S;
	
	int N, M, K;
	
	const int dx[] = {1, -1, 0, 0};
	const int dy[] = {0, 0, 1, -1};
	
	void place(int x, int y)
	{
		S.erase(mp(C[x][y], mp(x, y)));
		C[x][y] = -1;
		REP(k, 0, 4)
		{
			int nx = x + dx[k];
			int ny = y + dy[k];
			if (nx > 0 && ny > 0 && nx <= N && ny <= M && C[nx][ny] != -1)
			{
				S.erase(mp(C[nx][ny], mp(nx, ny)));
				++C[nx][ny];
				S.insert(mp(C[nx][ny], mp(nx, ny)));
			}
		}
	}
	
	int solve()
	{
		int best = inf;
		scanf("%d%d%d", &N, &M, &K); int _K = K;
		if (!N || !M || !K) return 0;
		

		rep(i, 1, N) C[i].clear(); S.clear();		
		
		int cost = 0;
		place(1, 1); --K;
		rep(i, 1, N) rep(j, 1, M) 
			if (C[i][j] != -1) 
				S.insert(mp(C[i][j], mp(i, j)));
		while (K)
		{
			int x = S.begin()->yy.xx, y = S.begin()->yy.yy;
			cost += S.begin()->xx;
			place(x, y);
			--K;
		}
		best = cost;
		
		if (N >= 2) 
		{
			cost = 0;
			rep(i, 1, N) C[i].clear(); S.clear();
			K = _K;
			place(2, 1); --K;
			rep(i, 1, N) rep(j, 1, M) 
				if (C[i][j] != -1) 
					S.insert(mp(C[i][j], mp(i, j)));
			while (K)
			{
				int x = S.begin()->yy.xx, y = S.begin()->yy.yy;
				cost += S.begin()->xx;
				place(x, y);
				--K;
			}
			best = min(best, cost);
		}
		
		
		if (M >= 2) 
		{
			cost = 0;
			rep(i, 1, N) C[i].clear(); S.clear();
			K = _K;
			place(1, 2); --K;
			rep(i, 1, N) rep(j, 1, M) 
				if (C[i][j] != -1) 
					S.insert(mp(C[i][j], mp(i, j)));
			while (K)
			{
				int x = S.begin()->yy.xx, y = S.begin()->yy.yy;
				cost += S.begin()->xx;
				place(x, y);
				--K;
			}
			best = min(best, cost);		
		}
		
		
		return best;
	}
	
	int main()
	{
		int cases;
		scanf("%d", &cases);
		rep(_, 1, cases) 
			printf("Case #%d: %d\n", _, solve()),cerr<<_<<endl;
	}
}



int main()
{
	subtask2::main();
	return 0;
}


