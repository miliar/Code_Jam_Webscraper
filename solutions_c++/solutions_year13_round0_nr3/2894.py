#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <numeric>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>

using namespace std;

#define REP(i,n) for (int i=0,_n=(n); i < _n; i++)
#define REPD(i,n) for (int i=(n)-1; i >= 0; i--)
#define FOR(i,a,b) for (int _b=(b), i=(a); i <= _b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))

#define CLEAR(x) memset(x,0,sizeof x);
#define CLEARA(x) memset(&x,0,sizeof x);
#define FILL(x,v) memset(x,v,sizeof x);
#define FILLA(x,v) memset(&x,v,sizeof x);

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 0x7fffffff
#define X first
#define Y second
#define pb push_back
#define SZ(c) (int)(c).size()
#define MP make_pair
#define eps 1.0e-11
const double pi = acos(-1.0);

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;

#define FN "C-small-attempt0"

#define N 111000
bool possible;

bool isPalindrome(LL n) 
{
    if (n<10) return true;
    int length = (int)log10(n);
    LL xx = (int)pow((double)10,length);
    int fd = n / xx;
    int ld = n % 10;
    if (fd!=ld) return false;
    else 
    {
        int nd = (n % xx);
        nd /= 10;
        return isPalindrome(nd);
    }
}
int main()
{
	freopen(FN ".in","r",stdin);
	freopen(FN ".out","w",stdout);

	int T,X,acc;
	LL A,B;
	A=0;B=0;
	scanf("%d",&X);
	FOR(T,1,X)
	{
       printf("Case #%d: ",T);
       scanf("%d %d",&A,&B);
       acc=0;
       int ra = (int)sqrt(A);
       if (ra<sqrt(A)) ra++;
       int rb = (int)sqrt(B);
       FOR(i,ra,rb)
       {
            if (isPalindrome(i) and isPalindrome(i*i)) acc++;
       }
       cout << acc << endl;
	}
	return 0;
}
