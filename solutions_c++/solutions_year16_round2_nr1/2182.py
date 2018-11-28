#include <iostream>
#include <stack>
#include <queue>
#include <algorithm>
#include <set>
#include <string>
#include <map>
#include <utility>

using namespace std;

#define REP(i , a) for (int i = 0 ; i < (a); ++i)
#define FOR(i, a, b) for ( int i = a ; i < (b); ++i )
#define REPE(i, a) REP(i, a+1)
#define FORE(i, a, b) FOR(i,a,b+1)
#define BG begin()
#define ST first
#define ND second
#define ED end()
#define MP(a,b) make_pair(a,b)
#define lli long long int
#define ulli unsigned long long int
#define PII pair < int, int >
#define VI vector<int>
#define VPII vector < PII >

void rem(char * p, int * a)
{
	while (*p)
	{
		a[*p]--;
		p++;
	}
}

int main()
{
	char * p[10] = {
		"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
	int t;
	cin >> t;
	VI an;
	string s;
	int a[100];
	FORE(z, 1, t)
	{
		REP(i, 100)
			a[i] = 0;
		cout << "Case #" << z << ": ";
		cin >> s;
		if (s.size() < 3)
			cin >> s;
		REP(i, s.size())
			++a[s[i]];
		while (a['Z'])
		{
			rem(p[0], a);
			an.push_back(0);
		}
		while (a['G'])
		{
			rem(p[8], a);
			an.push_back(8);
		}
		while (a['W'])
		{
			rem(p[02], a);
			an.push_back(02);
		}
		while (a['U'])
		{
			rem(p[04], a);
			an.push_back(04);
		}
		while (a['X'])
		{
			rem(p[06], a);
			an.push_back(06);
		}
		while (a['O'])
		{
			rem(p[01], a);
			an.push_back(01);
		}
		while (a['S'])
		{
			rem(p[07], a);
			an.push_back(07);
		}
		while (a['V'])
		{
			rem(p[5], a);
			an.push_back(05);
		}
		while (a['T'])
		{
			rem(p[3], a);
			an.push_back(03);
		}

		while (a['I'])
		{
			rem(p[9], a);
			an.push_back(9);
		}

		sort(an.BG, an.ED);
		REP(i, an.size())
			cout << an[i];
		cout << endl;
		an.clear();
	}
	return 0;
}