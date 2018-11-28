/*
ID: dixtosa1
PROG: milk2
LANG: C++11
*/
#pragma comment(linker, "/STACK:16777216")
#include <iostream>
#include <fstream>
#include <cstdio>
#include <stdio.h>
#include <cstdlib>
#include <stdlib.h>
#include <string>
//#include <string.h>
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
#include <functional> //std::greater<int>
//#include <tuple>

//#include "Biginteger.cpp"
//#include "sqrt.cpp"
//#include "tree.cpp"
//#include "funcs.cpp"

typedef long long ll;
typedef std::pair<ll, ll> pii;
#define ALL(x)           (x).begin(), (x).end()
#define forn(N)          for(long long i = 0; i < (long long)N; i++)
#define fornj(N)         for(long long j = 0; j < (long long)N; j++)
#define fornk(N)         for(long long k = 0; k < (long long)N; k++)
#define foreach(c,itr)   for(auto itr=(c).begin();itr!=(c).end();itr++)
#define PI 3.1415926535897932384626433
#define LINF (1LL<<60)
#define INF (1<<30)
#define awesome vector<int> A(N); forn(N) scanf("%d", &A[i]);
#define v vector
#define File "Patterns"
using namespace std;

map<char, int> MAP;

string take(string name, char from, int num)
{
	int rem = MAP[from];
	forn(name.length())
	{
		MAP[name[i]] -= rem;
	}
	return string(rem, num + '0');
}
string solve()
{
	string _0 = take("ZERO", 'Z', 0);
	string _2 = take("TWO", 'W',2);
	string _6 = take("SIX", 'X',6);
	string _8 = take("EIGHT", 'G',8);
	string _3 = take("THREE", 'H',3);

	string _4 = take("FOUR", 'U',4);
	string _1 = take("ONE", 'O',1);
	string _5 = take("FIVE", 'F',5);
	string _7 = take("SEVEN", 'V', 7);
	string _9 = take("NINE", 'I', 9);

	return _0 + _1 + _2 + _3 + _4 + _5 + _6 + _7 + _8 + _9;
}
int main()
{
#if defined(_DEBUG) || defined(_RELEASE)
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#else
	//freopen(File".in", "r", stdin); freopen(File".out", "w", stdout);
#endif

	int T; cin >> T;
	for (int test = 1; test <= T; test++)
	{
		string s; cin >> s;
		MAP.clear();
		forn(26)
		{
			MAP['A' + i] = count(ALL(s), 'A' + i);
		}
		cout << "Case #" << test << ": " << solve() << endl;
	}

	//printf("\n\ntime-%.3lf", clock()*1e-3);
	return 0;
}