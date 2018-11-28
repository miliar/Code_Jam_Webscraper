#define INPUT 1
#define OUTPUT 1
#define DEBUG 1
#define FILE_NAME ""
#define RND 0

#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define ld long double
#define ull unsigned long long
#define uint unsigned int
#define PII pair<int, int>
#define PLL pair<ll, ll >
#define VI vector<int>
#define VVI vector<VI>
#define dbg(x) cerr << #x << " = " << (x) << endl;

const double PI = acos(-1);
const double EPS = 1e-7;
const int MOD = 1e9 + 7;
const int INF = 2e9 + 7;
const ll INFL = 8e18L + 7;
const double INFD = 1e300;

#ifdef LOCAL
	bool debug = 1;
#else
	bool debug = 0;
#endif

void run();

int main(int argc, char** argv)
{
	#ifdef LOCAL
		if (RND)
		{
			int rnd = 0;
			if (argc == 2)
			{
				istringstream ss(argv[1]);
				ss >> rnd;
			}
			rnd += time(0);
			srand(rnd);
			freopen("input.txt", "w", stdout);
		}
		else
		{
			if (INPUT)
				freopen("input.txt", "r", stdin);
			if (OUTPUT)
				freopen("output.txt", "w", stdout);
		}
		if (!DEBUG)
			debug = 0;
	#else
		if (FILE_NAME != "")
		{
			freopen(FILE_NAME".in", "r", stdin);
			freopen(FILE_NAME".out", "w", stdout);
		}
	#endif
	
	run();
	
	#ifdef LOCAL
		fprintf(stderr, "%.3f seconds \n", clock() / (double) CLOCKS_PER_SEC);
	#endif
	
	return 0;
}

const int N = 1e5 + 7;
int t, n, x;

#define Q pair<bool, char>
map<pair<char, char>, Q> m;
Q f(Q a, Q b)
{
	Q res = m[{a.second, b.second}];
	return {a.first ^ b.first ^ res.first, res.second};
}

Q e[N];

void run()
{
	m[{'1', '1'}] = {0, '1'};
	m[{'1', 'i'}] = {0, 'i'};
	m[{'1', 'j'}] = {0, 'j'};
	m[{'1', 'k'}] = {0, 'k'};
	m[{'i', '1'}] = {0, 'i'};
	m[{'i', 'i'}] = {1, '1'};
	m[{'i', 'j'}] = {0, 'k'};
	m[{'i', 'k'}] = {1, 'j'};
	m[{'j', '1'}] = {0, 'j'};
	m[{'j', 'i'}] = {1, 'k'};
	m[{'j', 'j'}] = {1, '1'};
	m[{'j', 'k'}] = {0, 'i'};
	m[{'k', '1'}] = {0, 'k'};
	m[{'k', 'i'}] = {0, 'j'};
	m[{'k', 'j'}] = {1, 'i'};
	m[{'k', 'k'}] = {1, '1'};
	
	Q ni = {0, 'i'};
	Q nj = {0, 'j'};
	Q nk = {0, 'k'};
	
	scanf("%d", &t);
	for (int ct = 1; ct <= t; ct++)
	{
		dbg(ct)
		scanf("%d%d", &n, &x);
		string s = "", s0;
		cin >> s0;
		for (int i = 0; i < x; i++)
			s += s0;
		n *= x;
		
		e[n] = {0, '1'};
		for (int i = n - 1; i >= 0; i--)
			e[i] = f({0, s[i]}, e[i + 1]);
		
		bool ok = 0;
		Q qi = {0, '1'};
		for (int i = 0; i < n; i++)
		{
			qi = f(qi, {0, s[i]});
			Q qj = {0, '1'};
			if (qi == ni)
			for (int j = i + 1; j < n; j++)
			{
				qj = f(qj, {0, s[j]});
				if (qj == nj && e[j + 1] == nk)
					ok = 1;
			}
		}
		
		printf("Case #%d: %s\n", ct, ok ? "YES" : "NO");
	}
}
/*
if (debug) printf(": %d \n", );
if (debug) printf("\n");
*/