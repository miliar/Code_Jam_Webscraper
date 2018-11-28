#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int main() {
	int tc;
	int len;
	char cake[110];
	scanf("%d", &tc);
	for (int testcase = 1; testcase <= tc; testcase++) {
		int ans = 0;
		

		scanf("%s", cake);
		len = strlen(cake);

		bool sw = false;
		int cnt = 0;
		for (int i = 0; i < len; i++) {
			if (!sw && cake[i] == '-') {
				sw = true;
				cnt++;
			}
			else if (sw && cake[i] == '+') {
				sw = false;
			}
		}
		ans = cnt * 2;
		if (cake[0] == '-') ans--;
		printf("Case #%d: ", testcase);
		printf("%d\n", ans);
	}
}