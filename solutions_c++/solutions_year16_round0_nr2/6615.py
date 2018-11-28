#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

#define FFF 105
char s[FFF];

int main() {
	int n;
	freopen("out.out","w",stdout);
	scanf("%d",&n);
	for(int i = 1;i <= n; i++) {
		printf("Case #%d: ",i);
		scanf("%s",s);
		int cnt = 0;
		char now = 's';
		for(int j = 0;s[j] != '\0';j++) {
			if(now != s[j]) {
				cnt++;
				now = s[j];
			}
		}
		if(now == '+')
			cnt --;
		printf("%d\n",cnt);
	}
	return 0;
}