#include <cstdio>

using namespace std;

int main(){
	int tc;
	char buff[1010];
	int testcase = 1;
	scanf("%d", &tc);
	while (tc--)
	{
		int smax;
		int sum = 0;
		int ans = 0;
		scanf("%d %s", &smax,buff);
		sum = buff[0] - '0';
		for (int i = 1; i <= smax; i++){
			int tmp = buff[i] - '0';
			if (sum >= i){
				sum += tmp;
			}
			else{
				ans += (i - sum);
				sum += (i - sum);
				sum += tmp;
			}
		}
		printf("Case #%d: %d\n", testcase, ans);
		testcase++;
	}
	return 0;
}