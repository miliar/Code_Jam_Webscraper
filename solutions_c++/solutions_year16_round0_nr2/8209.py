#include <cstdio>
using namespace std;

int findLastTail(char* s){
	for(int i = 100; i >= 0; i--){
		if(s[i] == '-') return i;
	}
	return -1;
}

int findFirstTail(char* s){
	for(int i = 0; i < 101; i++){
		if(s[i] == '-') return i;
	}
	return -1;
}

int findFirstHead(char* s){
	for(int i = 0; i < 101; i++){
		if(s[i] == '+') return i;
	}
	return -1;
}

void flipStack(char* s, int len){
	int c;
	int j = len;			
	for(int i = 0; i < j; i++, j--){
		c = s[i];
		s[i] = s[j];
		s[j] = c;
	}
	
	for(int i = 0; i <= len; i++){
		if(s[i] == '-') s[i] = '+';
		else s[i] = '-';
	}
}

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int tests;
	scanf("%d", &tests);
	char s[101];
	for(int t = 1; t <= tests; t++){
		scanf("%s", s);

		int flips = 0;
		while(findLastTail(s) != -1){
			int lt = findLastTail(s);
			int ft = findFirstTail(s);
			int fh = findFirstHead(s);

			if(fh < ft && fh >= 0){
				flipStack(s, ft-1);
			}
			else{
				flipStack(s, lt);
			}
			// printf("%s\n", s);

			flips++;
		}
		printf("Case #%d: %d\n", t, flips);
	}

	return 0;
}