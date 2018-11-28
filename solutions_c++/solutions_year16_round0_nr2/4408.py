#include <bits/stdc++.h>
using namespace std;

FILE *in = fopen("fl.in", "r");
FILE *out = fopen("fl.out", "w");

char inp[111];

void doit(int i){
	reverse(inp, inp + i + 1);
	for(int q = 0; q <= i; q++){
		if(inp[q] == '+'){
			inp[q] = '-';
		}
		else{
			inp[q] = '+';
		}
	}
}

int main(){
	int ntest;
	fscanf(in, "%d\n", &ntest);
	for(int test = 1; test <= ntest; test++){
		fscanf(in, "%s", inp);
		int result = 0;
		for(int q = strlen(inp) - 1; q >= 0; q--){
			if(inp[q] == '-'){
				if(inp[0] == '-'){
					doit(q);
					result ++;
				}
				else{
					for(int w = 0; inp[w] == '+' && w < q; w++){
						inp[w] = '-';
					}
					result += 2;
					doit(q);
				}
			}
		}
		fprintf(out, "Case #%d: %d\n", test, result);
	}
	return 0;
}