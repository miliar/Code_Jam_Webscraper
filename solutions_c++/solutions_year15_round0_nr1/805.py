#include <cstdio>
#include <algorithm>
using namespace std;

int T;
int Smax;
char in[1010];

int main()
{
	scanf("%d", &T);

	for (int t = 0; t++ < T;) {
		scanf("%d%s", &Smax, in);

		int ret = 0, sum = 0;
		for (int i = 0; i <= Smax; ++i) {
			if (in[i] == '0') continue;
			
			int ad = max(0, i - sum);
			ret += ad;
			sum += ad;
			sum += in[i] - '0';
		}
		printf("Case #%d: %d\n", t, ret);
	}
	return 0;
}
