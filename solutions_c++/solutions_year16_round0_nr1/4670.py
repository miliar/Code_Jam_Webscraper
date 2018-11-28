#include <stdio.h>
#include <string.h>

int N;
bool visited[10];

bool is_finish(){
	for(int i=0; i<=9; i++){
		if(!visited[i]){
			return false;
		}
	}
	return true;
}

int main(void){

	int testcase;
	scanf("%d", &testcase);

	for(int t_itr=1; t_itr<=testcase; t_itr++){
		scanf("%d", &N);
		
		memset(visited, false, 10);

		int res;
		bool find = false;
		for(int i=1; ; i++){
			if(N == 0){
				break;
			}
			int tmp = res = i*N;

			while(tmp > 0){
				visited[tmp%10] = true;
				tmp /= 10;
			}

			if(is_finish()){
				find = true;
				break;
			}
		}

		printf("Case #%d: ", t_itr);
		if(find){
			printf("%d\n", res);
		}
		else{
			printf("INSOMNIA\n");
		}
	}

	return 0;
}