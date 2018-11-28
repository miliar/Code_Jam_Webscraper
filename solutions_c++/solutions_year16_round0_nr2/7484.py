#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	// your code goes here
	FILE  *inp, *op;
	inp = fopen("B-large.in", "r");
	op = fopen("output2.txt", "w");

	int tc, t, f, cnt, i, minus;
	char a[105];
	
	fscanf(inp, "%d", &tc);
	t = 0;
	while(t++ < tc) {
		fscanf(inp, "%s", a);
		fprintf(op, "Case #%d: ",t);
		i = 0;
		f =0;
		cnt = 0;
		minus = 0;
		while(a[i]) {
			if(minus == 0 && a[i] =='+') {
				f = 1;
				
			}
			if(a[i]=='+' && minus!=0){
				if(f ==0)
				cnt++;
				else cnt+=2;
				minus = 0;
				f=1;
			} else if(a[i]== '-') {
				minus++;
			}
			i++;
		}
		if(minus!=0) {
			if(f==0)
				cnt++;
			else cnt+=2;				
		}
		fprintf(op, "%d\n", cnt);
		//cout<<cnt;
	}
	
	return 0;
	
}
