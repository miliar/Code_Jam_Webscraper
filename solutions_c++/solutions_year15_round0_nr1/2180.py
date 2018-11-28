#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define clr(x) memset((x), 0, sizeof(x))
#define pb push_back
#define mp make_pair
#define sz size()
#define x first
#define y second
#define forn(i, n) for(int i=0; i<(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)

typedef long double ld;

// Constants
const ld PI = 3.1415926535897932384626433832795;
const ld EPS = 1e-11;

// Types
typedef signed   long long i64;
typedef unsigned long long u64;
typedef pair < int, int > PII;

int N,n,kol,ans;
string s;

int main()
{
	if(0)
	{
		freopen("z.in", "wt", stdout);
		cout <<100<<endl;
		forn(i,100)
		{
			cout <<1000<<' ';
			forn(j,999)
				cout <<'0';
			cout <<"9\n";
		}
	}
	freopen("z.in", "rt", stdin);
	freopen("z.out", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	cin >>N;
	forn(I,N)
	{
		cin >>n>>s;
		forn(i,1010)
		{
			kol=i;
			bool can=1;
			forn(j,s.size())
			{
				if(kol>=j)
					kol+=(int)(s[j]-'0');					
				else
					can=0;
			}	
			if(can)
			{
				cout <<"Case #"<<I+1<<": "<<i<<endl;
				break;
			}
		}
		
	}

	return 0;
}
