#include <bits/stdc++.h>
using namespace std;

map <string, int> mem;
int tot;

int getID(string s)
{
	//cout << "[" << s << "]" << endl;
	if(mem.count(s))
		return mem[s];
	tot ++;
	mem[s] = tot;
	return tot;
}

int n;
vector <int> words[1001];

vector <int> getTokeys()
{
	vector <int> ret;
	string s;
	char c;
	while(c = cin.get())
	{
		if(c == 0)
			break;
		if(c == '\n')
			break;
		if(c == ' ')
		{
			ret.push_back(getID(s));
			s = "";
		}
		else
			s += c;
	}
	if(s != "")
		ret.push_back(getID(s));
	return ret;
}

int x[1000001];

#define MAXN 200001

int maxint = ~0U>>1;
int flow;
int pi[MAXN+1], v[MAXN+1];
int S, T;

struct etype
{
	int t, c;
	etype* next;
	etype* pair;
	etype(){next=0;}
	etype(int _t, int _c, etype* _n){t=_t, c=_c, next=_n;}
}*e[MAXN+1], *eb[MAXN+1], *Pe, *Pool;

int aug(int w, int lim)
{
	int t;
	v[w] = 1;
	if(w == T)
	{
		flow += lim;
		return lim;
	}
	for(etype *& i=e[w]; i; i = i->next)
		if(i->c && !v[i->t] && pi[w] == pi[i->t] + 1)
			if(t = aug(i->t, min(lim, i->c)))
				return i->c -= t, i->pair->c += t, t;
	return 0;
}

bool fix()
{
	int t = maxint;
	for(int i = S; i <= T; i++)
		if(v[i])
		{
			for(etype *j = eb[i]; j; j = j->next)
				if(j->c && !v[j->t])
					t = min(t, pi[j->t] + 1 - pi[i]);
		}
	if(t == maxint)
		return 0;

	for(int i = S; i <= T; i++)
		if(v[i])
			e[i] = eb[i], pi[i] += t;
	return 1;
}

void addedge(int s, int t, int c)
{
	//cout << s << " -> " << t << " = " << c << endl;
	++Pe;
	Pe->t = t, Pe->c = c, Pe->next = e[s];
	e[s] = Pe;
	++Pe;
	Pe->t = s, Pe->c = 0, Pe->next = e[t];
	e[t] = Pe;
	e[s]->pair=e[t];
	e[t]->pair=e[s];
}

void prepare()
{
	if(Pool == NULL)
		Pool = new etype[10000001];
	Pe = Pool;
	memset(e, 0, sizeof(e));
}

int MaxFlow()
{
	flow = 0;
	memcpy(eb, e, sizeof(e));
	memset(pi, 0, sizeof(pi));
	do
	{
		do
		memset(v, 0, sizeof(v));
		while(aug(S, maxint));
	}
	while(fix());
	return flow;
}

/*  Note
	1. Set maxNodes here: #define MAXN 200001
	2. Set maxEdges here: Pool = new etype[1000001];
	3. S must be the min id, T must be the max id
*/

/*  Eaxmple
	prepare();
	S = 1, T = 2;
	addedge(1, 2, 3);
	cout << MaxFlow() << endl;
*/

int gW1(int x)
{
	return 1 + x;
}

int gW2(int x)
{
	return 1 + tot + x;
}

int gS1(int x)
{
	return 1 + tot + tot + x;
}

int gS2(int x)
{
	return 1 + tot + tot + n + x;
}

void solve()
{
	tot = 0;
	mem.clear();
	cin >> n;
	char c;
	c = cin.get();
	for(int i = 1; i <= n; i++)
	{
		words[i] = getTokeys();
		//cout << words[i].size() << endl;
	}
	memset(x, 0, sizeof(x));
	for(int i = 0; i < words[1].size(); i++)
		x[words[1][i]] |= 1;
	for(int i = 0; i < words[2].size(); i++)
		x[words[2][i]] |= 2;
	
	S = 1;
	T = 1 + tot + tot + n + n + 1;
	prepare();

	int ans = 0;
	for(int i = 1; i <= tot; i++)
	{
		if(x[i] != 1 && x[i] != 3)
			addedge(S, gW1(i), 1);
		else
			ans ++;

		if(x[i] != 2 && x[i] != 3)
			addedge(gW2(i), T, 1);
		else
			ans ++;

		addedge(gW1(i), gW2(i), 10000000);
	}

	int BIG = 10000;

	for(int i = 3; i <= n; i++)
	{
		addedge(S, gS1(i), BIG);
		addedge(gS1(i), gS2(i), 10000000);
		addedge(gS2(i), T, BIG);
	}

	

	for(int i = 3; i <= n; i++)
		for(int j = 0; j < words[i].size(); j++)
		{
			addedge(gW1(words[i][j]), gS2(i), 10000000);
			addedge(gS1(i), gW2(words[i][j]), 10000000);
		}
	int f = MaxFlow();
	//cout << f << endl;
	ans += f;
	ans -= tot;

	cout << ans % BIG << endl;

	
}

int MAIN()
{
	int TestCase;
	cin >> TestCase;
	for(int caseID = 1; caseID <= TestCase; caseID ++)
	{
		cout << "Case #" << caseID << ": ";
		solve();
	}
	return 0;
}

int main()
{
	int start = clock();
	#ifdef LOCAL_TEST
		freopen("in.txt", "r", stdin);
		freopen("out.txt", "w", stdout);
	#endif
	ios :: sync_with_stdio(false);
	cout << fixed << setprecision(16);
	int ret = MAIN();
	#ifdef LOCAL_TEST
		cout << "[Finished in " << clock() - start << " ms]" << endl;
	#endif
	return ret;
}
