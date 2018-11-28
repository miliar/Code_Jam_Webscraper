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

const int N = 1e3 + 7;
int t, n;

map<ll, int> ans;
int pow10[10];
int f(ll a)
{
	if (a == 0)
		return 0;
	if (ans[a] != 0)
		return ans[a];
	
	int ret = f(a / 10);
	
	for (int i = 1; i <= 9; i++)
	{
		int amn = a / pow10[i] % 10;
		if (amn > 0)
		{
			for (int j = 1; j < i - 1; j++)
				ret = min(ret, f(a - pow10[i] + pow10[j] + pow10[i - j]));
		}
	}
	return ans[a] = (ret + 1);
}

void run()
{
	pow10[1] = 1;
	for (int i = 2; i < 10; i++)
		pow10[i] = pow10[i - 1] * 10;
	
	scanf("%d", &t);
	for (int ct = 1; ct <= t; ct++)
	{
		dbg(ct)
		scanf("%d", &n);
		ll a = 0;
		for (int i = 0; i < n; i++)
		{
			int p;
			scanf("%d", &p);
			a += pow10[p];
		}
		//dbg(a)
		
		printf("Case #%d: %d\n", ct, f(a));
	}
}
/*
if (debug) printf(": %d \n", );
if (debug) printf("\n");
*/