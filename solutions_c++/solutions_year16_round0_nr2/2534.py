#include <iostream>
#include <string>
#include <string.h>
#include <cstdio>

#define LL long long
using namespace std;
const int maxn = 105;

char s[maxn];
int cnt(char s[]){
	int len = strlen(s), res = 0;
	for(int i=0;i<len;i++){
		if ( i==0 || s[i]!=s[i-1] )
			res++;
	}
	return res;
}

int main(){

    int t; scanf("%d", &t);
    for(int it=1;it<=t;it++){
    	scanf("%s", s); 
    	int ans = cnt(s) - 1; // strlen(s)>0
    	if ( s[strlen(s)-1]=='-' ) ans++;
    	printf("Case #%d: %d\n", it, ans );
    }

    return 0;
}