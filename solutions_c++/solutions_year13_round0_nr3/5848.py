#include <cstdio>
#include <cstring>

int check(char number[1000]);

int main(int argc, char *argv[]){
	int T;
	scanf("%d\n",&T);
	char is[1024*1024];
	for(int i=0; i<1001; i++){
		is[i]=0;
	}
	for(int i=0; i*i<=1000;i++){
		char buff1[1000];
		char buff2[1000];
		sprintf(buff1,"%d",i);
		sprintf(buff2,"%d",i*i);
		if(check(buff1) && check(buff2)){
			//printf("%d\n",i*i);
			is[i*i] = 1;
		}
	}
	for(int cases=0; cases<T; cases++){
		int res;
		int a, b;
		scanf("%d %d\n", &a, &b);
		res=0;
		for(int i=a; i<=b; i++){
			res+=is[i];
		}
		printf("Case #%d: %d\n",cases+1, res);
	}
	
}

int check(char number[1000]){
	int len = strlen(number);
	for(int i=0, j=len-1; i<j; i++, j--){
		if(number[i]!=number[j]){
			return 0;
		}
	}
	return 1;
}


