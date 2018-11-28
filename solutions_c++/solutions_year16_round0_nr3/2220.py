#include <cstdio>

int T;
int N, J;
bool table[32];
int ct;

void print(int pos){
	if(pos == N - 1){
		ct++;
		for(int i = 0; i < N; i++)
			if(table[i])
				printf("1");
			else 
				printf("0");
		for(int i = 2; i <= 10; i++)
			printf(" %d", i + 1);
		printf("\n");

		return;
	}
	if(ct < J)print(pos + 2);
	table[pos] = table[pos + 1] = 1;
	if(ct < J)print(pos + 2);
	table[pos] = table[pos + 1] = 0;
}

int main(){
	scanf("%d", &T);
	for(int tt = 1; tt <= T; tt++){
		scanf("%d %d", &N, &J);
		table[0] = 1;
		table[N - 1] = 1;
	
		printf("Case #%d:\n", tt);
		print(1);
	}
}