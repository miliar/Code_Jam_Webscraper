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
long long int solve1(int a, int aa[10005])
{
	long long int sum=0;
	for(int i=1;i<a;i++)
	{
		if(aa[i]<aa[i-1])
			sum+=aa[i-1]-aa[i];
	}
	return sum;
}
long long int solve2(int a, int aa[10005])
{
	long long int maxdiff=0;
	for(int i=1;i<a;i++)
	{
		if(aa[i]<aa[i-1])
			if(aa[i-1]-aa[i]>maxdiff)
				maxdiff = aa[i-1]-aa[i];
	}
	long long int sum=0;
	long long int prev=0;
	for(int i=0;i<a-1;i++)
	{
		if(aa[i]<=maxdiff)
			sum+=aa[i];
		else
		{
			sum+=maxdiff;

		}
	}
	return sum;
}
int main()
{
	freopen("in.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	scanf("%d", &qq);
	forn(ii, qq)
	{
		
		int aa[10005];
		printf("Case #%d: ", ii+1);
		//std::cout<<ii+1<<endl;
		cin>>a;
		for(int i=0;i<a;i++)
			cin>>aa[i];
		long long int ans = solve1(a,aa) ;//? (32 - __builtin_clz(k)) : 0;
		long long int ans2 = solve2(a,aa) ;//? (32 - __builtin_clz(k)) : 0;
		printf("%ld", ans);
		printf(" %ld\n", ans2);
	}

	return 0;
}
