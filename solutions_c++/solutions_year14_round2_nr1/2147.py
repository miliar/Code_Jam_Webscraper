#include <iostream>
#include <cstdio>
#include <cstring>
#define lli long long int
using namespace std;

int main() {
	// your code goes here
	lli tcase,n,c2,count,i,j,k,pca,nca,pcb,ncb,c1;
		
	scanf("%lld", &tcase);
	
	c2 = 1;
	
	while (c2 <= tcase) {
		scanf("%lld", &n);
		
		char a[102], b[102];
		
		count = 0;
		c1 = 0;
		
		scanf("%s%s", a, b);
		
		pca = a[0];
		pcb = b[0];
		
		if (pca != pcb)
			++count;
			
		for (i = 1 , j = 1; (a[i] != '\0') && (b[j] != '\0') && (count == 0) ; ) {
			if (a[i] == b[j]) {
				pca = a[i];
				pcb = b[j];
				++i;
				++j;
				
			} else if (a[i] == pcb) {
				pca = a[i];
				++i;
				++c1;
			} else if (b[j] == pca) {
				pcb = b[j];
				++j;
				++c1;
			} else {
				++count;
				break;
			}
		}
		
		if (a[i] != '\0' && count == 0) {
			for (; a[i] != '\0'; ++i) {
				if (a[i] == pcb)
					++c1;
				else  {
					++count;
					break;
				}
			}
		}
		
		if (b[j] != '\0' && count == 0) {
			for (; b[j] != '\0'; ++j) {
				if (b[j] == pca)
					++c1;
				else {
					++count;
					break;
				}
			}
		}
		
		if (count > 0)
			printf("Case #%lld: Fegla Won\n", c2);
		else
			printf("Case #%lld: %lld\n", c2, c1);
		++c2;
	}
		
	return 0;
}