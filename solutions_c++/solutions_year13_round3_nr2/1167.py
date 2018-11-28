#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define MID 15000
#define YMAX 50
char str[1000009];
char lib[1000009];
int n;
int isvow(char c){
	switch(c){
		case 'a':case 'e':case 'i':case 'o':case'u':
			return 1;
		default:
			return 0;
	}
}
long solve(){
	memset(lib,0,sizeof(lib));
	int L =strlen(str);
	int tmp=0;
	for(int i=0;i<L;i++){
		if(isvow(str[i]))
			tmp=0;
		else
			tmp++;
		lib[i]=tmp;

	}
	tmp =0;
	long res=0;
	for(int i=0;i<L;i++){
		if(lib[i]>=n)
			tmp = i-n+2;
		res +=tmp;
	}
	return res;
}
int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		scanf("%s%d",str, &n);
		printf("Case #%d: %ld\n",t,solve());
	}

}
