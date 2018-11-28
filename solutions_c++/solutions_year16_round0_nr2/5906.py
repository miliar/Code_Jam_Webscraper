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
#include <fstream>
using namespace std;

#define FOR(i, a, b) for(int i=(a);i<(b);i++)
#define RFOR(i, b, a) for(int i=(b)-1;i>=(a);--i)
#define FILL(A,value) memset(A,value,sizeof(A))

#define ALL(V) V.begin(), V.end()
#define SZ(V) (int)V.size()
#define PB push_back
#define MP make_pair
#define INF 1000000000
const double PI = acos(-1.0);

typedef long long ll;
typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;

bool numbersUsed[10];

bool needMoreIterations()
{
	return numbersUsed[0] & numbersUsed[1]& numbersUsed[2]& numbersUsed[3]& numbersUsed[4]& numbersUsed[5]& numbersUsed[6]& numbersUsed[7]& numbersUsed[8]& numbersUsed[9];
}

void markUsedNumbers(ll x)
{
	while(x)
	{
		numbersUsed[x%10]=1;
		x/=10;
	}
}

void solve()
{
	string s;
	cin >> s;
	s.push_back('+');
	int cnt = 0;
	for (int i = 1; i < s.size(); ++i)
	{
		if (s[i] != s[i-1])++cnt;
	}
	cout << cnt << endl;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; ++test)
	{
		cerr << "Test: " << test << endl;
		printf("Case #%d: ", test);
		solve();
	}
	return 0;
}