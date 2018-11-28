#include <cstdio>
#include <cstring>
using namespace std;

const int N = 1000 + 100;
char str[N];

int main()
{
	int T;
	scanf("%d", &T);

	for(int ca = 1; ca <= T; ++ca) {
		int n, s = 0, ans = 0;
		scanf("%d%s", &n, str);
		for(int i = 0; i <= n; ++i) {
			if(s < i) {
				ans += i - s;
				s = i;
			}
			s += str[i] - '0';
		}
		printf("Case #%d: %d\n", ca, ans);
	}
}