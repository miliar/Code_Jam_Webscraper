#include <cstdio>
#include <cstring>
char * solve(){
	static char output[2000];
	static char input[1001];
	memset(output,0,2000*sizeof(char));
	memset(input,0,1001*sizeof(char));
	char * first = &(output[1000]); 
	char * last = &(output[1000]);
	int current = 1;
	gets(input);
	*first = input[0];
	*last = input[0];
	while (input[current] >= 'A' && input[current] <= 'Z' ) {
		if (input[current] >= *first) {
			first--;
			*first = input[current];
		} else {
			last++;
			*last = input[current];
		}
		current++;
	}
	return first;	
}



int main(){
	int c;
	char nullChars[1000];
	scanf("%d",&c);
	gets(nullChars);
	
	for (int d = 1; d <= c; d++) {
		printf("Case #%d: %s\n",d,solve());
	}
}
