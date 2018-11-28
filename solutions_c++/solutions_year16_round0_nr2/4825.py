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

int T;
string s;
int res,pos;

int main()
{
	freopen("z.in", "rt", stdin);
	freopen("z.out", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	cin >>T;
	forn(I,T)
	{
		cin >>s;
		res=0;
		while(1)
		{
			pos=-1;
			for(int i=s.size()-1; i>=0; i--)
				if(s[i]=='-')
				{
					pos=i;
					break;
				}
			if(pos==-1)
				break;
			res++;
			for(int i=0; i<=pos; i++)
			{
				if(s[i]=='-')
					s[i]='+';
				else
					s[i]='-';
			}
		}
		cout <<"Case #"<<I+1<<": "<<res<<endl;
	}


	return 0;
}
