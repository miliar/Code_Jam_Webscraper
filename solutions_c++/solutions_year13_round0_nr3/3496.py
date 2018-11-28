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

int k;
i64 a,b,ans;
vector <int> v1,v2;

bool pal(int i)
{
	v1.clear();
	v2.clear();
	while(i>0)
	{
		v1.pb(i%10);
		v2.pb(i%10);
		i/=10;
	}
	reverse(v2.begin(),v2.end());
	forn(i,v1.size())
		if(v1[i]!=v2[i])
			return 0;
	return 1;
}

int main()
{
	freopen("z.in", "rt", stdin);
	freopen("z.out", "wt", stdout);

	cin >>k;
	forn(t,k)
	{
		cout <<"Case #"<<t+1<<": ";
		cin >>a>>b;
		
		ans=0;
		for(i64 i=1; i*i<=b; i++)
		{
			if(pal(i))
				if(pal(i*i) && i*i>=a)
						ans++;
		}
		cout <<ans<<endl;
	}

	return 0;
}
