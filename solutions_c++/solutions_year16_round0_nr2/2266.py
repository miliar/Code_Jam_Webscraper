
#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:167772160000")
#include <iostream>
#include <fstream>
#include <cstdio>
#include <stdio.h>
#include <cstdlib>
#include <stdlib.h>
#include <string>
#include <list>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <vector>
#include <iomanip>
#include <queue>
#include <deque>
#include <set>
#include <stack>
#include <sstream>
#include <assert.h>
#include <functional>
#include <climits>
#include <cstring>
typedef long long ll;
typedef std::pair<ll, ll> pll;
typedef std::pair<int, int> pii;
typedef std::pair<double, double> pdd;
#define ALL(x)           (x).begin(), (x).end()
#define forn(N)          for(int i = 0; i<(int)N; i++)
#define fornj(N)         for(int j = 0; j<(int)N; j++)
#define fornk(N)         for(int k = 0; k<(int)N; k++)
#define forn1(N)          for(int i = 1; i<=(int)N; i++)
#define fornj1(N)         for(int j = 1; j<=(int)N; j++)
#define fornk1(N)         for(int k = 1; k<=(int)N; k++)
#define PI 3.1415926535897932384626433
#define LINF (1LL<<60)
#define INF (1<<30)
#define v vector
#define File "Patterns"
#define ll long long
#define print(n) printf("%d ", (n));
#define printll(n) printf("%I64d", (n));
#define printline() printf("\n");
#define read(n) scanf("%d", &n);
#define read2(n, m) scanf("%d%d", &n, &m);
#define readll(n) scanf("%I64d", &n);
#define mp make_pair
#define x first
#define y second
#define double long double
using namespace std;




int main()
{
#if defined(_DEBUG) || defined(_RELEASE)
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#else
	//freopen(File".in", "r", stdin); freopen(File".out", "w", stdout);
#endif
	int T; cin >> T;
	fornk1(T) {
		string s; cin >> s;
		s += "+";
		int answer = 0;
		forn(s.length() - 1)answer += (s[i] != s[i + 1]);
		cout << "Case #" << k << ": " << answer << endl;

	}
	return 0;

}

