#include <stdio.h>
#include <string.h>

int main(){
	int t;
	scanf(" %d", &t);
	for(int k = 1; k <= t; k++){
		char s[150];
		scanf(" %s", s);
		int res = 0, len = strlen(s);
		for(int i = 1; i < len; i++){
			if(s[i] != s[i-1])
				res++;
		}
		if(s[len-1] != '+')
			res++;
		
		printf("Case #%d: %d\n", k, res);
	}
	return 0;
}