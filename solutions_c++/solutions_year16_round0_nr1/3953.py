#include <bits/stdc++.h>
using namespace std;
int t, n;
int f(int num){
	int M = 0;
	while(true){
		M |= (1<<(num%10));
		num /= 10;
		if(num==0) break;
	}
	return M;
}
int main(){
	scanf("%d", &t);
	for(int c=1; c<=t; c++){
		scanf("%d", &n);
		int M = 0;
		printf("Case #%d: ", c);
		if(n==0) printf("INSOMNIA\n");
		else{
			int i = 1;
			while(true){
				M |= f(n*i);
				if(M==(1<<10)-1){
					printf("%d\n", i*n);
					break;
				}
				i++;
			}
		}
	}
	return 0;
}