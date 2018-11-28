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

int tab[10005];

int jebaj()
{
	int n, m, wyn = 0;
	cin >> n >> m;
	REP(i, n)
		cin >> tab[i];
	sort(tab, tab + n);
	int pocz = 0, kon = n - 1;
	while(pocz <= kon)
	{
		if(pocz == kon)
		{
			wyn++;
			kon--;
		}
		else
		{
		if(tab[pocz] + tab[kon] > m)
		{
			wyn++;
			kon--;
		}
		else
		{
			wyn++;
			
			pocz++;
			kon--;
		}
	}
	}	
	return wyn;
}

int main()
{
	IOSYNC;
	int t;
	//t = 1;
	cin >> t;
	
	REP(i, t) 
	{
		cout << "Case #" << i + 1 << ": ";
		cout << jebaj() << "\n";;
	}
}
