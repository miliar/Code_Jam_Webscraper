#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

char SS[1002];
int S[1002];
int K, len;
int ans;

int main()
{
	int T;
	
	freopen("input_A.txt", "r", stdin);
	freopen("output_A.txt", "w", stdout);

	scanf("%d", &T);

	for(int test_case=1;test_case<=T;test_case++)
	{
		scanf("%s %d", SS, &K);

		for(len=0;SS[len]!=0;len++)
			S[len] = (SS[len]=='+')? 1:-1;
	
		ans = 0;
		for(int i=0;i<=len-K;i++)
		{
			if(S[i]==-1)
			{
				for(int j=i;j<i+K;j++)
					S[j] *= -1;
				ans++;
			}
		}

		for(int i=len-K+1;i<len;i++)
		{
			if(S[i]==-1)
				ans = -1;
		}

		if(ans==-1)
			printf("Case #%d: IMPOSSIBLE\n", test_case);
		else
			printf("Case #%d: %d\n", test_case, ans);
	}

	return 0;
}
