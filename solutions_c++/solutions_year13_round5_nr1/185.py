#include<functional>
#include<algorithm>
//#include<iostream>
#include<numeric>
#include<cassert>
#include<cstring>
#include<cstdio>
#include<vector>
#include<queue>
//#include<cmath>
#include<set>
#include<map>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef vector<LL> VLL;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,b,e) for(int i=(b);i<=(e);++i)
#define FORD(i,b,e) for(int i=(b);i>=(e);--i)
#define FOReach(it,V) for(__typeof((V).begin()) it=(V).begin();it!=(V).end();++it)

#define PB push_back
#define ALL(V) (V).begin(),(V).end()
#define SIZE(V) ((int)(V).size())

#define MP make_pair
#define ST first
#define ND second

#define DBG

#ifdef DBG
	#define debug(...) fprintf(stderr, __VA_ARGS__)
#else
	#define debug(...)
#endif

int stmp;
#define scanf stmp=scanf


const int MAX = 40;
const int MAXV = 1000;
const int INF = 1000000001;

int n, k;
int arr[MAX];
int cnt[MAXV+1];

int main(int argc, char *argv[]) {
	int Z;
	scanf("%d", &Z);
	FOR(z,1,Z)
	{
		printf("Case #%d: ", z);
		scanf("%d %d", &k, &n);
		REP(i,37) arr[i] = 0;
		REP(i,n) scanf("%d", arr+i);
		double res = 0.;
		FOR(s,1,2*MAXV)
		{
			VI V;
			REP(i,37)
				if(arr[i] <= s)
					V.PB(s-arr[i]);
			int sum = accumulate(ALL(V), 0);
			if(sum > k) break;
			sort(ALL(V));
			int sz = SIZE(V);
			int in = sum;
			int ingame = sum;
			FOReach(it,V)
			{
				if(in > k) break;
				res = max(res, (double)- in + 36.*ingame/sz);
				in++;
				ingame -= *it;
				--sz;
			}
		}
		printf("%.10lf\n", res);
	}
	return 0;
}

