#include <stdio.h>
#include <string.h>

char s[3000];
int vec[50], lit[50];

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	int T, n;
	//char mask[] = "ZWUXGOTFSI";
	
	scanf("%d", &T);
	for(int cont = 1; cont <= T; ++cont){
		for(int i = 0; i < 50; ++i)
			vec[i] = 0;
		
		for(int i = 0; i < 50; ++i)
			lit[i] = 0;
		
		
		scanf("%s", s);
		n = strlen(s);
		
		for(int i = 0; i < n; ++i){
			lit[(int)(s[i] - 'A')]++;
		}
		
		n = lit[(int)('Z' - 'A')];
		if(n > 0){
			vec[0] = n;
			lit[(int)('Z' - 'A')] -= n;
			lit[(int)('E' - 'A')] -= n;
			lit[(int)('R' - 'A')] -= n;
			lit[(int)('O' - 'A')] -= n;
		}
		
		n = lit[(int)('W' - 'A')];
		if(n > 0){
			vec[2] = n;
			lit[(int)('T' - 'A')] -= n;
			lit[(int)('W' - 'A')] -= n;
			lit[(int)('O' - 'A')] -= n;
		}
		
		n = lit[(int)('U' - 'A')];
		if(n > 0){
			vec[4] = n;
			lit[(int)('F' - 'A')] -= n;
			lit[(int)('O' - 'A')] -= n;
			lit[(int)('U' - 'A')] -= n;
			lit[(int)('R' - 'A')] -= n;
		}

		n = lit[(int)('X' - 'A')];
		if(n > 0){
			vec[6] = n;
			lit[(int)('S' - 'A')] -= n;
			lit[(int)('I' - 'A')] -= n;
			lit[(int)('X' - 'A')] -= n;
		}
		
		n = lit[(int)('G' - 'A')];
		if(n > 0){
			vec[8] = n;
			lit[(int)('E' - 'A')] -= n;
			lit[(int)('I' - 'A')] -= n;
			lit[(int)('G' - 'A')] -= n;
			lit[(int)('H' - 'A')] -= n;
			lit[(int)('T' - 'A')] -= n;
		}
		
		n = lit[(int)('O' - 'A')];
		if(n > 0){
			vec[1] = n;
			lit[(int)('O' - 'A')] -= n;
			lit[(int)('N' - 'A')] -= n;
			lit[(int)('E' - 'A')] -= n;
		}
		
		n = lit[(int)('T' - 'A')];
		if(n > 0){
			vec[3] = n;
			lit[(int)('T' - 'A')] -= n;
			lit[(int)('H' - 'A')] -= n;
			lit[(int)('R' - 'A')] -= n;
			lit[(int)('E' - 'A')] -= n;
			lit[(int)('E' - 'A')] -= n;
		}
		
		n = lit[(int)('F' - 'A')];
		if(n > 0){
			vec[5] = n;
			lit[(int)('F' - 'A')] -= n;
			lit[(int)('I' - 'A')] -= n;
			lit[(int)('V' - 'A')] -= n;
			lit[(int)('E' - 'A')] -= n;
		}
		
		n = lit[(int)('S' - 'A')];
		if(n > 0){
			vec[7] = n;
			lit[(int)('S' - 'A')] -= n;
			lit[(int)('E' - 'A')] -= n;
			lit[(int)('V' - 'A')] -= n;
			lit[(int)('E' - 'A')] -= n;
			lit[(int)('N' - 'A')] -= n;
		}
		
		n = lit[(int)('I' - 'A')];
		if(n > 0){
			vec[9] = n;
			lit[(int)('N' - 'A')] -= n;
			lit[(int)('I' - 'A')] -= n;
			lit[(int)('N' - 'A')] -= n;
			lit[(int)('E' - 'A')] -= n;
		}
		
		printf("Case #%d: ", cont);
		for(int i = 0; i < 10; ++i){
			for(int j = 0; j < vec[i]; ++j){
				printf("%d", i);
			}
		}
		
		printf("\n");
		
	}
	
	
	
return 0;	
}
