#include <stdio.h>

int t,i,j;
int smax, length;
char shy[1005];
int stand;
int needed;

int main () {
	
	scanf("%d\n",&t);
	for(i=1;i<=t;i++) {
		scanf("%d %s\n",&smax, shy);
		length = smax+1;
		
		needed = 0;
		stand = shy[0]-'0';
		for(j=1;j<length;j++) {
			if(shy[j]-'0'>0) {
				if(stand < j) { 
					needed += j-stand;
					stand += j-stand;
				}
				stand += (shy[j]-'0');
			}
		}
		
		printf("Case #%d: %d\n",i,needed);
	}
	
	
	return 0;
}
