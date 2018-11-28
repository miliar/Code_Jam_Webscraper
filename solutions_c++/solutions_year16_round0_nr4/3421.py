#include "set"
#include "cstdio"

using namespace std;
long long ans[200];

int main(int argc, char const *argv[])
{
	int t;
	scanf("%d", &t);
	for (int testcase = 0; testcase < t; ++testcase) {
		long long k, c, s;
		scanf("%lld%lld%lld", &k, &c, &s);
		for (int i = 0; i < k; ++i)
		{
			ans[i] = i+1;
		}
		for (int i = 1; i < c; ++i)
		{
			for (int j = 0; j < k; ++j)
			{
				ans[j] = (ans[j]-1)*k+j+1;
			}
		}

		printf("Case #%d:", testcase+1);
		for (int i = 0; i < k; ++i)
		{
			printf(" %lld", ans[i]);
		}
		printf("\n");
		
	}
	return 0;
}