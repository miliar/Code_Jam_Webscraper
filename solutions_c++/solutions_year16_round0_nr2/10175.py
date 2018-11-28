#include<stdio.h>
#include<string.h>
using namespace std;

int main() {
	freopen("B-large(1).in","r",stdin);
	freopen("output.txt","w",stdout);
	int i,t,n,k, nr;
	char s[256],p;
	scanf("%d\n",&t);
	for(i = 0; i < t; i++) {
		k = 0;
		nr = 0;
		scanf("%c",&p);
		while(p!='\n') {
			s[k] = p;
			k++;
			scanf("%c",&p);
		}
		n = strlen(s);
		for(int j = k - 1; j >= 0; j--) {
			if (s[j] == '+' && nr%2==0) {
				continue;
			}
			if (s[j] == '-' && nr%2==1) {
				continue;
			}
			nr++;	
		}
		printf("Case #%d: %d\n",i+1,nr);
	}
	return 0;
}
