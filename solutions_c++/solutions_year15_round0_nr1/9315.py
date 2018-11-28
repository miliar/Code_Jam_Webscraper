#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

typedef long long LL;
typedef double DB;
typedef unsigned UINT;
typedef unsigned long long ULL;

#define min(a, b)  a < b ? a : b
#define max(a, b)  a > b ? a : b

#define rep(i,n) for(int i=0;i<n;++i)
#define rep1(i,n) for(int i=1;i<=n;++i)
#define repab(i,a,b) for(int i=a;i<=b;++i)
#define dwn(i,n) for (int i=n-1;i>-1;--i)
#define dwn1(i,n) for (int i=n;i>0;--i)
#define dwnab(i,a,b) for(int i=a;i>=b;--i)
#define each(it, A) for (__typeof(A.begin()) it=A.begin(); it != A.end(); ++it)

#define pair pii<int, int>
#define all(v) (v).begin(), (v).end()
#define pb(x) push_back(x)
#define mp(x,y) make_pair((x),(y))
#define sortv(v) sort(all(v))

#define mset(m) memset(m,0,sizeof(m))

#define sz(c) (int)c.size()
#define ff first
#define ss second

#define SI ({int x;scanf("%d", &x);x;});
#define SL ({LL x;scanf("%I64d", &x);x;});

#define PI(n) printf("%d", n);
#define PLL(n) printf("%I64d", n);

#define PILN(n) printf("%d\n", n);
#define PLLN(n) printf("%I64d\n", n);

#define PLN printf("\n");

#define MAX 2222

int n, t, sm;
char s[MAX];

int main() 
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	t = SI
	
	rep1(tt, t)
	{
		n = SI
		scanf("%s", s);
			
		int count = (s[0] - '0'), friends = 0;
		
		rep1(i, n)
		{
			if (count < i)
			{
				friends += (i - count);
				count = i;
			}
			count += (s[i] - '0');
		}
		
		printf("Case #%d: %d\n", tt, friends);
	}
	
    return 0;
}


