#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	// your code goes here
	FILE  *inp, *op;
	inp = fopen("A-large.in", "r");
	op = fopen("output1.txt", "w");

	int tc, t;
	long long int i, n, cnt, ans, r, k, s, mark[11];
	
	fscanf(inp, "%d", &tc);
	//cout<<tc;
	t = 0;
	while(t++ < tc) {
		fscanf(inp, "%lld", &n);
		fprintf(op, "Case #%d: ",t);
		if(n==0){
			fprintf(op, "INSOMNIA\n");
		}
		else {
			
			for(i=0;i<11;i++) mark[i] = 0;
			cnt = 1;
			s = 0;
			while(1) {
				k = cnt*n;
				while(k) {
					r = k%10;
					k/=10;
					if(mark[r]==0) {
						mark[r]=1;
						s+=r;		
					} 
					
				}
				if(s == 45 && mark[0]==1) {
					ans = cnt*n;
					break;
				}
				cnt++;
			}
			fprintf(op, "%lld\n", ans);
		//	cout<<ans<<endl;
		}
	}
	
	return 0;
	
}
