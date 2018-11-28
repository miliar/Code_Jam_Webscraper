#include<stdio.h>
#include<iostream>
#include<map>
#include<vector>
#include<string>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;
int main()
{
	int cases;
	scanf("%d", &cases);
	for(int i1 = 1;i1 <= cases;i1++) {
		int n;
		scanf("%d", &n);
		char s[n+2];
		scanf("%s", &s);

		int count = (int)s[0] - 48;
		int ans = 0;
		for(int i = 1;i <= n;i++) {
			int t = s[i] - 48;
			if(count >= i) {
				count += t;
			}else {
				ans += i-count;
				count += i - count + t;
			}
		}
		printf("Case #%d: %d\n",i1, ans);
	}
	return 0;
}
