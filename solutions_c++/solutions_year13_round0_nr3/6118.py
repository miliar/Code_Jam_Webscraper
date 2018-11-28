//Arek Wrobel - skater
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;
#define REP(I, N) for(int I=0; I<(N); ++I)
#define FOR(I, M, N) for(int I=(M); I<=(N); ++I)
#define FORD(I, M, N) for(int I=(M); I>=(N); --I)
#define FOREACH(IT, CON) for(__typeof(CON.begin()) IT=CON.begin(); IT!=CON.end(); ++IT)
#define ST first
#define ND second
#define MP make_pair
#define PB push_back
const int INF=1000000000;
const LL INFLL=1000000000000000000LL;

LL A, B;
LL wy;

int stos[128];
int iles;

bool check(LL x){
	iles=0;
	while(x){
		stos[iles++]=x%10;
		x/=10;
	}
	for(int i=iles/2; i<iles; ++i)
		if (stos[i]!=stos[iles-i-1])
			return false;
	return true;
}

int main()
{
	int T;
	scanf("%d", &T);
	FOR(lpt, 1, T){
		//wej
		scanf("%lld%lld", &A, &B);
		//prog
		wy=0;
		LL i=0;
		while(i*i<A) ++i;
		for(; i*i<=B; ++i)
			if (check(i) && check(i*i)){
				++wy;
//				printf("%lld: %lld -> %lld\n", wy, i, i*i);
			}
		//wyj
		printf("Case #%d: %lld\n", lpt, wy);
	}
	return 0;
}

