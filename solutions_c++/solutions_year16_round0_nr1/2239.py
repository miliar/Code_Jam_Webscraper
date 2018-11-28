#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <set>
#include <vector>
#include <map>

using namespace std;

bool fg[10];
int main(int argc, char const *argv[])
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T = 0;
	int cas = 0;
	scanf("%d", &T);
	while(T--) {
		cas++;
		long long n;
		scanf("%lld", &n);
		printf("Case #%d: ", cas);
		if(n == 0) {
			puts("INSOMNIA");
			continue;
		}
		memset(fg, 0, sizeof(fg));
		int cnt = 0;
		long long now = 0, tmp;
		int over = 0;
		while(1) {
			now += n;
			cnt++;
			tmp = now;
			while(tmp) {
				int x = tmp % 10;
				if(!fg[x]) {
					fg[x] = 1;
					over++;
				}
				tmp /= 10;
			}
			if(over == 10) {
				break;
			}
		}
		printf("%lld\n", now);
	}
	return 0;
} 