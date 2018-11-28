#include <cstdio>
int main () {
	int n;
	scanf("%d", &n);
	for (int i=1; i<=n; i++) {
		int maxi;
		scanf("%d", &maxi);
		char s[1001];
		scanf(" %s", s);
		int sum=0, ans=0;
		for (int j=0; j<maxi+1; j++) {
			int temp = s[j]-'0';
			if (temp>0&&sum<j) {
				ans+=j-sum;
				sum+=j-sum;
			}
			sum+=temp;
		}
		printf("Case #%d: %d\n", i, ans);
	}
	return 0;
}
