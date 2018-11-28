#include <cstdio>

int t;
int smax;
char s[1234];
int sum;
int ans;

int main()
{
scanf("%d\n", &t);

for(int q=1; q<=t; q++) {
	scanf("%d %s\n", &smax, s);
	for(int i=0; i<=smax; i++) s[i]-='0';
	sum=ans=0;
	for(int i=0; i<=smax; i++) {
		if(sum<i) {
			ans+=i-sum;
			sum+=i-sum;
		}
		sum+=s[i];
	}
	printf("Case #%d: %d\n", q, ans);
}

	return 0;
}
