#include<cstdio>

int n,t;

int func() {
	scanf("%d ", &n);
	int standed=0;
	int friends=0;
	for (int i=0; i<=n; i++) {
		int howmany = getchar()-'0';
//		printf("Howmany: %d\n",howmany);
		if (standed>8) continue;
		if(standed < i && howmany>0) {
			friends += i-standed;
			standed = i;
		}
		standed += howmany;
	}
	return friends;
}

int main() {
	scanf("%d ", &t);
	for(int tc=1; tc<=t; tc++) {
		printf("Case #%d: %d\n", tc, func());
	}
}

