#include <bits/stdc++.h>

#define FWD(a,b,c) for(int a=(b); a<(c); ++a)
#define SIZE(a) ((int)a.size())
#define pb push_back
#define PII pair<int, int>
#define x first
#define y second

using namespace std;

typedef long long LL;

int n, p, q, r, s;

int at(int i){
	return ((LL)i*p+q) % r + s;
}

bool check(LL w){
	LL c = 0;
	int k = 0;
	FWD(i,0,n){
		if(at(i) > w) return 0;
		if(at(i) + c > w){
			++k;
			c = 0;
		}
		c += at(i);
	}
	if(c) ++k;
	return k <= 3;
}

int main(){
	int Z; scanf("%d", &Z); FWD(z,1,Z+1){
		LL low = 0, high = 0, sum = 0;
		scanf("%d %d %d %d %d", &n, &p, &q, &r, &s);
		//printf("case:\n");
		//if(n < 20) FWD(i,0,n) printf("%d ", at(i));
		//printf("\n");
		FWD(i,0,n) sum += at(i);
		high = sum;
		while(high-low > 1){
			if(check((low+high)/2))
				high = (low+high)/2;
			else
				low = (low+high)/2;
		}
		//printf("sum: %lld high: %lld\n", sum, high);
		printf("Case #%d: %.10Lf\n", z, (long double)(sum-high)/sum);
	}
	return 0;
}
