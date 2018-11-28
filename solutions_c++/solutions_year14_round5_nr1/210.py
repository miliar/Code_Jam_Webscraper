#include <cstdio>
#include <vector>

using namespace std;

typedef long long t;

static int n,p,q,r,s;
static t data[1000005];
static t sumTo[1000005];
static t sumAll;

static t sum(int a,int b);
static t calc();
static bool test(t lim);

int main() {
	int cases;
	scanf("%d",&cases);
	for(int round=1; round<=cases; round++) {
		scanf("%d%d%d%d%d",&n,&p,&q,&r,&s);
		for(int i=0; i<n; i++)
			data[i]=(((long long)i)*p+q)%r+s;
		sumTo[0]=0;
		for(int i=0; i<n; i++)
			sumTo[i+1]=sumTo[i]+data[i];
		sumAll=sumTo[n];
		t best=calc();
		double prob=(double)best/sumAll;
		printf("Case #%d: %0.12f\n",round,prob);
	}
	return 0;
}

static t sum(int a,int b) {
	return sumTo[b]-sumTo[a];
}

static t calc() {
	if(n==1)
		return 0;
	if(n==2)
		return min(data[0],data[1]);
	t lo=0,hi=sumAll+1,mid;
	while(lo+1<hi) {
		mid=(lo+hi)/2;
		if(test(mid-1))
			hi=mid;
		else
			lo=mid;
	}
	return sumAll-lo;
}

static bool test(t lim) {
	int used=0;
	int from=0,to;
	for(to=1; to<=n; to++) {
		while(sum(from,to)>lim) {
			from=to-1;
			used++;
			if(used>=3)
				return false;
		}
	}
	return true;
}

