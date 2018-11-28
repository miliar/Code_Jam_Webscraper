#include <stdio.h>
#include <string.h>

int main()
{
	int t, c = 1, ans, smax, i, count, n;
	char people[1005];
	scanf("%d", &t);
	while(t--){
		scanf("%d %s", &smax, people);
		count = ans = 0;
		for(i = 0;i <= smax;i++){
			n = people[i] - '0';
			if(n == 0 && count == 0)
				ans += 1;
			else if(n == 0 && count != 0)
				count -= 1;
			else
				count += (n - 1);
			//printf("%d %d %d %d\n", i, n, count, ans);
		}
		printf("Case #%d: %d\n", c++, ans);
	}
	return 0;
}
