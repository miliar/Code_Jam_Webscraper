#include <stdio.h>



int main() {
	int tc,max,fri,sum;
	char str[1010];
	scanf("%d",&tc);
	for(int t=1; t<=tc; t++) {
		scanf("%d",&max);
		scanf("%s",str);
		fri = sum = 0;
		for(int i=0; i<=max; i++) {
			if((str[i]-'0') == 0)
				continue;
			if(sum < i) {
				fri += (i - sum);
				sum = i;
			}
			sum += (str[i] - '0');
		}
		printf("Case #%d: %d\n",t,fri);
	}
}