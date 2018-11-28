#include <iostream>
#include <cstring>
#include <cstdio>
#include <cassert>
using namespace std;
const int Maxn = 11, HASH = 10007, STATE = 1000100;
#define L(x) (1 << (x))
struct HashMap
{
	struct Edge
	{
		int s, v, next;
		Edge(){}
		Edge(int s, int v, int next) : s(s), v(v), next(next){}
	}edge[STATE];
	int box[HASH], size;
	void add(int s, int v)
	{
		int hash = s % HASH;
		for (int i = box[hash]; i != -1; i = edge[i].next)
			if (edge[i].s == s)
			{
				edge[i].v = min(edge[i].v, v);
				return;
			}
		edge[size] = Edge(s, v, box[hash]);
		box[hash] = size++;
	}
	void clear()
	{
		size = 0;
		memset(box, -1, sizeof(box));
	}
}dp[2];
int cur, state;
int n, m;
int board[Maxn][Maxn];
void clear(int k)
{
	int v = 7 << 3 * k;
	state ^= state & v;
}
void set(int k, int v)
{
	if (k < 0) return;
	clear(k);
	state |= (v << 3 * k);
}
int code(int k, int state)
{
	int ret = 0;
	for (int i = 2; i >= 0; --i)
	{
		ret <<= 1;
		if (state & L(3 * k + i)) ret |= 1;
	}
	return ret;
}
bool only(int x)
{
	return (x & 3) == 3;
}
bool one(int x)
{
	return only(x) ? 0 : (x & 1);
}
bool two(int x)
{
	return only(x) ? 0 : (x & 2);
}
int find(int k)
{
	int c = code(k, state);
	int dir = 1;
	if (only(c)) return -1;
	if (two(c)) dir = -1;
	for (int i = k, cnt = 0; i <= m && i >= 0; i += dir)
	{
		int cc = code(i, state);
		if ((c & 4) != (cc & 4) || cc == 0 || only(cc)) continue;
		if (c == cc) cnt++;
		else cnt--;
		if (cnt == 0) return i;
	}
	return -1;
}
void shift()
{
	state <<= 3;
	assert(state < L(3 * m + 3) && state >= 0);
}
void bitout(int x)
{
	while (x)
	{
		cout << x % 2;
		x >>= 1;
	}
}
void block(int x, int y)
{
	for (int i = 0; i < dp[cur].size; ++i)
	{
		int s = dp[cur].edge[i].s;
		int v = dp[cur].edge[i].v;
		int left = code(y - 1, s), up = code(y, s);
		if (left || up) continue;
		//cout << x <<" " << y <<" "; bitout(s); cout << " " <<left <<" " << up <<" " << v <<endl;
		state = s;
		if (y == m) shift();
		dp[cur ^ 1].add(state, v);
	}
}
void blank(int x, int y)
{
	for (int i = 0; i < dp[cur].size; ++i)
	{
		int s = dp[cur].edge[i].s;
		int v = dp[cur].edge[i].v;
		int left = code(y - 1, s), up = code(y, s);
		int numleft = 2 + bool(left & 4), numup = 2 + bool(up & 4);
		//cout << x <<" " << y <<" "; bitout(s); cout << " " <<left <<" " << up <<" " << v <<endl;
		if (left && up)
		{
			if (numleft != numup || board[x][y] || (one(left) && two(up)))
				continue; // not same edge or is end point or close
			state = s;
			if (only(left) && only(up))
			{
				clear(y - 1), clear(y);
			}
			else if (only(left) || only(up))
			{
				int match = find(only(left) ? y : y - 1);
				clear(y - 1), clear(y), set(match, 3 | (left & 4));
			}
			else if (left == up)
			{
				int match = find(one(left) ? y : y - 1);
				clear(y - 1), clear(y), set(match, left);
			}
			else
			{
				assert(two(left) && one(up));
				clear(y - 1), clear(y);
			}
			if (y == m) shift();
			dp[cur ^ 1].add(state, v + 1);
		}
		else if (left || up)
		{
			int tmp = left + up;
			if (board[x][y] && numleft + numup - 2 != board[x][y]) continue;
			if (board[x][y])
			{
				state = s;
				if (only(tmp))
				{
					clear(y - 1), clear(y);
				}
				else
				{
					int match = find(left ?  y - 1 : y);
					clear(y - 1), clear(y), set(match, 3 + (board[x][y] == 2 ? 0 : 4));
				}
				if (y == m) shift();
				dp[cur ^ 1].add(state, v + 1);
				continue;
			}
			if (y < m)
			{
				state = s;
				clear(y - 1), set(y, tmp);
				dp[cur ^ 1].add(state, v + 1);
			}
			if(x < n)
			{
				state = s;
				set(y - 1, tmp), clear(y);
				if (y == m) shift();
				dp[cur ^ 1].add(state, v + 1);
			}
		}
		else
		{
			if (board[x][y] == 0) // may not go
			{
				state = s;
				clear(y - 1), clear(y);
				if (y == m) shift();
				dp[cur ^ 1].add(state, v);
				if (y < m && x < n) // new circle
				{
					state = s;
					set(y - 1, 1), set(y, 2);
					dp[cur ^ 1].add(state, v + 1);
					state = s;
					set(y - 1, 5), set(y, 6);
					dp[cur ^ 1].add(state, v + 1);
				}
			}
			else
			{
				if (y < m)
				{
					state = s;
					clear(y - 1), set(y, 3 + (board[x][y] == 2 ? 0 : 4));
					dp[cur ^ 1].add(state, v + 1);
				}
				if (x < n)
				{
					state = s;
					set(y - 1, 3 + (board[x][y] == 2 ? 0 : 4)), clear(y);
					if (y == m) shift();
					dp[cur ^ 1].add(state, v + 1);
				}
			}

		}
	}
}
void chatou()
{
	cur = state = 0;
	dp[cur].clear();
	dp[cur].add(0, 0);
	for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= m; ++j)
		{
			dp[cur ^ 1].clear();
			if (board[i][j] == 1) block(i, j);
			else blank(i, j);
			cur ^= 1;
		}
	if (dp[cur].size == 0) printf("0\n");
	else
	{
		assert(dp[cur].size == 1);
		printf("%d\n", dp[cur].edge[0].v - 2);
	}
}


int main()
{
	//freopen("in.txt", "r", stdin);
	while (scanf("%d%d", &n, &m) != EOF)
	{
		if (n == 0) break;
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= m; ++j)
				scanf("%d", &board[i][j]);
		chatou();
	}
	return 0;
}