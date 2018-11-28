#include<stdio.h>

int main(void){
	int test_case;
	scanf("%d", &test_case);

	int case_count=1;

	while(test_case--){
		float C, F, X;
		int c_count=0;
		double total_time =0.0;
		double now_c_time, now_x_time;
		double next_c_time, next_x_time;
		double nnext_c_time, nnext_x_time;

		scanf("%f %f %f", &C, &F, &X);
		
		while(true){
			now_c_time=C/(2.0+F*((c_count)*1.0));
			now_x_time=X/(2.0+F*((c_count)*1.0));

			next_c_time=C/(2.0+F*((c_count+1)*1.0));
			next_x_time=X/(2.0+F*((c_count+1)*1.0));

			nnext_c_time=C/(2.0+F*((c_count+2)*1.0));
			nnext_x_time=X/(2.0+F*((c_count+2)*1.0));

			if(nnext_c_time + nnext_x_time > next_x_time){
				total_time+=now_x_time;
				break;
			}
			else{
				total_time+=now_c_time;
				c_count++;
			}
		}
		printf("Case #%d: %.7lf\n", case_count++, total_time);
	}
}