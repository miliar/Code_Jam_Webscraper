#include <stdio.h>
#include <string.h>

int main(void){
	int testcase;
	scanf("%d", &testcase);

	for(int i=1; i<=testcase; i++){
		int s_max;
		char str[1200];
		int curr_standing = 0;
		int answer = 0;
		scanf("%d %s", &s_max, str);
		//printf("%d %s ", s_max, str);

		for(int j=0; j<s_max+1; j++){
			if(str[j] == '0'){
			
			}
			else{
				if(j <= curr_standing){
				
				}
				else{
					answer = answer + j - curr_standing;
					curr_standing = j;
				}
				curr_standing += str[j] - '0';
			}
		}
		printf("Case #%d: %d\n", i, answer);
	}
	return 0;
}