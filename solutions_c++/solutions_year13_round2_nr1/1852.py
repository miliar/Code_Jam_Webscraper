#include<cstdio>
#include<algorithm>

#define INF 100000000

using namespace std;

int absorb(int *A, int b) {
	if((*A)==1) return INF;
	int ret=0;
	while((*A)<=b) {
		(*A)+=(*A)-1;
		ret++;
	}
	return ret;
}


int main() {

	int T,N,A,t,i,ans,v;
	int motes[2000000]={0};

	scanf("%d", &T);
	for(t=1;t<=T;t++) {
		scanf("%d%d", &A, &N);
		for(i=0;i<N;i++) scanf("%d", &motes[i]);
		sort(motes, motes+N);
		ans=N;v=0;
		for(i=0;i<N;i++) {
			v+=absorb(&A, motes[i]);
			A+=motes[i];
			ans=min(ans, v+(N-1)-i);
		}
		printf("Case #%d: %d\n", t, ans);
	}

	return 0;
}
