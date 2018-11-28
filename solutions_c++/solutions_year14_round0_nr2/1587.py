#include <cstdio>

int main()
{
	int t, caseNum = 1, i;
	double ans, now, last, c, f, x;
	scanf("%d", &t);
	while(t--){
		scanf("%lf%lf%lf", &c, &f, &x);
		ans = x / 2;
		now = 0;
		for(i = 0;1;i++){
			now += c / (2 + i * f);
			last = x / (2 + (i + 1) * f);
			if(now + last < ans)
				ans = now + last;
			else
				break;
		}
		printf("Case #%d: %lf\n", caseNum++, ans);
	}
	return 0;
}
