#include <algorithm>
#include <iostream>
#include <sstream>
#include <cassert>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <deque>
#include <ctime>
#include <list>
#include <set>
#include <map>
//zlb//

using namespace std;

typedef long long     LL;
typedef pair<int,int> pii;

double PI  = acos(-1);
double EPS = 1e-7;
int INF    = 1000000000;
int MOD    = 1000000007;
int MAXINT = 2147483647;
LL INFLL   = 1000000000000000000LL;
LL MAXLL   = 9223372036854775807LL;

#define fi            first
#define se            second
#define mp            make_pair
#define pb            push_back
#define SIZE(a)       (int)a.size()
#define MIN(a, b)     (a) = min((a), (b))
#define MAX(a, b)     (a) = max((a), (b))
#define input(in)     freopen(in,"r",stdin)
#define output(out)   freopen(out,"w",stdout)
#define RESET(a, b)   memset(a,b,sizeof(a))
#define FOR(a, b, c)  for (int (a)=(b); (a)<=(c); (a)++)
#define FORD(a, b, c) for (int (a)=(b); (a)>=(c); (a)--)
#define FORIT(a, b)   for (__typeof((b).begin()) a=(b).begin(); a!=(b).end(); a++)

int mx[8] = {-1,1,0,0,-1,-1,1,1};
int my[8] = {0,0,-1,1,-1,1,-1,1};

// ------------ //

struct trie
{
	trie* nx[26];
};

trie *head[4];
int co = 0;

trie *init()
{
	co++;
	trie *tmp = new trie;
	FOR(a,0,25)
	{
		tmp->nx[a] = NULL;
	}
	return tmp;
}

string k[1005];

void add(int x,int pos,trie *cur)
{
	if (pos == k[x].length()) return;
	int c = k[x][pos]-'A';
	if (cur->nx[c] == NULL)
	{
		cur->nx[c] = init();
	}
	add(x,pos+1,cur->nx[c]);
}

void clean(trie *cur)
{
	if (cur == NULL) return;
	FOR(a,0,25)
	{
		clean(cur->nx[a]);
	}
	delete cur;
}

int maks = -1;
int num = 0;
int ada[5];
int lol[100];
int m,n;

void go(int pos)
{
	if (pos == m)
	{
		FOR(a,0,n-1)
		{
			if (ada[a] == 0) return;
		}
		co = 0;
		FOR(a,0,n-1)
		{
			head[a] = init();
		}
		FOR(a,0,m-1)
		{
			add(a,0,head[lol[a]]);
		}
		if (maks < co)
		{
			maks = co;
			num = 1;
		}
		else if (maks == co) num++;
		FOR(a,0,n-1)
		{
			clean(head[a]);
		}
		return;
	}
	FOR(a,0,n-1)
	{
		ada[a]++;
		lol[pos] = a;
		go(pos+1);
		ada[a]--;
	}
}

int main()
{
	int t,tc=0;
	scanf("%d",&t);
	while(t--)
	{
		tc++;
		printf("Case #%d: ",tc);
		
		scanf("%d%d",&m,&n);
		FOR(a,0,m-1)
		{
			cin >> k[a];
		}
		
		maks = -1;
		num = 0;
		go(0);

		FOR(a,0,n-1)
		{
			ada[a] = 0;	
		}
		FOR(a,0,m-1)
		{
			k[a] = "";
		}
		co = 0;
		printf("%d %d\n",maks,num);
	}
}
