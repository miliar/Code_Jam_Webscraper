#include<stdio.h>

int main() {

	int T;
	double C,F,X;
	double ans_min, next_ans;
	int num=1, i, j;

	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);

	scanf("%d", &T);
	while(T-->0) {
		scanf("%lf %lf %lf", &C, &F, &X);
		ans_min = X/2.0;

		for(i=1 ;  ; i++) {
			for(j=1,next_ans=0 ; j<=i ; j++) next_ans+=C/(2.0+F*(j-1));
			next_ans+=X/(2.0+F*i);

			if(ans_min<next_ans) break;
			else ans_min = next_ans;
		}

		printf("Case #%d: ", num++);
		printf("%.7lf\n", ans_min);
	}

	return 0;
}