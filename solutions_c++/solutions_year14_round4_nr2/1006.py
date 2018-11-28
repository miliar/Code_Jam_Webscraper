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

int bla[1003], tab[1003];
map<int, int> pozycja;
		

int jebaj2()
{
	int res = 10000001, n;
	cin >> n;
	REP(i, n)
	{
		cin >> tab[i];
		pozycja[tab[i]] = i;
		bla[i] = tab[i];
	}
	sort(tab, tab + n);
	
		int left = 0, right = n - 1;
		int count = 0;
		
		REP(i, n)
		{
			int p = pozycja[tab[i]];
			
			if(p - left < right - p)
			{
				FORD(j, p - 1, left)
				{
					pozycja[bla[j]]++;
					pozycja[bla[j + 1]]--;
					swap(bla[j], bla[j + 1]);
					count++;
				}
				left++;
			}
			else
			{
				FOR(j, p, right - 1)
				{
					pozycja[bla[j]]++;
					pozycja[bla[j + 1]]--;
					swap(bla[j], bla[j + 1]);
					count++;
				}
				right--;
			}
		}
	
	return count;
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
		cout << jebaj2() << "\n";;
	}
}
