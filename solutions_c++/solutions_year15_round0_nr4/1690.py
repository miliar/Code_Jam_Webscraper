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
int t;

void run()
{
	scanf("%d", &t);
	for (int ct = 1; ct <= t; ct++)
	{
		int x, n, m;
		scanf("%d%d%d", &x, &n, &m);
		if (n > m)
			swap(n, m);
		
		bool can;
		if (x == 1)
			can = 1;
		if (x == 2)
			can = n * m % 2 == 0;
		if (x == 3)
			can = n > 1 && (n == 3 || m == 3);
		if (x == 4)
			can = n >= 3 && m == 4;
		
		printf("Case #%d: %s\n", ct, can ? "GABRIEL" : "RICHARD");
	}
}
/*
if (debug) printf(": %d \n", );
if (debug) printf("\n");
*/