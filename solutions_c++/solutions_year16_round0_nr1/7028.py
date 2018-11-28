#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
bool has[10];

void fill(int t){
	while(t){
		has[t % 10] = true;
		t /= 10;
	}
}

bool check(){
	for(int i = 0; i < 10; i++){
		if(!has[i]){
			return false;
		}
	}
	return true;
}
int main(){
	int N, n;
	scanf("%d", &N);
	bool found = false;
	for(int icase = 1; icase <= N; icase++){
		memset(has, 0, sizeof(has));
		scanf("%d", &n);
		found = false;
		printf("Case #%d: ", icase);
		if(n == 0){
			printf("INSOMNIA\n");
			continue;
		}
		for(int i = 1; i <= 10; i++){
			int t = n * i;
			fill(t);
			if(check()){
				found = true;
				printf("%d\n", t);
				break;
			}
		}
		if(found){
			continue;
		}
		int end = -1;
		for(int i = 9; i >= 0; i--){
			if(!has[i]){
				end = i;
				break;
			}
		}
		if(end != -1){
			int t = n;
			while(t){
				end *= 10;
				t /= 10;
			}
		}
		end += (n - end % n);
		for(int i = 11; i * n <= end; i++){
			int t = n * i;
			fill(t);
			if(check()){
				found = true;
				printf("%d\n", t);
				break;
			}
		}
	}
	return 0;
}
