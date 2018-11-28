#include <iostream>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <string>
#include <list>
#include <vector>
#include <string.h>
#include <stack>
#include <algorithm>
#include <math.h>

using namespace std;

int M, N, mx, mxCnt;
string S[100];

void setbit(long long &bMask, int pos, long long val)
{
	long long msk = 3ll;
	msk <<= (pos*2);
	msk = ~msk;
	bMask &= msk;
	bMask |= (val << (pos * 2) );
}

int getbit(long long bMask, int pos)
{
	long long msk = 3ll;
	msk <<= (pos * 2);
	bMask &= msk;
	bMask >>= (pos * 2);
	return bMask;
}

vector <int> groups[4];

struct Node
{
	Node *children[30];
	char val;
	Node(char c)
	{
		val = c;
		for (int i = 0; i < 30; i++)
			children[i] = NULL;
	}
	Node *addChild(char c, int &nw)
	{
		if (children[c - 'A'] == NULL)
		{
			children[c - 'A'] = new Node(c);
			nw++;
		}
		return children[c - 'A'];
	}
	~Node()
	{
		for (auto x:children)
		if (x != NULL)
			delete x;
		
	}
};

int makeTrie(int grp)
{
	Node *root = new Node(' '), *cur;
	int cnt = 1;
	int i, j, k;
	for (auto x : groups[grp])
	{
		cur = root;
		for (i = 0; i < S[x].length(); i++)
			cur = cur->addChild(S[x][i], cnt);
	}
	delete root;
	return cnt;
}

int calc(long long bMask)
{
	int occ[4];
	for (int i = 0; i < N; i++)
	{
		occ[i] = 0;
		groups[i].clear();
	}
	for (int i = 0; i < M; i++)
	{
		int cur = getbit(bMask, i);
		occ[cur]++;
		groups[cur].push_back(i);
	}
	int ans = 0;
	for (int i = 0; i < N; i++)
	{
		if (occ[i] == 0)
			return -1;
		ans += makeTrie(i);
	}
	return ans;
}

void solve(int cur, long long bMask)
{
	if (cur == M)
	{
		int cnt = calc(bMask);
		if (cnt == -1)
			return;
		if (cnt > mx)
		{
			mx = cnt;
			mxCnt = 1;
		}
		else if (cnt == mx)
			mxCnt++;
		return;
	}
	for (int i = 0; i < N; i++)
	{
		setbit(bMask, cur, i);
		solve(cur + 1, bMask);
	}
}

int main()
{
	int T, i, j;
	cin >> T;
	for (int tt = 1; tt <= T; tt++)
	{
		cerr << tt << endl;
		cin >> M >> N;
		mx = 0;
		for (i = 0; i < M; i++)
			cin >> S[i];
		solve(0, 0);
		cout << "Case #" << tt << ": " << mx << " " << mxCnt << endl;
	}
}