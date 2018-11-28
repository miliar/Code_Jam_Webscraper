//Karol Kaszuba
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef double D;
typedef long double LD;
typedef vector<PII> VII;

#define FOR(i,x,y) for(int i=(x);i<=(y);++i)
#define REP(i,x) FOR(i,0,(x)-1)
#define FORD(i,x,y) for(int i=(x);i>=(y);--i)
#define VAR(i,c) __typeof(c) i=(c)
#define FORE(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)

#define SIZE(c) (int)((c).size())
#define ALL(c) (c).begin(),(c).end()
#define PB push_back
#define IN insert
#define ER erase
#define MP make_pair
#define ST first
#define ND second
#define IOSYNC ios_base::sync_with_stdio(0)

int tab[10][10];

void jebaj(int test_case)
{
	int a, b;
	set <int> secik;
	cin >> a;
	REP(i, 4) REP(j, 4) cin >> tab[i + 1][j + 1];
	REP(i, 4) secik.IN(tab[a][i + 1]);
	cin >> b;
	REP(i, 4) REP(j, 4) cin >> tab[i + 1][j + 1];
	VI v;
	REP(i, 4)
		if(secik.find(tab[b][i + 1]) != secik.end()) v.PB(tab[b][i + 1]);
	cout << "Case #" << test_case << ": ";
	if(SIZE(v) == 1)
	{
		cout << v[0] << "\n";
		return;
	}
	if(v.empty())
	{
		cout << "Volunteer cheated!\n";
		return;
	}
	cout << "Bad magician!\n";
	
}

int main()
{
	IOSYNC;
	int t;
	cin >> t;
	REP(i, t) jebaj(i + 1);
}
