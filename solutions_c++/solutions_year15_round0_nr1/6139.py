#include<cstdio>

int main(void){
	int t, smax, i, count, sum, extra, c=1;
	char s[1001];
	scanf("%d",&t);
	while(t--){
		count=0;
		sum=0;
		scanf("%d",&smax);
		scanf("%s",s);
		for(i=0;i<=smax;i++){
			extra=0;
			if(sum<=i-1)
				extra=i-sum;
			count+=extra;
			sum = sum+int(s[i]-48)+extra;
		}
		printf("Case #%d: %d\n", c,count);
		c++;

	}
}