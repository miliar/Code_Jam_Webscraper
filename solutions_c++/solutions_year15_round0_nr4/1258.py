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

int N,x,r,c;

int main()
{
	freopen("z.in", "rt", stdin);
	freopen("z.out", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	cin >>N;
	forn(I,N)
	{
		cin >>x>>r>>c;
		if(r>c)
			swap(r,c);

		bool win=1;
		if(x==2 && (r*c)%2==1)
			win=0;
		if(x==3)
		{
			if((r*c)%3!=0 || r==1)
				win=0;
		}
		if(x==4)
		{
			if((r*c)%4!=0 || r<3)
				win=0;
        }

		cout <<"Case #"<<I+1<<": ";
		if(win)
			cout <<"GABRIEL\n";
		else
			cout <<"RICHARD\n";		
	}

	return 0;
}
