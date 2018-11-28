#include <stdio.h>
#include <string>

int main()
{
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		char str[2000];
		scanf(" %s", str);
		int n = strlen(str);
		std::string res;
		for (int i=0; i<n; i++) {
			if (i==0) {
				res = str[i];
				continue;
			}
			if (res[0] <= str[i]) {
				res = str[i] + res;
			} else {
				res += str[i];
			}
		}
		printf("Case #%d: %s\n", t, res.c_str());
	}
	return 0;
}