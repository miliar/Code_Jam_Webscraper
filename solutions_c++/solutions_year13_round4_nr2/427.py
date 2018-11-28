#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
#include <queue>
#define FWD(a,b,c) for(int a=(b); a<(c); ++a)
#define BCK(a,b,c) for(int a=(b); a>(c); --a)
#define PII pair<int, int>
#define x first
#define y second

using namespace std;

typedef long long LL;

const LL mod = 1000002013;

bool is_guaranteed(LL x, LL n, LL p){
	//printf("sprawdzam %lld %lld %lld\n", x, n, p);
	while(p > 0){
		if(x == 0)
			return true;
		x = (x-1)/2;
		n /= 2;
		p -= n;
	}
	return false;
}

int main(){
	int n, m;
	LL p, x, y;
	int Z;
	scanf("%d", &Z);
	FWD(z,1,Z+1){
		scanf("%d %lld", &n, &p);
		printf("Case #%d: ", z);
		//guaranteed
		x = 0;
		y = (1LL<<n);
		while(y-x>1)
			if(is_guaranteed((x+y)/2, (1LL<<n), p))
				x = (x+y)/2;
			else
				y = (x+y)/2;
		printf("%lld ", x);
		//could
		m = 0, y = (1<<n)-1;
		while(y >= p){
			++m;
			y = y/2;
		}
		printf("%lld\n", (1LL<<n) - (1LL<<m));
	}
}

