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
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define bublic public
#define clr(x) memset((x), 0, sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define sz size()
#define For(i, st, en) for(int i=(st); i<=(int)(en); i++)
#define Ford(i, st, en) for(int i=(st); i>=(int)(en); i--)
#define forn(i, n) for(int i=0; i<(int)(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)
#define fori(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); it++)

template <class _T> inline _T sqr(const _T& x) { return x * x; }
template <class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }
template <class _T> inline istream& operator << (istream& is, const _T& a) { is.putback(a); return is; }

typedef long double ld;

// Constants
const ld PI = 3.1415926535897932384626433832795;
const ld EPS = 1e-11;

// Types
typedef signed   long long i64;
typedef unsigned long long u64;
typedef set < int > SI;
typedef vector < ld > VD;
typedef vector < int > VI;
typedef vector < bool > VB;
typedef vector < string > VS;
typedef map < string, int > MSI;
typedef pair < int, int > PII;

int qq;
int a, b, c;
long long int solve(int a, string aa)
{
	long long int *temp = (long long int *)malloc(sizeof(long long int)*1100);
	long long int count=0;
	for(int i=0;i<=a;i++)
	{
		int num = aa[i]-'0';
		if(i==0)
		{
			temp[i] =0;
					count+=num;

		}
		else
		{
			if(count>=i)
			{
				temp[i]=temp[i-1];
				count+=num;
			}
			else
			{
				temp[i] = temp[i-1]+1;
						count+=num+1;
			}
		}
	}
	count = temp[a];
	free(temp);
	return count;
}
int main()
{
	freopen("in.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	scanf("%d", &qq);
	forn(ii, qq)
	{
		string aa;
		printf("Case #%d: ", ii+1);
		cin>>a>>aa;
		long long int ans = solve(a,aa) ;//? (32 - __builtin_clz(k)) : 0;
		printf("%ld\n", ans);
	}

	return 0;
}
