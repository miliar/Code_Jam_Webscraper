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

#define FN "A-large"

#define N 111000


int main()
{
	freopen(FN ".in","r",stdin);
	freopen(FN ".out","w",stdout);

	int T,X;
	scanf("%d",&X);
	FOR(T,1,X)
	{
       printf("Case #%d: ",T);
       LL a=0,n=0;
       LL V[101];
       int o=0,temp=0;
       cin >> a >> n;
       REP(i,n) cin >> V[i];
       vector<int> v (V, V+n);
       SORT(v);
       bool out=false;
       if (a==1) o=n;
       else
       REP(i,n)
       {
            temp = 0;
            while (true)
            {
                if (a<=v[i])
                {
                    temp++;
                    a+=a-1;
                    if (v[i]<a)
                    {
                       a+=v[i];
                       if (temp<n-i)
                           o+=temp;
                       else
                       {
                           o+=n-i;
                           out = true;
                       }
                       break;
                    }
                }
                else
                {
                    a+=v[i];
                    if (temp<n-i)
                        o+=temp;
                    else
                    {
                        o+=n-i;
                        out = true;
                    }
                    break;
                }
                if (o>n) break;
                if (out) break;
            }
            if (o>n) break;
            if (out) break;
        }
        if (o>n) o=n;
        printf("%d\n",o);
	}
	return 0;
}
