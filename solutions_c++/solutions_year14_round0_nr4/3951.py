#include <stdio.h>
#include <algorithm>

using namespace std;

int main () {
	int T;		//number of test-cases
	int test_case = 0, N, index, inner_index, war_points, lower_limit, deceitful_war_points;
	double masses_naomi[1000], masses_ken[1000];

	scanf("%d",&T);

	while (test_case++ < T) {
		//scan and proces one test-case
		scanf("%d", &N);

		for(index = 0; index < N; index++)
			scanf("%lf", &masses_naomi[index]);

		for(index = 0; index < N; index++)
			scanf("%lf", &masses_ken[index]);

		sort(masses_naomi, masses_naomi + N);
		sort(masses_ken, masses_ken + N);

		//calculate regular war game points
		inner_index = N-1, war_points =0, lower_limit = 0;
		for(index = N-1; index >= 0 && inner_index >= lower_limit; index--) {
			for(; inner_index >= lower_limit; inner_index--) {
				if (masses_naomi[index] > masses_ken[inner_index]) {
					lower_limit++;
					break;
				}
				if (masses_naomi[index] < masses_ken[inner_index]) {
					war_points++;
					inner_index--;
					break;
				}
			}
		}
		war_points = N - war_points;

		//calculate Deceitful war points
		deceitful_war_points = 0, lower_limit = 0, inner_index = N - 1;
		for(index = N-1; index >= lower_limit && inner_index >= 0; index--) {
			for(; inner_index >= 0; inner_index--, lower_limit--) {
				if(masses_naomi[index] > masses_ken[inner_index]) {
					deceitful_war_points++;
					inner_index--;
					break;
				}
			}
		}		
		//print result
		printf("Case #%d: %d %d\n", test_case, deceitful_war_points, war_points);
	}
	return 0;
}
