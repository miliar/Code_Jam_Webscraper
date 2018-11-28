#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	long long P[40] = {0ll, 1ll, 4ll, 9ll, 121ll, 484ll, 10201ll, 12321ll, 14641ll, 40804ll, 44944ll, 1002001ll, 1234321ll, 4008004ll, 100020001ll, 102030201ll, 104060401ll, 121242121ll, 123454321ll, 125686521ll, 400080004ll, 404090404ll, 10000200001ll, 10221412201ll, 12102420121ll, 12345654321ll, 40000800004ll, 1000002000001ll, 1002003002001ll, 1004006004001ll, 1020304030201ll, 1022325232201ll, 1024348434201ll, 1210024200121ll, 1212225222121ll, 1214428244121ll, 1232346432321ll, 1234567654321ll, 4000008000004ll, 4004009004004ll};
	long long A, B;
	scanf("%d", &T);
	for(int t=1; t<=T; t++)
	{
		scanf("%lld %lld", &A, &B);
		printf("Case #%d: ", t);
		int a = upper_bound(P, P+40, A)-P;
		int b = upper_bound(P, P+40, B)-P;
		if(P[a-1] != A)
			printf("%d\n", b-a);
		else
			printf("%d\n", b-a+1);
	}
	return 0;
}
