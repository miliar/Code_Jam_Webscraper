#include "akash.h"
typedef double mytype;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	mytype init_rate = 2.0;
	int no_of_cases; scanf("%d", &no_of_cases);
	mytype C, F, X, t_prev,t_curr,t_temp;
	for (int case_no = 1; case_no <= no_of_cases; ++case_no) {
		scanf("%lf %lf %lf", &C,&F,&X);

		t_prev = (X/init_rate);
		t_curr = 0.0;
		for (int n = 0;  ; n++) {
			t_curr += (  C / (init_rate + (n*F))  );
			t_temp = t_curr + (X / (init_rate + (n+1)*F));
			if ( t_temp > t_prev ) break;
			t_prev = t_temp;
		}

		printf("Case #%d: %.7f\n", case_no,t_prev);
	}

	return 0;
}
