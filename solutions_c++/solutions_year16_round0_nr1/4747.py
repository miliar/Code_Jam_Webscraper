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
#include <sstream>

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

int T,n,d;
bool b[10];

void tra(int c)
{
	stringstream ss;
	ss << c;
	string s = ss.str();
	forn(i,s.size())
		b[s[i]-'0']=1;
}

bool chk()
{
	forn(i,10)
		if(b[i]==0)
			return 0;
	return 1;
}

int main()
{
	freopen("z.in", "rt", stdin);
	freopen("z.out", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	cin >>T;
	forn(I,T)
	{
		forn(i,10)
			b[i]=0;
		
		cin >>n;
		if(n==0)
		{
			cout <<"Case #"<<I+1<<": "<<"INSOMNIA"<<endl;
			continue;	
		}
		
		d=n;
		tra(d);
		while(!chk())
		{
			d+=n;
			tra(d);
		}
		cout <<"Case #"<<I+1<<": "<<d<<endl;
	}

	return 0;
}
