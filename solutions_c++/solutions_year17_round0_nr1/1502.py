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

int T,k;
string s;

int main()
{
	#ifdef LOCAL
	freopen("z.in","rt",stdin);
	freopen("z.out","wt",stdout);	
	#endif

	cin >>T;
	forn(I,T)
	{
		cin >>s>>k;
		int ans=0;
		forn(i,s.size()-k+1)
		{
			if(s[i]=='-')
			{
				ans++;
				forn(j,k)
				{
					if(s[i+j]=='-')
						s[i+j]='+';
					else
						s[i+j]='-';
				}
			}
		}

		bool ok=1;
		forn(i,s.size())
			if(s[i]=='-')
				ok=0;
		cout <<"Case #"<<I+1<<": ";
		if(ok)
			cout <<ans<<endl;
		else
			cout <<"Impossible"<<endl;
	}

	return 0;
}