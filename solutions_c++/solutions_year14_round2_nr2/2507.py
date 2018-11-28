#define _CRT_SECURE_NO_WARNINGS
#include <set>
#include <map>
#include <cmath>
#include <stack>
#include <queue>
#include <string>
#include <cstdio>
#include <vector>
#include <cctype>
#include <climits>
#include <ctime>
#include <sstream>
#include <cstdlib>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define fast ios_base::sync_with_stdio(false)


#define read freopen("in.in","r",stdin)
#define write freopen("out.in","w",stdout)

#define rep(i,a,b) for(int i=a;i<b;++i)
#define rep_(i,a,b) for(int i=a;i>=b;--i)
#define rep_it(it,a) for(auto it = a.begin();it!=a.end();++it)
#define wh(t) while(t--)

#define Set(a,b) memset(a,b,sizeof a)
#define Vset(a,b,c) a.resize(b,c)
#define clr(a) a.clear()
#define Sz(a) a.size()
#define Arrsz(a) sizeof a / sizeof a[0]
#define All(a) a.begin(),a.end()
#define mp make_pair
#define mpp(a,b,c) mp(mp(a,b),c)

#define Bug puts("Bug")
#define Nl puts("");
#define Vi vector
#define pr pair
#define oo (1<<29)

#define isnum(a) (a>=48 && a<=57)
#define isS(a) (a>='a' && a<='z')
#define isU(a) (a>='A' && a<='Z')
#define toS(a) (isU(a)?a+32:a)
#define toU(a) (isS(a)?a-32:a)
#define toC(a) a&15

typedef long long lli;
typedef unsigned long long llu;
typedef Vi<int> vi;
typedef pr<int, int> pii;
typedef pr<int, pii> piii;
typedef map<string, int>::iterator Mit;
typedef set<lli>::iterator Sit;

template<typename T>
inline void get(T &x)
{
	T y, s = 1, i = 10;
	y = 0;
	char c = getchar();
	while (!isnum(c)) {
		if (c == '-')s = -1;
		c = getchar();
	}
	while (isnum(c))y = (y << 1) + (y << 3) + (toC(c)), c = getchar();
	if (c != '.')goto rt;
	c = getchar();
	while (isnum(c))y = y + (toC(c)) / i, i = (i << 1) + (i << 3), c = getchar();
rt:
	x = y*s;
}

template<typename T>
inline void put(T x)
{
	if (!x) {
		putchar('0');
		return;
	}
	char c[10] = {};
	int ln = 0;
	while (x) {
		c[ln++] = x % 10;
		x /= 10;
	}
	while (ln--) {
		putchar(c[ln] + '0');
	}

}

#define si(a) get(a)
#define sii(a,b) get(a),get(b)
#define siii(a,b,c) get(a), get(b),get(c)
int main()
{


	int t;
	si(t);
	while (t--) {
		static int k = 1;
		printf ("Case %d: ",k++);
		int a,b,c,sum =0 ;
		siii(a,b,c);
		rep(i,0,a+1){
			rep(j,0,b+1){
				if(i&j < c)sum++;
			}
		}
		printf("%d ",sum);
	
	}
	return 0;
}