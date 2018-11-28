#include <bits/stdc++.h>
using namespace std;

long long t, n;
bool dig[10];

void update(long long num){
	//i10 = 1;
	for(long long i = 1; i < INT_MAX/10; i*=10){
		if(i > num){break;}
		//printf("num = %d, %d = true\n", num, (num%(i*10))/i);
		dig[(num%(i*10))/i] = true;
		//i10 *= 10;
	}
	
	/*printf("after update %d:\n", num);
	for(int i = 0; i < 10; i++){
		printf("dig[%d] = %d\n", i, dig[i]);
	}*/
}

int main(){
	scanf("%lld", &t);
	for(long long tc = 0; tc < t; tc++){
		//printf("restart\n");
		scanf("%lld", &n);
		for(int i = 0; i < 10; i++){
			dig[i] = false;
		}
		for(long long i = 1; i <= 100000; i++){
			update(i * n);
			for(int j = 0; j < 10; j++){
				if(!dig[j]){
					//printf("%d is continue, i = %d\n", j, i);
					goto contin;
				}
			}
			printf("Case #%lld: %lld\n", tc+1, i * n);
			//printf("goto, i = %d\n", i);
			goto breakage;
			contin:;
		}
		printf("Case #%lld: INSOMNIA\n", tc+1);
		breakage:;
	}
}
