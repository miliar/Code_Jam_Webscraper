#include<cstdio>
#include<cstring>

using namespace std;

int t;
char str[105];
int main(){
	scanf("%d", &t);
	for (int tt = 1; tt<=t; tt++) {
		scanf("%s", str);
		int n = strlen(str);
		int ans = 0;
		for (int i = 1; i < n; i++) {
			if (str[i] != str[i-1])
				ans++;
		}
		if (str[n-1]=='-')
			ans++;
		printf("Case #%d: %d\n", tt, ans);
	}
	return 0;
}
