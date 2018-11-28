#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/stack:16777216")
#include <string>
#include <vector>
#include <map>
#include <list>
#include <iterator>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility> 
#include <time.h>
#include <functional>
using namespace std;
 
#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
#define RFOR(i, b, a) for(int i = (b) - 1; i >= (a); --i)
#define REP(i, N) FOR(i, 0, N)
#define RREP(i, N) RFOR(i, N, 0)
#define FILL(A,value) memset(A,value,sizeof(A))
 
#define ALL(V) V.begin(), V.end()
#define SZ(V) (int)V.size()
#define PB push_back
#define MP make_pair
const double Pi = acos(-1.0);

typedef long long Int;
typedef unsigned long long UINT;
typedef vector <int> VI;
typedef pair <int, int> PII;

const int INF = 1000000000;

struct state
{
	int next[26];
	state()
	{
		FILL(next, -1);
	}
};

struct Trie
{
	state a[100];

	int n;

	Trie(): n(0) {}

	void add(string s)
	{
		if (n == 0)
		{
			n = 1;
		}
		int cur = 0;
		FOR(i,0,s.size())
		{
			if (a[cur].next[s[i] - 'A'] != -1)
			{
				cur = a[cur].next[s[i] - 'A'];
			}
			else
			{
				a[cur].next[s[i] - 'A'] = n;
				cur = n;
				++n;
			}
		}
	}
};

bool nx(vector<int> & a, int m)
{
	FOR(i,0,a.size())
	{
		if (a[i] < m - 1)
		{
			++a[i];
			return 1;
		}
		else a[i] = 0;
	}
	return 0;
}

int main()
{
	freopen("in.txt" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);
	int t;
	cin >> t;   
	FOR(tt,0,t)
	{
		printf("Case #%d: " , tt + 1);
		int n,m;
		cin >> n >> m;
		vector<string> S(n);
		FOR(i,0,n)
			cin >> S[i];

		vector<int> a(n,0);

		int res = 0;
		int cnt = 0;

		do
		{
			Trie A[5];
			FOR(i,0,a.size())
			{
				A[a[i]].add(S[i]);
			}
			int r = 0;
			FOR(i,0,5)
				r += A[i].n;
			if (r > res)
			{
				res = r;
				cnt = 1;
			}
			else
			{
				if (r == res)
				{
					++cnt;
				}
			}
		}while (nx(a,m));

		cout << res << ' ' << cnt << endl;

	}

    return 0;
}