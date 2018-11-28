#include <iostream>

using namespace std;

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	freopen("log-small", "w", stderr);
		
	int tt;
	int size = 1002;
	
	scanf("%d",&tt);
	for(int a = 0 ; a < tt ; a++) {
		if(a > 0) {
			printf("\n");
		}
		printf("Case #%d: ", a+1);
		int sm, n=0, p=0;
		char ss[size];
		scanf("%d %s",&sm, &ss);
		
		for(int i = 0 ; i <= sm != '\0' ; i++) {
			int iss = ss[i] - '0';
			p = p + ((iss-1)*-1);
			if(p > 0) {
				n++;
				p--;
			}
			
		}
		
		printf("%d",n);
	}
	
	return 0;
}

//110011
