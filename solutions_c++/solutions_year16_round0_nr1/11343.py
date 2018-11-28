#include <stdio.h>
#include <string.h>

int count[10] = {0};

bool check(){
	for(int i = 0; i < 10; i++){
		if(count[i] == 0) return false;
	}
	return true;
}

int main(){
	int n;
	scanf("%d", &n);
	for(int testcase = 1; testcase <= n; testcase++){
		bool flag = false;

		// init
		for(int i = 0; i < 10; i++){
			count[i] = 0;
		}

		int input, tmp = 0;
		scanf("%d", &input);
		if(input == 0){
			printf("Case #%d: INSOMNIA\n", testcase);
			continue;
		}
		int cnt = 1;
		int result;
		while(!check()){
			tmp = input * cnt++;
			result = tmp;
			// printf("tmp%d\n", tmp);
			while(tmp > 0){
				int t = tmp % 10;
				tmp /= 10;
				count[t] = 1;
			}
			

		}

		
		printf("Case #%d: %d\n", testcase, result);


		// for(int i = 0; i < 10; i++){
		// 	printf("%3d", count[i]);
		// }
		// putchar('\n');


		// char input[1000];
		// scanf("%s", input);
		// int len = strlen(input);

		// for(int i = 0; i < len; i++){
		// 	count[input[i]-'0'] = 1;
		// }

		// int num = input[0]-'0';
		// for(int i = 1; i < len; i++){
		// 	num *= 10;
		// 	int c = input[i]-'0';
		// 	num += c;
		// }



	}
	return 0;
}