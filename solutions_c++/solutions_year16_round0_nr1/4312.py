#include<cstdio>

int getDigits(int n){
	int res = 0;

	while(n != 0){
		res |= (1 << (n%10));
		n /= 10;
	}
	 return res;
}

int main(){
	int T;
	scanf("%d", &T);

	//printf("%d",getDigits(T));
	int cnt=0;
	while(cnt < T){
		int N;
		scanf("%d",&N);

		if(N == 0){
			printf("Case #%d: INSOMNIA\n",cnt+1);
			cnt++;
			continue;
		}

		int stopAt = 1023;
		int flag = 0;
		int atNum = N;

		while(flag != stopAt){
			flag |= getDigits(atNum);
			atNum += N;
		}

		printf("Case #%d: %d\n",cnt+1,atNum-N);


		cnt++;
	}
}
