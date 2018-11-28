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
long long int solve(int a, int b,int c)
{
	if(a==1)
		return 0;
	if(a==2)
	{
		if((b*c)%2==0)
			return 0;
		else
			return 1;
	}
	if(a==3)
	{
		if(b==3&&c>=2)
			return 0;
		else if(c==3&&b>=2)
			return 0;
		else
			return 1;
	}
	if(a==4)
	{
			int index = (b-1)*4+c-1;
			switch(index)
			{
				case 0 : return 1; break;
				case 1 : return 1;break;
				case 11: return 0;break;
				case 14: return 0;break;
				case 15: return 0;break;
				default: return 1;break;
			}
	}
	return 0;
}
int main()
{
	freopen("in.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	scanf("%d", &qq);
	forn(ii, qq)
	{
		
		int aa[1005];
		printf("Case #%d: ", ii+1);
		//std::cout<<ii+1<<endl;
		cin>>a>>b>>c;
		long long int ans = solve(a,b,c) ;//? (32 - __builtin_clz(k)) : 0;
		if(ans==0)
			cout<<"GABRIEL"<<endl;
		else
			cout<<"RICHARD"<<endl;
	//	printf("%ld\n", ans);
	}

	return 0;
}
