#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

const int N = 101;
int t;
char S[N];

int f(int n){
	while(n>0&&S[n-1]=='+') --n;
	if (n==0) return 0;
	int res=1;
	if (S[0]=='+'){
		res++;
		for(int i=0;i<n;++i){
			if (S[i]=='+') S[i]='-';
			else break;
		}
	}
	for(int i=0;i<n;++i){
		if (S[i]=='-') S[i]='+'; else S[i]='-';
	}
	reverse(S,S+n);
	return f(n) + res;
}

int main(){
	scanf("%d\n", &t);
	for(int tt=1; tt<=t; ++tt){
		printf("Case #%d: ", tt);
		fgets(S, N, stdin);
		int n=strlen(S);
		S[--n]=0;
		int res=f(n);
		printf("%d\n",res);
	}
	return 0;
}
