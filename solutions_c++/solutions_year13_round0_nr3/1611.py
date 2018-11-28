#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<utility>
#include<sstream>
#include<cstring>
#include <string>

//#include <iostream>

using namespace std;

#define REP(i,v)for(int i=0;i<(v);++i)
#define FOR(i,x,v)for(int i=x;i<=(v);++i)
#define FORD(i,x,v)for(int i=x;i>=(v);--i)
#define VAR(v,n) __typeof(n) v = (n)
#define FOREACH(i,c) for(VAR(i,(c).begin()); i != (c).end(); ++i)
#define ALL(c) (c).begin(), c.end()
#define PB push_back
#define SZ size
#define MP make_pair
#define FI first
#define SE second
#define CL clear()
#define RS resize
#define INFTY 1000000001
#define EPS 10e-9
#define SIZE(x) ((int)(x).size())

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<bool> VB;
typedef pair<int,int> PII;
typedef long long LL;
typedef vector<string> VS;

void show(PII p)
{printf("(%d %d)\n",p.FI,p.SE);}

void show(VI e)
{REP(i,SIZE(e)) printf("%d ",e[i]); printf("\n");}

void show(vector<PII> e)
{REP(i,SIZE(e)) printf("(%d %d) ",e[i].FI,e[i].SE); printf("\n");}

void show(VS e)
{REP(i,SIZE(e)) printf("%s\n",e[i].c_str());}

void show(VVI e)
{REP(i,SIZE(e)) show(e[i]);}

#define MAX_AB 100000000000001
#define MAX_SQ_AB 10000001
int cache[MAX_SQ_AB];


LL reversed(LL l){
    LL res = 0, last;
    while(l > 0){
        last = l % 10;
        res = res * 10 + last;
        l /= 10;
    }
    return res;
}

void fill_cache(){
    int count = 0;
    LL i, i2;
    for(i=1; i < MAX_SQ_AB ; i++){
        if(i == reversed(i)){
            i2 = i*i;
            if(i2 == reversed(i2)){
                count++;
            }
        }
        cache[i] = count;
    }
}

int main()
{
    int t;
    LL a, b, as, bs, count, x2;
    scanf("%d", &t);

    fill_cache();

    REP(i,t){
        scanf("%lld %lld", &a, &b);
        as = ceil(sqrt(a));
        bs = floor(sqrt(b));

        count = cache[bs] - cache[as-1];

        printf("Case #%d: %lld\n", i+1, count);
    }
	return 0;
}

