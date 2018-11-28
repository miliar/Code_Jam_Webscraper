#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<climits>
#include<sstream>

#include<algorithm>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<utility>
#include<stack>
#include<queue>
#include<deque>
#include<list>
#include<bitset>

using namespace std;

typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef vector<string> vs; 
typedef pair<int,int> ii;
typedef long long int LLI;
typedef unsigned long long int ULLI;

#define sz(a)                        int((a).size()) 
#define pb                           push_back 
#define mp                           make_pair
#define F                            first
#define S                            second
#define present(c,x)                 ((c).find(x) != (c).end()) 
#define cpresent(c,x)                (find(all(c),x) != (c).end())
#define tr(c,i)                      for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define all(c)                       (c).begin(),(c).end()
#define si(n)                        scanf("%d",&n)
#define sl(n)                        scanf("%lld",&n)
#define sf(n)                        scanf("%f",&n)
#define sd(n)                        scanf("%lf",&n)
#define ss(n)                        scanf("%s",n)

#define abs(x)                       ((x)<0?-(x):(x))
#define fill(a,v)                    memset((a),(v),sizeof (a))
#define INF                          INT_MAX
#define LINF                         (long long)1e18
#define EPS                          1e-9
#define MAX 10000000

map<LLI, int> m;

bool ispal(LLI x)
{
	LLI rx = 0, xx = x;
	while(x > 0)
	{
		rx = 10*rx + x%10;
		x /= 10;
	}
	return (xx == rx);
}

void pre()
{
	LLI sq;
	int cnt = 0;
	for(int i=0; i<=MAX; ++i)
		if(ispal(i) && ispal((sq = 1LL*i*i)))
			m[sq] = ++cnt;
}

int main()
{
	pre();
	int t;
	LLI a, b;

	si(t);
	for(int cases=1; cases<=t; ++cases)
	{
		printf("Case #%d: ",cases);
		sl(a); sl(b);
		map<LLI, int>::iterator it1 = m.lower_bound(a);
		map<LLI, int>::iterator it2 = m.upper_bound(b);
		printf("%d\n",it2->S - it1->S);
	}
	return 0;
}
