#include<stdio.h>
int main() {
	int t,no;
	scanf("%d",&t);
	no=1;
	while(t--) {
		int s,i;
		char ar[1005];
		scanf("%d",&s);
		scanf(" %s",&ar);
		int sum=0,total=0,ans=0;
		for(i=0;i<=s;i++) {
			if(i<=sum) {
				sum = sum+ar[i]-'0';
			}
			else if(i>sum && (ar[i]-'0')!=0) {
				total = i-sum;
				sum = sum+total+(ar[i]-'0');
				ans = ans+total;
			}
		}
		printf("Case #%d: %d\n",no,ans);
		no++;
	}
	return 0;
}